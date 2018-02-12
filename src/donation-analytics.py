
import os

def readFile(filename):
    filehandle = open(filename)
    for l in filehandle:
        row = l.strip().split("|")
        # print "CMTE_ID: " + row[0] + "\nNAME: " + row[7] +"\nZIP_CODE: " + row[10] +"\nTRANSACTION_DT: " + row[13] +"\nTRANSACTION_AMT: " + row[14] +"\nOTHER_ID: " + row[15] + "\n-----------------------------------\n"
    # print filehandle.read()
    filehandle.close()


def infoParse(filename):
    filehandle = open(filename)
    for l in filehandle:
        record = l.strip().split("|")

        if check_transaction_date(record) and check_zip_code(record) and check_name(record) and check_CMTE_ID(record) and check_transaction_amt(record) and check_otherID(record): #runs through each check to make sure current line data is valid

            current_cmte_id = record[0]
            current_name = record[7]
            current_zip_code = record[10][:5] #only first 5 digits of zip code are used
            current_transaction_date = record[13]
            current_transaction_amt = record[14]

            # Before appending the record to the NAME list, this loop checks to see if there is already a record with the same name in the master NAME list.
            # If so, it will add that record to a separate list of duplicates

            for i in NAME_LIST:
                if i == current_name:
                    print "\n--------------------DUPLICATE-----------------------\n"
                    print "Index: " + str(NAME_LIST.index(current_name)) + " - " + str(current_name)
                    print "Current Dupe: " + str(len(NAME_LIST))

                    orig_record = NAME_LIST.index(current_name)
                    dupe_record = len(NAME_LIST)


                    duplicate_donor_name.append(current_name)
                    dupl

                    print "Names Array: " + str(NAME_LIST)
                    print "Duplicate Name Array: " + str(duplicate_donor_name)

                    print "Original Record: " + str(CMTE_ID_LIST[orig_record]) + " " + str(NAME_LIST[orig_record])
                    print "Duplicate Record: " + str(CMTE_ID_LIST[dupe_record]) + " " + str(duplicate_donor_name[dupe_record])


            #Here, each valid record is entered into separate lists based on data type
            CMTE_ID_LIST.append(current_cmte_id)
            NAME_LIST.append(current_name)
            ZIP_CODE_LIST.append(current_zip_code)
            TRANSACTION_DT_LIST.append(current_transaction_date)
            TRANSCTION_AMT_LIST.append(current_transaction_amt)

            # print "\n\nCMTE_ID: " + record[0] + "\nNAME: " + record[7] +"\nZIP_CODE: " + record[10] +"\nTRANSACTION_DT: " + record[13] +"\nTRANSACTION_AMT: " + record[14] +"\nOTHER_ID: " + record[15] + "\n-----------------------------------\n"


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


CMTE_ID_LIST = []
NAME_LIST = []
ZIP_CODE_LIST = []
TRANSACTION_DT_LIST = []
TRANSCTION_AMT_LIST = []
OTHER_ID_LIST = []

duplicate_donations = []
duplicate_donor_cmte_ID =
duplicate_donor_name = []
duplicate_donor_zipCode = []
duplicate_donor_transaction_dt = []


#For accessing the txt file
fileDir = os.path.dirname(os.path.realpath('__file__'))
# print fileDir

# filename = os.path.join(fileDir, './Github/donation-analytics/input/cm.txt')
filename = os.path.join(fileDir, './Github/donation-analytics/insight_testsuite/tests/test_1/input/itcont.txt')
filename = os.path.abspath(os.path.realpath(filename))
# print filename
readFile(filename)
infoParse(filename)
