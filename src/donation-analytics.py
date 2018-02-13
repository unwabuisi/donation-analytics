####################################################
# IMPORT LIBRARIES
import os
import math

####################################################
# FILE ACCESS & MANIPULATION FUNCTIONS
def readPercentile(filename):
    #this function reads the percentile text file and sets the variable 'percentile' to whatever value is in the first line of the text file.
    filehandle = open(filename)
    for l in filehandle:
        percentile = l
    return percentile

####################################################
# DATA MANIPULATION FUNCTIONS
def percentileCalculator(p, big_N, listOfValues):
    # This function calculates the percentile value using the nearest-rank method on a list
    # big_N is the LENGTH of the list
    p = float(p)
    big_N = float(big_N)
    small_n = (p/100)*big_N
    small_n = int(math.ceil(small_n))
    return listOfValues[small_n - 1]

def infoParse(filename):
    # This function opens the file and reads each line, puts each block of data into an array index, using '|' as the delimter
    # Only valid data is saved, invalid or malformed data is ignored

    filehandle = open(filename)
    for l in filehandle:
        record = l.strip().split("|")

        if check_transaction_date(record) and check_zip_code(record) and check_name(record) and check_CMTE_ID(record) and check_transaction_amt(record) and check_otherID(record): # Checks to make sure current line data is valid

            # Here, each only the important data values are extracted and put into separate arrays, retaining the original order
            current_cmte_id = record[0]
            current_name = record[7]
            current_zip_code = record[10][:5] #only first 5 digits of zip code are used
            current_transaction_date = record[13][-4:]
            current_transaction_amt = record[14]

            # Before appending the record to the NAME list, this loop checks to see if there is already a record with the same name in the master NAME list.
            # If so, that means it is a duplicate and this loop it will add that record to a separate array list of duplicates (duplicate_donations)
            for i in NAME_LIST:
                if i == current_name:

                    # print "\n--------------------DUPLICATE FOUND-----------------------\n"
                    # print "Current Iteration: " + str(len(NAME_LIST))
                    # print "NAMES: " + str(NAME_LIST)
                    # print "Matching NAME: " + str(current_name) + " - " + "Index: (" + str(NAME_LIST.index(current_name)) + ")"

                    orig_record = NAME_LIST.index(current_name)
                    dupe_record = len(duplicate_donor_name)
                    duplicate_donor_cmte_ID.append(current_cmte_id)
                    duplicate_donor_name.append(current_name)
                    duplicate_donor_zipCode.append(current_zip_code)
                    duplicate_donor_transaction_dt.append(current_transaction_date)
                    duplicate_donor_transaction_amt.append(current_transaction_amt)
                    duplicate_donations.append(record)

                    # print "Original Record: " + str(CMTE_ID_LIST[orig_record]) + " " + str(NAME_LIST[orig_record]) + " " + str(ZIP_CODE_LIST[orig_record]) + " " + str(TRANSACTION_DT_LIST[orig_record][-4:]) + " " + str(TRANSCTION_AMT_LIST[orig_record])
                    # print "Duplicate Record: " + str(duplicate_donor_cmte_ID[dupe_record]) + " " + str(duplicate_donor_name[dupe_record]) + " " + str(duplicate_donor_zipCode[dupe_record]) + " " + str(duplicate_donor_transaction_dt[dupe_record][-4:]) + " " + str(duplicate_donor_transaction_amt[dupe_record])
                    # print "\n-----------------------------------------------------------\n"

            #Here, each valid record is entered into separate lists based on data type
            CMTE_ID_LIST.append(current_cmte_id)
            NAME_LIST.append(current_name)
            ZIP_CODE_LIST.append(current_zip_code)
            TRANSACTION_DT_LIST.append(current_transaction_date)
            TRANSCTION_AMT_LIST.append(current_transaction_amt)

    filehandle.close()

