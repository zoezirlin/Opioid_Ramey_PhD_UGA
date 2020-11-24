
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 21:31:52 2020

@author: dinazirlin
"""


"""STEP 1

importing packages and API

"""
#########################
#importing packages
import pandas as pd
import numpy as np
import arcospy
#########################





"""STEP 2

importing raw state CSV file

"""
#########################
#specifying which variable I want imported from the raw CSV file
fields = ['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','dos_str','MME_Conversion_Factor']

#reading in raw state CSV file
df = pd.read_csv(r'/Users/zoezirlin/Desktop/arcos-al-statewide-itemized.csv',usecols=fields)

#creating malleable copy
df = df.copy()
##########################





"""STEP 3

transforming variables and creating new variables for requested data

"""
##########################
#creating volume variable
df['Volume'] = df['DOSAGE_UNIT']*df['dos_str']

#creating MME variable
df['MME'] = df['DOSAGE_UNIT']*df['dos_str']*df['MME_Conversion_Factor']

#creating data formatting for eventual integration into CDC
df['col'] = df['TRANSACTION_DATE'].astype(str)
df['YEAR'] = df['col'].str[-4:]
df['DAY_MONTH'] = df['col'].str[:-4]
df['DAY'] = df['DAY_MONTH'].str[-2:]
df['MONTH'] = df['DAY_MONTH'].str[:-2]
df.drop('col', axis=1, inplace=True)
df.drop('DAY_MONTH', axis=1, inplace=True)
df.drop('TRANSACTION_DATE', axis=1, inplace=True)
df['M_X'] = ('m' + df['MONTH'])
df['MONTH_YEAR'] = df['YEAR'] + df['M_X']

#creating binary purdue or industry option in new variable titled "PURDUE_VS_INDUSTRY"
df['PURDUE_VS_INDUSTRY'] = np.where(df['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')

#dropping unnecessary variables
df.drop('DAY', axis=1, inplace=True)
df.drop('MONTH', axis=1, inplace=True)
df.drop('M_X', axis=1, inplace=True)
df.drop('MME_Conversion_Factor', axis=1, inplace=True)
##########################





"""STEP 4

importing API data for fip codes and population

"""
##########################
#import fips and state populations
county_pop = arcospy.county_population(state="AL", key="WaPo")
county_pop.head()

#delete first two numbers in the countyfips to make room for the state
county_pop['countyfips'] = county_pop['countyfips'].str[2:]

#replace first two digits in country fips with buyer state
county_pop['FIP_CODE'] = county_pop['BUYER_STATE'] + county_pop['countyfips'] 

#dropping unnecessary variables from countypop before merge with state CSV
county_pop.drop('STATE', axis=1, inplace=True)
county_pop.drop('COUNTY', axis=1, inplace=True)
county_pop.drop('county_name', axis=1, inplace=True)
county_pop.drop('variable', axis=1, inplace=True)
county_pop.drop('NAME', axis=1, inplace=True)
county_pop.drop('countyfips', axis=1, inplace=True)
##########################





"""STEP 5

merging the two dataframes together on BUYER_COUNTY
gaining fipcode and population into state csv

"""
##########################
#merging raw state CSV with fip code API file through BUYER_COUNTY and BUYER_STATE
x = pd.merge(df, county_pop, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')

#creating aggregated files for final merges into 50 state csv files
alabama_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
alabama_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)

#creating dataframes for above aggregated files
data1_A = pd.DataFrame(alabama_A.to_records())
data1_B = pd.DataFrame(alabama_B.to_records())
##########################





"""STEP 6

adding populations into aggregated dataframes

"""
##########################
#transforming API data types to strings
county_pop = county_pop.rename(columns={'year':'YEAR'})
county_pop['YEAR'] = county_pop['YEAR'].astype(str)
county_pop['population'] = county_pop['population'].astype(str)

#taking a chunk of the API data for the merge below
county_merge = county_pop[['FIP_CODE','population','YEAR']]

#merging aggregated file 
a = data1_A.merge(county_merge, on=['FIP_CODE','YEAR'])
b = data1_B.merge(county_merge, on=['FIP_CODE','YEAR'])

#filling dataframes NA's with 0's
a.fillna(0)
b.fillna(0)

#exporting these files to CSV's on computer for manual validity checks
a.to_csv('/Users/zoezirlin/Desktop/Book1.csv')
b.to_csv('/Users/zoezirlin/Desktop/Book2.csv')












#renaming columns for dataframe a
#a.columns =['Population',
                                        'Month_Year', 
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