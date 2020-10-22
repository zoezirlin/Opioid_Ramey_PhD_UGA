#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:37:44 2020

@author: zoezirlin
"""


#PACKAGES
import pandas as pd
import numpy as np

# DATASET OUTLINE
#   BUYER_COUNTY    FIPS        MONTHYEAR       YEAR        STATE       MME_PURDUE      MME_INDUSTRY    DOSAGE_PURDUE   DOSAGE_INDUSTRY     VOLUME_PURDUE       VOLUME_INDUSTRY


#to do
#   - convert dates back into numbers


                            #ALABAMA

###############################################################################
# STEP 1: importing the alabama CSV

al_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-al-statewide-itemized.csv')

variables_full_head = al_full.head()
###############################################################################




###############################################################################
# STEP 2: creating malleable df to cut down

al = al_full.copy()
###############################################################################




###############################################################################
# STEP 3: creating df with only preferred covariates

al = al[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
###############################################################################




###############################################################################
# STEP 4: creating dosage unit variable through direct calculation

al['Volume'] = al['DOSAGE_UNIT']*al['dos_str']
###############################################################################




###############################################################################
# STEP 5: splitting dates into day, month and year

# https://stackoverflow.com/questions/39217347/how-to-split-number-to-separate-columns-in-pandas-dataframe

# Making string version of original column, call it 'col'
al['col'] = al['TRANSACTION_DATE'].astype(str)

# https://towardsdatascience.com/the-basics-of-indexing-and-slicing-python-lists-2d12c90a94cf

al['YEAR'] = al['col'].str[-4:]
al['DAY_MONTH'] = al['col'].str[:-4]

al['DAY'] = al['DAY_MONTH'].str[-2:]
al['MONTH'] = al['DAY_MONTH'].str[:-2]

al.drop('col', axis=1, inplace=True)
al.drop('DAY_MONTH', axis=1, inplace=True)
al.drop('TRANSACTION_DATE', axis=1, inplace=True)

###############################################################################




###############################################################################
# STEP 6: splitting dates into monthyear

# Insert an "m" in front of each "MONTH" variable in new variable "M_X"
al['M_X'] = ('m' + al['MONTH'])


# Merge "YEAR" and "MONTH" into one variable: MONTH_YEAR
al['MONTH_YEAR'] = al['YEAR'] + al['M_X']
###############################################################################



###############################################################################
# STEP 8: Getting the FIPS codes

# Importing FIPS excel sheet, using converter to keep leadinig zero's
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})

# Creating the FIP code layout necessitated by research requirments
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']

# Making county names upper case to be able to match to master dataframe
fip['County Name'] = fip['County Name'].str.upper()

# Dropping unnecessary variables
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)

# Renaming variable to match other dataframe
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})

# Creating new joined dataframe "x" before we fold data into pivot table
x = pd.merge(al, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')

###############################################################################




###############################################################################
# STEP 9: creating dataframe with MME_PURDUE, MME_INDUSTRY, etc. 

al_p = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)

alabama_final = pd.DataFrame(al_p.to_records())

alabama_final.fillna(0)

###############################################################################




###############################################################################
# STEP 10: finalizing the variable names and exporting to CSV

for col in alabama_final.columns: 
    print(col)
    

alabama_final.columns =['Month_Year', 
                                        'County',
                                        'Year',
                                        'Month',
                                        'State',
                                        'FIPS_Code',
                                        'Dosage_Industry',
                                        'Dosage_Purdue',
                                        'MME_Industry',
                                        'MME_Purdue',
                                        'Volume_Industry',
                                        'Volume_Purdue'
                                        ]

alabama_final.to_csv(r'/Volumes/ZOE ZIRLIN/alabama_expanded.csv')    
###############################################################################