def repeatDonors(dupeList):
        # Here we want to identify repeat donors giving to the SAME RECIPIENT (CMTE_ID) from the SAME ZIP CODE (ZIP_CODE) in the SAME CALENDAR YEAR (TRANSACTION_DATE)
        # OUTPUT CMTE_ID | ZIPCODE | CALENDAR YEAR | PERCENTILE | TOTAL CONTRIBUTION AMOUNTS | # OF CONTRIBUTIONS THAT MATCH (CMTE_ID, ZIP_CODE, YYYY)

    numOfRepeatDonors = 1
    transaction_amounts = {} #transaction amounts and number of donors are stored together
    transaction_amounts_list = []
    zipcodes = {} #zipcodes and their number of donors are stored in dictionary data structure
    i = 0
    while i < len(dupeList):
        if duplicate_donor_cmte_ID.count(duplicate_donor_cmte_ID[i]) > 1 and duplicate_donor_zipCode.count(duplicate_donor_zipCode[i]) > 1 and duplicate_donor_transaction_dt.count(duplicate_donor_transaction_dt[i]) > 1: # Same CTMID && ZIP CODE

            if duplicate_donor_zipCode[i] not in zipcodes: #this if/else statement checks if a zipcode already has a donation listed. If so, it will update the number of donors + 1
                zipcodes[duplicate_donor_zipCode[i]] = numOfRepeatDonors
                transaction_amounts[duplicate_donor_zipCode[i]] = int(duplicate_donor_transaction_amt[i])
            else:
                zipcodes[duplicate_donor_zipCode[i]] += 1
                transaction_amounts[duplicate_donor_zipCode[i]] += int(duplicate_donor_transaction_amt[i])

            transaction_amounts_list.append(dupeList[i][14])

            print str(dupeList[i][0]) + "|" + str(dupeList[i][10][:5]) + "|" + str(dupeList[i][13][-4:]) + "|" + percentileCalculator(percentile, len(transaction_amounts_list), transaction_amounts_list) + "|" + str(transaction_amounts[dupeList[i][10][:5]]) + "|" + str(zipcodes[dupeList[i][10][:5]])

            # print duplicate_donor_cmte_ID[i] + " " + duplicate_donor_zipCode[i] + " " + duplicate_donor_transaction_dt[i] + " " + duplicate_donor_name[i] + " " + duplicate_donor_transaction_amt[i]


        elif duplicate_donor_cmte_ID.count(duplicate_donor_cmte_ID[i]) > 1: #Multiple contributions to the same CMTE_ID but not from the same ZIP CODE

            transaction_amounts_list.append(dupeList[i][14])
            print str(dupeList[i][0]) + "|" + str(dupeList[i][10][:5]) + "|" + str(dupeList[i][13][-4:]) + "|" + percentileCalculator(percentile, len(transaction_amounts_list), transaction_amounts_list) + "|" + dupeList[i][14] + "|" + str(numOfRepeatDonors)
            # print duplicate_donor_cmte_ID[i] + " " + duplicate_donor_zipCode[i] + " " + duplicate_donor_transaction_dt[i] + " " + duplicate_donor_name[i] + " " + duplicate_donor_transaction_amt[i]


        else: #Just one duplicate donation from these zip codes
            transaction_amounts_list.append(dupeList[i][14])
            print str(dupeList[i][0]) + "|" + str(dupeList[i][10][:5]) + "|" + str(dupeList[i][13][-4:]) + "|" + percentileCalculator(percentile, len(transaction_amounts_list), transaction_amounts_list) + "|" + dupeList[i][14] + "|" + str(numOfRepeatDonors)
            # print duplicate_donor_cmte_ID[i] + " " + duplicate_donor_zipCode[i] + " " + duplicate_donor_transaction_dt[i] + " " + duplicate_donor_name[i] + " " + duplicate_donor_transaction_amt[i]

        # print transaction_amounts_list
        i +=1

    # print duplicate_donor_cmte_ID
    # print "OUTPUT: " + str(dupeList[0][0]) + "|" + str(dupeList[0][10][:5]) + "|" + str(dupeList[0][13][-4:]) + "|" + "percentile" + "|" + dupeList[0][14] + "|" + str(numOfRepeatDonors)
    return

#####################################################
# DATA VALIDATION FUNCTIONS
def check_transaction_date(record):
    # This function checks the transaction date to make sure it is a valid date within 12 months, 31 days, and years 2013 - 2020
    valid = False

    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22','23','24','25','26','27', '28', '29', '30', '31']
    years = ['13','14','15','16','17','18','19','20']

    if len(record[13]) == 8:
        s = record[13]
        r = [s[i:i+2] for i in xrange(0, len(s), 2)] #This splits the string into MM/DD/YYY format to make compare each subset and make sure the date is valid
        if r[0] in months and r[1] in days and r[2] in years and r[3] in years:
            valid = True
            return valid
    return valid
def check_zip_code(record):
    #Checks zip code to make sure it is a valid zipcode with at least 5 digits and less than 9
    valid = False

    if len(record[10]) >= 5 and len(record[10]) <= 9:
        valid = True
    return valid
def check_name(record):
    #Checks to make sure name is valid string with no numbers or other characters. Also name must not be empty or more than 200 characters
    valid = False

    numbersAndCharacters = ['0','1','2','3','4','5','6','7','8','9','!','@','#','$','^','&','*']
    if len(record[7]) <= 200 and len(record[7]) != 0:
        name = str(record[7]) #converts to string and makes sure there are no numbers or other characters in the Name
        for i in name:
            if i in numbersAndCharacters:
                valid = False
                return valid
            else:
                valid = True
    return valid
def check_CMTE_ID (record):
    #Checks to make sure CMTE_ID is not empty
    valid = False

    if len(record[0]) != 0:
        valid = True
    return valid
def check_transaction_amt(record):
    #Checks to make sure transaction amount is not empty
    valid = False

    if len(record[14]) != 0:
        valid = True
    return valid
def check_otherID(record):
    #Checks to make sure Other ID is an empty field --> "Because we are only interested in individual contributions, we only want records that have the field, OTHER_ID, set to empty"
    valid = False

    if record[15] == " " or record[15] == "":
        valid = True
    return valid

######################################################
#GLOBAL VARIABLES
CMTE_ID_LIST = []
NAME_LIST = []
ZIP_CODE_LIST = []
TRANSACTION_DT_LIST = []
TRANSCTION_AMT_LIST = []
OTHER_ID_LIST = []

duplicate_donations = []
duplicate_donor_cmte_ID = []
duplicate_donor_name = []
duplicate_donor_zipCode = []
duplicate_donor_transaction_dt = []
duplicate_donor_transaction_amt = []

percentile = readPercentile(filename_percentile)

########################################################
# FILE ACCESS & VARIABLES
fileDir = os.path.dirname(os.path.realpath('__file__'))

filename = os.path.join(fileDir, './Github/donation-analytics/insight_testsuite/tests/test_1/input/itcont.txt')
filename = os.path.abspath(os.path.realpath(filename))
filename_percentile = os.path.join(fileDir, './Github/donation-analytics/insight_testsuite/tests/test_1/input/percentile.txt')
filename_percentile = os.path.abspath(os.path.realpath(filename_percentile))
filename_output = os.path.join(fileDir, './Github/donation-analytics/output/repeat_donors.txt')
filename_output = os.path.abspath(os.path.realpath(filename_output))

########################################################
# START OF PROGRAM

infoParse(filename)

# repeatDonors(duplicate_donations)
