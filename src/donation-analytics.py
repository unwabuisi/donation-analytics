
import os
import math

def readFile(filename):
    filehandle = open(filename)
    for l in filehandle:
        row = l.strip().split("|")
        # print "CMTE_ID: " + row[0] + "\nNAME: " + row[7] +"\nZIP_CODE: " + row[10] +"\nTRANSACTION_DT: " + row[13] +"\nTRANSACTION_AMT: " + row[14] +"\nOTHER_ID: " + row[15] + "\n-----------------------------------\n"
    # print filehandle.read()
    filehandle.close()

def readPercentile(filename):
    filehandle = open(filename)
    for l in filehandle:
        percentile = l
    return percentile
def percentileCalculator(p, big_N, listOfValues):
    #This function calculates the percentile value using the nearest-rank method on an ordered list
    # big_N is the LENGTH if the list
    p = float(p)
    big_N = float(big_N)
    small_n = (p/100)*big_N
    small_n = int(math.ceil(small_n))
    return listOfValues[small_n - 1]

def infoParse(filename):
    filehandle = open(filename)
    for l in filehandle:
        record = l.strip().split("|")

        if check_transaction_date(record) and check_zip_code(record) and check_name(record) and check_CMTE_ID(record) and check_transaction_amt(record) and check_otherID(record): # Checks to make sure current line data is valid

            current_cmte_id = record[0]
            current_name = record[7]
            current_zip_code = record[10][:5] #only first 5 digits of zip code are used
            current_transaction_date = record[13][-4:]
            current_transaction_amt = record[14]

            # Before appending the record to the NAME list, this loop checks to see if there is already a record with the same name in the master NAME list.
            # If so, that means it is a duplicate and this loop it will add that record to a separate list of duplicates (duplicate_donations)

            for i in NAME_LIST:
                if i == current_name:
                    # print "\n--------------------DUPLICATE-----------------------\n"
                    # print "Index: " + str(NAME_LIST.index(current_name)) + " - " + str(current_name)
                    # print "Current Dupe: " + str(len(NAME_LIST))

                    orig_record = NAME_LIST.index(current_name)
                    dupe_record = len(duplicate_donor_name)
                    duplicate_donor_cmte_ID.append(current_cmte_id)
                    duplicate_donor_name.append(current_name)
                    duplicate_donor_zipCode.append(current_zip_code)
                    duplicate_donor_transaction_dt.append(current_transaction_date)
                    duplicate_donor_transaction_amt.append(current_transaction_amt)
                    duplicate_donations.append(record)

                    # print "Names Array: " + str(NAME_LIST)
                    # print "Duplicate Name Array: " + str(duplicate_donor_name)

                    # print "Original Record: " + str(CMTE_ID_LIST[orig_record]) + " " + str(NAME_LIST[orig_record]) + " " + str(ZIP_CODE_LIST[orig_record]) + " " + str(TRANSACTION_DT_LIST[orig_record][-4:]) + " " + str(TRANSCTION_AMT_LIST[orig_record])
                    # print "Duplicate Record: " + str(duplicate_donor_cmte_ID[dupe_record]) + " " + str(duplicate_donor_name[dupe_record]) + " " + str(duplicate_donor_zipCode[dupe_record]) + " " + str(duplicate_donor_transaction_dt[dupe_record][-4:]) + " " + str(duplicate_donor_transaction_amt[dupe_record])

                    ## TEST OUTPUT ##
                    # print "\nOUTPUT: " + str(duplicate_donor_cmte_ID[dupe_record]) + "|" + str(duplicate_donor_transaction_dt[dupe_record][-4:]) + "|" + str(duplicate_donor_transaction_amt[dupe_record]) + "\n--------"

            #Here, each valid record is entered into separate lists based on data type
            CMTE_ID_LIST.append(current_cmte_id)
            NAME_LIST.append(current_name)
            ZIP_CODE_LIST.append(current_zip_code)
            TRANSACTION_DT_LIST.append(current_transaction_date)
            TRANSCTION_AMT_LIST.append(current_transaction_amt)

            # print "\n\nCMTE_ID: " + record[0] + "\nNAME: " + record[7] +"\nZIP_CODE: " + record[10] +"\nTRANSACTION_DT: " + record[13] +"\nTRANSACTION_AMT: " + record[14] +"\nOTHER_ID: " + record[15] + "\n-----------------------------------\n"

