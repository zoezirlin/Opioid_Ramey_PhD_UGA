# Opioid_Ramey_PhD_UGA
PhD research data management repository for Rachel Ramey, Doctoral Student at University of Georgia Department of Marketing, measuring the impact of marketing pharmaceuticals on the American opioid epidemic. Current data programming conducted by Zoe Zirlin (UGA MMR).

https://www.terry.uga.edu/directory/marketing/rachel-ramey.html

## Updates as of October 19th: programming steps so far
Zoe Zirlin, Oct. 20 2020

#### Step 1
Importing the state CSV file, downloaded from https://www.washingtonpost.com/graphics/2019/investigations/dea-pain-pill-database/. 
Will run each state's CSV file through the following code, and then concatenate into one dataframe for further use in Stata.


#### Step 2
Creating a malleable copy of that dataframe for programming.


#### Step 3
Creating dataframe from master state CSV file to include only:
BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str'


#### Step 4
Creaing the "DOSAGE_UNIT" variable column, which is an obervation's dosage unit multiplied by its dosage strength.
al['DOSAGE_UNIT']*al['dos_str']


#### Step 5
Splitting the dates (formatted like "7032006" or "12132006" into three three variables: MONTH, YEAR, DAY.


#### Step 6
Creating new variable "MONTH_YEAR" to be formatted as "2006m3" if, for example, an obervation was made in 2006, month 3 (March of 2006.)


#### Step 7
Creating a new column labeling the binary option of PURDUE or INDUSTRY, to segment the observations into two possible categories: Purdue pharmaceutical company or non-purdue pharma.


#### Step 8
Importing the FIPS codes to be merged into state dataframe


#### Step 9.A
Creating the final state dataframe A by aggregating data into pivot table (with either purdue or industry exploded into their own 3 variables)

#### Step 9.B
Creating the final state dataframe B by aggregating data into pivot table (with all of the pharma companies exploded into their own 3 variables)



#### Step 10
Finalizing the variable/column names and exporting into the state's own CSV file 😊


#### Step 11
Once each state has its own CSV file, concatenate all 50 files one on top of the other for final set
