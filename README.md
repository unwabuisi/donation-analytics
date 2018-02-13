# Table of Contents
1. [Introduction](README.md#introduction)
2. [Input Data](README.md#input-data)
3. [Step One](README.md#step-one)
4. [Step Two](README.md#step-two)
5. [Step Three](README.md#step-three)
6. [Output Data](README.md#output-data)
7. [Writing clean, scalable and well-tested code](README.md#writing-clean-scalable-and-well-tested-code)
8. [Repo directory structure](README.md#repo-directory-structure)
9. [Testing](README.md#testing)


# Introduction
This was a Coding Challenge I participated in for the [Insight Data Engineering Program](http://xyz.insightdatascience.com/Insight_Data_Engineering_White_Paper.pdf).
Here is the description:
>You’re a data engineer working for political consultants whose clients are cash-strapped political candidates. They've asked for help analyzing loyalty trends in campaign contributions, namely identifying areas of repeat donors and calculating how much they're spending.
The Federal Election Commission regularly publishes campaign contributions, and while you don’t want to pull specific donors from those files — because using that information for fundraising or commercial purposes is illegal — you want to identify areas (zip codes) that could be sources of repeat campaign contributions.

I completed the challenge in about 2 days (after uselessly procrastinating the other 4). It was extremely difficult at times, and deceptively simple during others but I really enjoyed the challenge of writing a program with a plausible real world application! Below are some details, and a general breakdown of how I did it.


# Input Data
The [first file](input/itcont.txt) given was a log of all donors and their contributions, etc. Each record contained:
* `CMTE_ID`: identifies the flier, which for our purposes is the recipient of this contribution
* `NAME`: name of the donor
* `ZIP_CODE`:  zip code of the contributor (we only want the first five digits/characters)
* `TRANSACTION_DT`: date of the transaction
* `TRANSACTION_AMT`: amount of the transaction
* `OTHER_ID`: a field that denotes whether contribution came from a person or an entity

Along with a bunch of other data like Name (LAST, FIRST), Employer, Occupation, and a bunch of other things we can ignore. All the data conformed to the style of the [FEC Data Dictionary](https://classic.fec.gov/finance/disclosure/metadata/DataDictionaryContributionsbyIndividuals.shtml). You can also download a sample data set to play with [here](https://classic.fec.gov/finance/disclosure/metadata/DataDictionaryContributionsbyIndividuals.shtml) **NOTE: Only the sets labeled 'Contributions By Individuals' will work with this program.**

Along with the data set, there is [another file](/input/percentile.txt) which contains a number value used to calculate a percentile.

# Step One
The first thing I wanted to do was get rid of all of the data I did not need. I created a function that parsed the text file line-by-line and put all of the info I wanted into a list. Within this function, I also checked to see whether each record was a duplicate or not. The criteria for a duplicate donor was:
>if a donor had previously contributed to any recipient listed in the [`itcont.txt`](input/itcont.txt) file in any prior calendar year, that donor is considered a repeat donor. Also, for the purposes of this challenge, you can assume two contributions are from the same donor if the names and zip codes are identical.

Each duplicate was put into a separate list, as well as having each specific identifier (name, zip code, transaction date, etc.) put into a list in the same order.


# Step Two
I created a function to calculate the percentile using the [nearest-rank method](https://en.wikipedia.org/wiki/Percentile#The_nearest-rank_method). Creating the function to calculate the value was simply, but the challenge was understanding why it nearest-rank method worked and how I would implement it.


# Step Three
With all of the appropriate data split up into a bunch of lists, I iterated through the duplicates list to find the records where donors in the same zip codes contributed to the same campaign more than once. This was the most challenging part of the problem. How could I compare the values in a list to other values in that same list, all while matching so many different conditions? After a few failed attempts, I re-stumbled on the idea of using Python's dictionary data structure to keep track of the two more important things **Zip Code** and **How many donations came from each zip code**.

Iterating through the list, I kept a key value pair {ZipCode : numberOfDonors} and for zipcodes that had already been parsed, I simply incremented the number of donors.

## Output Data
This part was fairly simple, as most of the heavy lifting was already done. The final output will look something like this:
> **CMTE_ID|ZIP_CODE|CALENDAR YEAR OF DONATION(YYYY)|PERCENTILE|TOTAL AMOUNT OF $ CONTRIBUTED FROM ZIP_CODE|# OF DUPLICATE DONORS**
ex: C00176214|98371|2017|30|280|28

## Testing

Python was the first programming language I learned and has been the one I feel most comfortable in. I tested the program with a few different data sets (up to 1.3GB) and for the most part it ran well. I did my best to keep the code clean and easy to understand, but there are a few things I should mention if you plan on running this on your machine.

1. I had some trouble getting the file paths correct on my machine. Under the #FILE ACCESS & VARIABLES section, uncommenting the second #fileDir line and replacing the string with the correct path on your machine will probably fix whatever errors you're getting.

2. There are a bunch of commented out 'print' statements all over each function. These were just to help me debug and can be used to display more info on the data.

Insight also provided some tests and the instructions on how to use them are below:
>To make sure that your code has the correct directory structure and the format of the output files are correct, we have included a test script called `run_tests.sh` in the `insight_testsuite` folder.
The tests are stored simply as text files under the `insight_testsuite/tests` folder. Each test should have a separate folder with an `input` folder for `percentile.txt` and `itcont.txt` and an `output` folder for `repeat_donors.txt`.
You can run the test with the following command from within the `insight_testsuite` folder:
    insight_testsuite~$ ./run_tests.sh
On a failed test, the output of `run_tests.sh` should look like:
    [FAIL]: test_1
    [Thu Mar 30 16:28:01 PDT 2017] 0 of 1 tests passed
On success:
    [PASS]: test_1
    [Thu Mar 30 16:25:57 PDT 2017] 1 of 1 tests passed
One test has been provided as a way to check your formatting and simulate how we will be running tests when you submit your solution. We urge you to write your own additional tests. `test_1` is only intended to alert you if the directory structure or the output for this test is incorrect.

For more info you can contact me at [unwabuisi@utexas.edu](mailto:unwabuisi@utexas.edu)