def duplicateCounter(list):
    # Here we want to identify repeat donors giving to the SAME RECIPIENT (CMTE_ID) from the SAME ZIP CODE (ZIP_CODE) in the SAME CALENDAR YEAR (TRANSACTION_DATE)
    # OUTPUT CMTE_ID | ZIPCODE | CALENDAR YEAR | PERCENTILE | TOTAL CONTRIBUTION AMOUNTS | # OF CONTRIBUTIONS THAT MATCH (CMTE_ID, ZIP_CODE, YYYY)

    print duplicate_donor_cmte_ID
    # print duplicate_donor_transaction_dt


    i = 0
    while i < len(duplicate_donor_cmte_ID):

        # if duplicate_donor_cmte_ID.count(duplicate_donor_cmte_ID[i]) > 1: # There is more than one duplicate record with the same CMTE_ID
            # print duplicate_donor_cmte_ID[i] + " DUPE"

        # else:
            # print duplicate_donor_cmte_ID[i]

            # if duplicate_donor_zipCode.count(duplicate_donor_zipCode[i]) > 1: # There is more than one duplicate record with the same Zip Code

                # if duplicate_donor_transaction_dt.count(duplicate_donor_transaction_dt[i]) > 1: # There is more than one duplicate record donation within the same calendar year

        # print duplicate_donor_cmte_ID[i]
        # print duplicate_donor_cmte_ID.count(duplicate_donor_cmte_ID[i])

        # if duplicate_donor_cmte_ID.count(duplicate_donor_cmte_ID[i]) == 1:
            # newList.append(duplicate_donor_cmte_ID[i])

        i +=1

    w = []
    x = []
    y = []
    z = []

    j = 0
    while j < len(duplicate_donor_cmte_ID):

        if duplicate_donor_zipCode.count(duplicate_donor_zipCode[j]) > 1 and duplicate_donor_cmte_ID.count(duplicate_donor_cmte_ID[j]) > 1 and duplicate_donor_transaction_dt.count(duplicate_donor_transaction_dt[j]) > 1: # Same CTMID && ZIP CODE
            # print "\n----------------ALL-------------------------\n"
            # print duplicate_donor_cmte_ID[j] + " " + duplicate_donor_zipCode[j] + " " + duplicate_donor_transaction_dt[j] + " " + duplicate_donor_name[j] + " " + duplicate_donor_transaction_amt[j]
            x.append(duplicate_donations[j])

        elif duplicate_donor_cmte_ID.count(duplicate_donor_cmte_ID[j]) > 1:
            # print "\n------------------ONE-----------------------\n"
            # print duplicate_donor_cmte_ID[j] + " " + duplicate_donor_zipCode[j] + " " + duplicate_donor_transaction_dt[j] + " " + duplicate_donor_name[j] + " " + duplicate_donor_transaction_amt[j]
            y.append(duplicate_donations[j])

        else: #Just one duplicate donation from these zip codes
            # print "\n------------------NONE-----------------------\n"
            # print duplicate_donor_cmte_ID[j] + " " + duplicate_donor_zipCode[j] + " " + duplicate_donor_transaction_dt[j] + " " + duplicate_donor_name[j] + " " + duplicate_donor_transaction_amt[j]
            z.append(duplicate_donations[j])
        j +=1

    print len(x)
    print x[0][0] + ' ' + x[0][10][-5:]
    print x[1][0] + ' ' + x[1][10][-5:]
    print x[2][0] + ' ' + x[2][10][-5:]
    print x[3][0] + ' ' + x[3][10][-5:]

    print len(y)
    print y[0][0] + ' ' + y[0][10][-5:]
    print y[1][0] + ' ' + y[1][10][-5:]
    print y[2][0] + ' ' + y[2][10][-5:]

    print len(z)
    print z[0][0] + ' ' + z[0][10][-5:]
    print z[1][0] + ' ' + z[1][10][-5:]
    print z[2][0] + ' ' + z[2][10][-5:]


    # k = 0
    # while k < len(x):
    #     if x[k] in x

