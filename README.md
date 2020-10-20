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
The next steps are:
- To create variables MME_PURDUE, MME_INDUSTRY, DOSAGE_PURDUE, DOSAGE_INDUSTRY, VOLUME_PURDUE, VOLUME_INDUSTRY
- Insert FIP codes ("AK090") in specific format necessitated by eventual project data merging into another government DF, (http://www.naarep.com/agentsite/training/templates/FIPS.pdf) 