def repeatDonors(dupeList):
        # Here we want to identify repeat donors giving to the SAME RECIPIENT (CMTE_ID) from the SAME ZIP CODE (ZIP_CODE) in the SAME CALENDAR YEAR (TRANSACTION_DATE)
        # OUTPUT CMTE_ID | ZIPCODE | CALENDAR YEAR | PERCENTILE | TOTAL CONTRIBUTION AMOUNTS | # OF CONTRIBUTIONS THAT MATCH (CMTE_ID, ZIP_CODE, YYYY)

    numOfRepeatDonors = 1
    transaction_amounts = []
    zipcodes = {} #zipcodes and their number of donors are stored in dictionary data structure
    i = 0
    while i < len(dupeList):
        if duplicate_donor_cmte_ID.count(duplicate_donor_cmte_ID[i]) > 1 and duplicate_donor_zipCode.count(duplicate_donor_zipCode[i]) > 1 and duplicate_donor_transaction_dt.count(duplicate_donor_transaction_dt[i]) > 1: # Same CTMID && ZIP CODE

            if duplicate_donor_zipCode[i] not in zipcodes: #this if/else statement checks if a zipcode already has a donation listed. If so, it will update the number of donors + 1
                zipcodes[duplicate_donor_zipCode[i]] = numOfRepeatDonors
            else:
                zipcodes[duplicate_donor_zipCode[i]] += 1

            print "OUTPUT: " + str(dupeList[i][7]) + "  -   " + str(dupeList[i][0]) + "|" + str(dupeList[i][10][:5]) + "|" + str(dupeList[i][13][-4:]) + "|" + "percentile" + "|" + dupeList[i][14] + "|" + str(zipcodes[dupeList[i][10][:5]])

            # print duplicate_donor_cmte_ID[i] + " " + duplicate_donor_zipCode[i] + " " + duplicate_donor_transaction_dt[i] + " " + duplicate_donor_name[i] + " " + duplicate_donor_transaction_amt[i]


        elif duplicate_donor_cmte_ID.count(duplicate_donor_cmte_ID[i]) > 1: #Multiple contributions to the same CMTE_ID but not from the same ZIP CODE
            print "OUTPUT2: " + str(dupeList[i][7]) + "  -   " + str(dupeList[i][0]) + "|" + str(dupeList[i][10][:5]) + "|" + str(dupeList[i][13][-4:]) + "|" + "percentile" + "|" + dupeList[i][14] + "|" + str(numOfRepeatDonors)
            # print duplicate_donor_cmte_ID[i] + " " + duplicate_donor_zipCode[i] + " " + duplicate_donor_transaction_dt[i] + " " + duplicate_donor_name[i] + " " + duplicate_donor_transaction_amt[i]


        else: #Just one duplicate donation from these zip codes
            print "OUTPUT3: " + str(dupeList[i][7]) + "  -   " + str(dupeList[i][0]) + "|" + str(dupeList[i][10][:5]) + "|" + str(dupeList[i][13][-4:]) + "|" + "percentile" + "|" + dupeList[i][14] + "|" + str(numOfRepeatDonors)
            # print duplicate_donor_cmte_ID[i] + " " + duplicate_donor_zipCode[i] + " " + duplicate_donor_transaction_dt[i] + " " + duplicate_donor_name[i] + " " + duplicate_donor_transaction_amt[i]

        i +=1

    # print duplicate_donations
    # print "OUTPUT: " + str(dupeList[0][0]) + "|" + str(dupeList[0][10][:5]) + "|" + str(dupeList[0][13][-4:]) + "|" + "percentile" + "|" + dupeList[0][14] + "|" + str(numOfRepeatDonors)
    return

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

duplicate_output = []

########################################################

#For accessing the txt file
fileDir = os.path.dirname(os.path.realpath('__file__'))
# print fileDir

# filename = os.path.join(fileDir, './Github/donation-analytics/input/cm.txt')
filename = os.path.join(fileDir, './Github/donation-analytics/insight_testsuite/tests/test_1/input/itcont3.txt')
filename = os.path.abspath(os.path.realpath(filename))
filename_p = os.path.join(fileDir, './Github/donation-analytics/insight_testsuite/tests/test_1/input/percentile.txt')
filename_p = os.path.abspath(os.path.realpath(filename_p))
# print filename

percentile = readPercentile(filename_p)

readFile(filename)
infoParse(filename)

testList = [384,250,230,384,333,384]

percentileCalculator(percentile,len(testList),testList)

# duplicateCounter(duplicate_donations)

repeatDonors(duplicate_donations)

# i = 0
# while i < len(duplicate_donations):
#     print duplicate_donor_transaction_amt[i]
#     i += 1
