#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:15:09 2020

@author: zoezirlin
"""
import pandas as pd
import numpy as np






#AL/1
alabama_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-al-statewide-itemized.csv')
variables_full_head = alabama_full.head()
alabama = alabama_full.copy()
alabama = alabama[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
alabama['Volume'] = alabama['DOSAGE_UNIT']*alabama['dos_str']
alabama['col'] = alabama['TRANSACTION_DATE'].astype(str)
alabama['YEAR'] = alabama['col'].str[-4:]
alabama['DAY_MONTH'] = alabama['col'].str[:-4]
alabama['DAY'] = alabama['DAY_MONTH'].str[-2:]
alabama['MONTH'] = alabama['DAY_MONTH'].str[:-2]
alabama.drop('col', axis=1, inplace=True)
alabama.drop('DAY_MONTH', axis=1, inplace=True)
alabama.drop('TRANSACTION_DATE', axis=1, inplace=True)
alabama['M_X'] = ('m' + alabama['MONTH'])
alabama['MONTH_YEAR'] = alabama['YEAR'] + alabama['M_X']
alabama['PURDUE_VS_INDUSTRY'] = np.where(alabama['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(alabama, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
alabama_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
alabama_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data1_A = pd.DataFrame(alabama_A.to_records())
data1_B = pd.DataFrame(alabama_B.to_records())
data1_A.fillna(0)
data1_B.fillna(0)
for col in data1_A.columns: 
    print(col)
data1_A.columns =['Month_Year', 
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



#AK/2 
alaska_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-ak-statewide-itemized.csv')
variables_full_head = alaska_full.head()
alaska = alaska_full.copy()
alaska = alaska[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
alaska['Volume'] = alaska['DOSAGE_UNIT']*alaska['dos_str']
alaska['col'] = alaska['TRANSACTION_DATE'].astype(str)
alaska['YEAR'] = alaska['col'].str[-4:]
alaska['DAY_MONTH'] = alaska['col'].str[:-4]
alaska['DAY'] = alaska['DAY_MONTH'].str[-2:]
alaska['MONTH'] = alaska['DAY_MONTH'].str[:-2]
alaska.drop('col', axis=1, inplace=True)
alaska.drop('DAY_MONTH', axis=1, inplace=True)
alaska.drop('TRANSACTION_DATE', axis=1, inplace=True)
alaska['M_X'] = ('m' + alaska['MONTH'])
alaska['MONTH_YEAR'] = alaska['YEAR'] + alaska['M_X']
alaska['PURDUE_VS_INDUSTRY'] = np.where(alaska['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(alaska, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
alaska_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
alaska_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data2_A = pd.DataFrame(alaska_A.to_records())
data2_B = pd.DataFrame(alaska_B.to_records())
data2_A.fillna(0)
data2_B.fillna(0)
for col in data2_A.columns: 
    print(col)
data2_A.columns =['Month_Year', 
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





# AZ/3
arizona_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-az-statewide-itemized.csv')
variables_full_head = arizona_full.head()
arizona = arizona_full.copy()
arizona = arizona[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
arizona['Volume'] = arizona['DOSAGE_UNIT']*arizona['dos_str']
arizona['col'] = arizona['TRANSACTION_DATE'].astype(str)
arizona['YEAR'] = arizona['col'].str[-4:]
arizona['DAY_MONTH'] = arizona['col'].str[:-4]
arizona['DAY'] = arizona['DAY_MONTH'].str[-2:]
arizona['MONTH'] = arizona['DAY_MONTH'].str[:-2]
arizona.drop('col', axis=1, inplace=True)
arizona.drop('DAY_MONTH', axis=1, inplace=True)
arizona.drop('TRANSACTION_DATE', axis=1, inplace=True)
arizona['M_X'] = ('m' + arizona['MONTH'])
arizona['MONTH_YEAR'] = arizona['YEAR'] + arizona['M_X']
arizona['PURDUE_VS_INDUSTRY'] = np.where(arizona['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(arizona, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
arizona_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
arizona_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data3_A = pd.DataFrame(arizona_A.to_records())
data3_B = pd.DataFrame(arizona_B.to_records())
data3_A.fillna(0)
data3_B.fillna(0)
for col in data3_A.columns: 
    print(col)
data3_A.columns =['Month_Year', 
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



# AR/4
arkansas_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-ar-statewide-itemized.csv')
variables_full_head = arkansas_full.head()
arkansas = arkansas_full.copy()
arkansas = arkansas[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
arkansas['Volume'] = arkansas['DOSAGE_UNIT']*arkansas['dos_str']
arkansas['col'] = arkansas['TRANSACTION_DATE'].astype(str)
arkansas['YEAR'] = arkansas['col'].str[-4:]
arkansas['DAY_MONTH'] = arkansas['col'].str[:-4]
arkansas['DAY'] = arkansas['DAY_MONTH'].str[-2:]
arkansas['MONTH'] = arkansas['DAY_MONTH'].str[:-2]
arkansas.drop('col', axis=1, inplace=True)
arkansas.drop('DAY_MONTH', axis=1, inplace=True)
arkansas.drop('TRANSACTION_DATE', axis=1, inplace=True)
arkansas['M_X'] = ('m' + arkansas['MONTH'])
arkansas['MONTH_YEAR'] = arkansas['YEAR'] + arkansas['M_X']
arkansas['PURDUE_VS_INDUSTRY'] = np.where(arkansas['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(arkansas, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
arkansas_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
arkansas_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data4_A = pd.DataFrame(arkansas_A.to_records())
data4_B = pd.DataFrame(arkansas_B.to_records())
data4_A.fillna(0)
data4_B.fillna(0)
for col in data4_A.columns: 
    print(col)
data4_A.columns =['Month_Year', 
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



#CA/5
california_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-ca-statewide-itemized.csv')
variables_full_head = california_full.head()
california = california_full.copy()
california = california[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
california['Volume'] = california['DOSAGE_UNIT']*california['dos_str']
california['col'] = california['TRANSACTION_DATE'].astype(str)
california['YEAR'] = california['col'].str[-4:]
california['DAY_MONTH'] = california['col'].str[:-4]
california['DAY'] = california['DAY_MONTH'].str[-2:]
california['MONTH'] = california['DAY_MONTH'].str[:-2]
california.drop('col', axis=1, inplace=True)
california.drop('DAY_MONTH', axis=1, inplace=True)
california.drop('TRANSACTION_DATE', axis=1, inplace=True)
california['M_X'] = ('m' + california['MONTH'])
california['MONTH_YEAR'] = california['YEAR'] + california['M_X']
california['PURDUE_VS_INDUSTRY'] = np.where(california['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(california, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
california_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
california_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data5_A = pd.DataFrame(california_A.to_records())
data5_B = pd.DataFrame(california_B.to_records())
data5_A.fillna(0)
data5_B.fillna(0)
for col in data5_A.columns: 
    print(col)
data5_A.columns =['Month_Year', 
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



# CN/ 6
conneticut_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-cn-statewide-itemized.csv')
variables_full_head = conneticut_full.head()
conneticut = conneticut_full.copy()
conneticut = conneticut[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
conneticut['Volume'] = conneticut['DOSAGE_UNIT']*conneticut['dos_str']
conneticut['col'] = conneticut['TRANSACTION_DATE'].astype(str)
conneticut['YEAR'] = conneticut['col'].str[-4:]
conneticut['DAY_MONTH'] = conneticut['col'].str[:-4]
conneticut['DAY'] = conneticut['DAY_MONTH'].str[-2:]
conneticut['MONTH'] = conneticut['DAY_MONTH'].str[:-2]
conneticut.drop('col', axis=1, inplace=True)
conneticut.drop('DAY_MONTH', axis=1, inplace=True)
conneticut.drop('TRANSACTION_DATE', axis=1, inplace=True)
conneticut['M_X'] = ('m' + conneticut['MONTH'])
conneticut['MONTH_YEAR'] = conneticut['YEAR'] + conneticut['M_X']
conneticut['PURDUE_VS_INDUSTRY'] = np.where(conneticut['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(conneticut, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
conneticut_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
conneticut_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data6_A = pd.DataFrame(conneticut_A.to_records())
data6_B = pd.DataFrame(conneticut_B.to_records())
data6_A.fillna(0)
data6_B.fillna(0)
for col in data6_A.columns: 
    print(col)
data6_A.columns =['Month_Year', 
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

#DE/7
delaware_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-de-statewide-itemized.csv')
variables_full_head = delaware_full.head()
delaware = delaware_full.copy()
delaware = delaware[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
delaware['Volume'] = delaware['DOSAGE_UNIT']*delaware['dos_str']
delaware['col'] = delaware['TRANSACTION_DATE'].astype(str)
delaware['YEAR'] = delaware['col'].str[-4:]
delaware['DAY_MONTH'] = delaware['col'].str[:-4]
delaware['DAY'] = delaware['DAY_MONTH'].str[-2:]
delaware['MONTH'] = delaware['DAY_MONTH'].str[:-2]
delaware.drop('col', axis=1, inplace=True)
delaware.drop('DAY_MONTH', axis=1, inplace=True)
delaware.drop('TRANSACTION_DATE', axis=1, inplace=True)
delaware['M_X'] = ('m' + delaware['MONTH'])
delaware['MONTH_YEAR'] = delaware['YEAR'] + delaware['M_X']
delaware['PURDUE_VS_INDUSTRY'] = np.where(delaware['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(delaware, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
delaware_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
delaware_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data7_A = pd.DataFrame(delaware_A.to_records())
data7_B = pd.DataFrame(delaware_B.to_records())
data7_A.fillna(0)
data7_B.fillna(0)
for col in data7_A.columns: 
    print(col)
data7_A.columns =['Month_Year', 
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



#DC/ 8
washdc_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-dc-statewide-itemized.csv')
variables_full_head = washdc_full.head()
washdc = washdc_full.copy()
washdc = washdc[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
washdc['Volume'] = washdc['DOSAGE_UNIT']*washdc['dos_str']
washdc['col'] = washdc['TRANSACTION_DATE'].astype(str)
washdc['YEAR'] = washdc['col'].str[-4:]
washdc['DAY_MONTH'] = washdc['col'].str[:-4]
washdc['DAY'] = washdc['DAY_MONTH'].str[-2:]
washdc['MONTH'] = washdc['DAY_MONTH'].str[:-2]
washdc.drop('col', axis=1, inplace=True)
washdc.drop('DAY_MONTH', axis=1, inplace=True)
washdc.drop('TRANSACTION_DATE', axis=1, inplace=True)
washdc['M_X'] = ('m' + washdc['MONTH'])
washdc['MONTH_YEAR'] = washdc['YEAR'] + washdc['M_X']
washdc['PURDUE_VS_INDUSTRY'] = np.where(washdc['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(washdc, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
washdc_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
washdc_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data8_A = pd.DataFrame(washdc_A.to_records())
data8_B = pd.DataFrame(washdc_B.to_records())
data8_A.fillna(0)
data8_B.fillna(0)
for col in data8_A.columns: 
    print(col)
data8_A.columns =['Month_Year', 
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


#CO/9
colorado_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-co-statewide-itemized.csv')
variables_full_head = colorado_full.head()
colorado = colorado_full.copy()
colorado = colorado[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
colorado['Volume'] = colorado['DOSAGE_UNIT']*colorado['dos_str']
colorado['col'] = colorado['TRANSACTION_DATE'].astype(str)
colorado['YEAR'] = colorado['col'].str[-4:]
colorado['DAY_MONTH'] = colorado['col'].str[:-4]
colorado['DAY'] = colorado['DAY_MONTH'].str[-2:]
colorado['MONTH'] = colorado['DAY_MONTH'].str[:-2]
colorado.drop('col', axis=1, inplace=True)
colorado.drop('DAY_MONTH', axis=1, inplace=True)
colorado.drop('TRANSACTION_DATE', axis=1, inplace=True)
colorado['M_X'] = ('m' + colorado['MONTH'])
colorado['MONTH_YEAR'] = colorado['YEAR'] + colorado['M_X']
colorado['PURDUE_VS_INDUSTRY'] = np.where(colorado['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(colorado, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
colorado_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
colorado_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data9_A = pd.DataFrame(colorado_A.to_records())
data9_B = pd.DataFrame(colorado_B.to_records())
data9_A.fillna(0)
data9_B.fillna(0)
for col in data9_A.columns: 
    print(col)
data9_A.columns =['Month_Year', 
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



#FL/10
florida_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-fl-statewide-itemized.csv')
variables_full_head = florida_full.head()
florida = florida_full.copy()
florida = florida[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
florida['Volume'] = florida['DOSAGE_UNIT']*florida['dos_str']
florida['col'] = florida['TRANSACTION_DATE'].astype(str)
florida['YEAR'] = florida['col'].str[-4:]
florida['DAY_MONTH'] = florida['col'].str[:-4]
florida['DAY'] = florida['DAY_MONTH'].str[-2:]
florida['MONTH'] = florida['DAY_MONTH'].str[:-2]
florida.drop('col', axis=1, inplace=True)
florida.drop('DAY_MONTH', axis=1, inplace=True)
florida.drop('TRANSACTION_DATE', axis=1, inplace=True)
florida['M_X'] = ('m' + florida['MONTH'])
florida['MONTH_YEAR'] = florida['YEAR'] + florida['M_X']
florida['PURDUE_VS_INDUSTRY'] = np.where(florida['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(florida, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
florida_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
florida_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data10_A = pd.DataFrame(florida_A.to_records())
data10_B = pd.DataFrame(florida_B.to_records())
data10_A.fillna(0)
data10_B.fillna(0)
for col in data10_A.columns: 
    print(col)
data10_A.columns =['Month_Year', 
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



#GA/11
georgia_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-ga-statewide-itemized.csv')
variables_full_head = georgia_full.head()
georgia = georgia_full.copy()
georgia = georgia[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
georgia['Volume'] = georgia['DOSAGE_UNIT']*georgia['dos_str']
georgia['col'] = georgia['TRANSACTION_DATE'].astype(str)
georgia['YEAR'] = georgia['col'].str[-4:]
georgia['DAY_MONTH'] = georgia['col'].str[:-4]
georgia['DAY'] = georgia['DAY_MONTH'].str[-2:]
georgia['MONTH'] = georgia['DAY_MONTH'].str[:-2]
georgia.drop('col', axis=1, inplace=True)
georgia.drop('DAY_MONTH', axis=1, inplace=True)
georgia.drop('TRANSACTION_DATE', axis=1, inplace=True)
georgia['M_X'] = ('m' + georgia['MONTH'])
georgia['MONTH_YEAR'] = georgia['YEAR'] + georgia['M_X']
georgia['PURDUE_VS_INDUSTRY'] = np.where(georgia['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(georgia, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
georgia_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
georgia_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data11_A = pd.DataFrame(georgia_A.to_records())
data11_B = pd.DataFrame(georgia_B.to_records())
data11_A.fillna(0)
data11_B.fillna(0)
for col in data11_A.columns: 
    print(col)
data11_A.columns =['Month_Year', 
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



#HI/12
hawaii_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-hi-statewide-itemized.csv')
variables_full_head = hawaii_full.head()
hawaii = hawaii_full.copy()
hawaii = hawaii[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
hawaii['Volume'] = hawaii['DOSAGE_UNIT']*hawaii['dos_str']
hawaii['col'] = hawaii['TRANSACTION_DATE'].astype(str)
hawaii['YEAR'] = hawaii['col'].str[-4:]
hawaii['DAY_MONTH'] = hawaii['col'].str[:-4]
hawaii['DAY'] = hawaii['DAY_MONTH'].str[-2:]
hawaii['MONTH'] = hawaii['DAY_MONTH'].str[:-2]
hawaii.drop('col', axis=1, inplace=True)
hawaii.drop('DAY_MONTH', axis=1, inplace=True)
hawaii.drop('TRANSACTION_DATE', axis=1, inplace=True)
hawaii['M_X'] = ('m' + hawaii['MONTH'])
hawaii['MONTH_YEAR'] = hawaii['YEAR'] + hawaii['M_X']
hawaii['PURDUE_VS_INDUSTRY'] = np.where(hawaii['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(hawaii, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
hawaii_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
hawaii_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data12_A = pd.DataFrame(hawaii_A.to_records())
data12_B = pd.DataFrame(hawaii_B.to_records())
data12_A.fillna(0)
data12_B.fillna(0)
for col in data12_A.columns: 
    print(col)
data12_A.columns =['Month_Year', 
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




#ID/13
idaho_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-id-statewide-itemized.csv')
variables_full_head = idaho_full.head()
idaho = idaho_full.copy()
idaho = idaho[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
idaho['Volume'] = idaho['DOSAGE_UNIT']*idaho['dos_str']
idaho['col'] = idaho['TRANSACTION_DATE'].astype(str)
idaho['YEAR'] = idaho['col'].str[-4:]
idaho['DAY_MONTH'] = idaho['col'].str[:-4]
idaho['DAY'] = idaho['DAY_MONTH'].str[-2:]
idaho['MONTH'] = idaho['DAY_MONTH'].str[:-2]
idaho.drop('col', axis=1, inplace=True)
idaho.drop('DAY_MONTH', axis=1, inplace=True)
idaho.drop('TRANSACTION_DATE', axis=1, inplace=True)
idaho['M_X'] = ('m' + idaho['MONTH'])
idaho['MONTH_YEAR'] = idaho['YEAR'] + idaho['M_X']
idaho['PURDUE_VS_INDUSTRY'] = np.where(idaho['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(idaho, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
idaho_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
idaho_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data13_A = pd.DataFrame(idaho_A.to_records())
data13_B = pd.DataFrame(idaho_B.to_records())
data13_A.fillna(0)
data13_B.fillna(0)
for col in data13_A.columns: 
    print(col)
data13_A.columns =['Month_Year', 
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



#IL/14
illinois_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-il-statewide-itemized.csv')
variables_full_head = illinois_full.head()
illinois = illinois_full.copy()
illinois = illinois[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
illinois['Volume'] = illinois['DOSAGE_UNIT']*illinois['dos_str']
illinois['col'] = illinois['TRANSACTION_DATE'].astype(str)
illinois['YEAR'] = illinois['col'].str[-4:]
illinois['DAY_MONTH'] = illinois['col'].str[:-4]
illinois['DAY'] = illinois['DAY_MONTH'].str[-2:]
illinois['MONTH'] = illinois['DAY_MONTH'].str[:-2]
illinois.drop('col', axis=1, inplace=True)
illinois.drop('DAY_MONTH', axis=1, inplace=True)
illinois.drop('TRANSACTION_DATE', axis=1, inplace=True)
illinois['M_X'] = ('m' + illinois['MONTH'])
illinois['MONTH_YEAR'] = illinois['YEAR'] + illinois['M_X']
illinois['PURDUE_VS_INDUSTRY'] = np.where(illinois['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(illinois, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
illinois_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
illinois_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data14_A = pd.DataFrame(illinois_A.to_records())
data14_B = pd.DataFrame(illinois_B.to_records())
data14_A.fillna(0)
data14_B.fillna(0)
for col in data14_A.columns: 
    print(col)
data14_A.columns =['Month_Year', 
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



#IN/15
indiana_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-in-statewide-itemized.csv')
variables_full_head = indiana_full.head()
indiana = indiana_full.copy()
indiana = indiana[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
indiana['Volume'] = indiana['DOSAGE_UNIT']*indiana['dos_str']
indiana['col'] = indiana['TRANSACTION_DATE'].astype(str)
indiana['YEAR'] = indiana['col'].str[-4:]
indiana['DAY_MONTH'] = indiana['col'].str[:-4]
indiana['DAY'] = indiana['DAY_MONTH'].str[-2:]
indiana['MONTH'] = indiana['DAY_MONTH'].str[:-2]
indiana.drop('col', axis=1, inplace=True)
indiana.drop('DAY_MONTH', axis=1, inplace=True)
indiana.drop('TRANSACTION_DATE', axis=1, inplace=True)
indiana['M_X'] = ('m' + indiana['MONTH'])
indiana['MONTH_YEAR'] = indiana['YEAR'] + indiana['M_X']
indiana['PURDUE_VS_INDUSTRY'] = np.where(indiana['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(indiana, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
indiana_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
indiana_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data15_A = pd.DataFrame(indiana_A.to_records())
data15_B = pd.DataFrame(indiana_B.to_records())
data15_A.fillna(0)
data15_B.fillna(0)
for col in data15_A.columns: 
    print(col)
data15_A.columns =['Month_Year', 
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



#IA/16
iowa_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-ia-statewide-itemized.csv')
variables_full_head = iowa_full.head()
iowa = iowa_full.copy()
iowa = iowa[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
iowa['Volume'] = iowa['DOSAGE_UNIT']*iowa['dos_str']
iowa['col'] = iowa['TRANSACTION_DATE'].astype(str)
iowa['YEAR'] = iowa['col'].str[-4:]
iowa['DAY_MONTH'] = iowa['col'].str[:-4]
iowa['DAY'] = iowa['DAY_MONTH'].str[-2:]
iowa['MONTH'] = iowa['DAY_MONTH'].str[:-2]
iowa.drop('col', axis=1, inplace=True)
iowa.drop('DAY_MONTH', axis=1, inplace=True)
iowa.drop('TRANSACTION_DATE', axis=1, inplace=True)
iowa['M_X'] = ('m' + iowa['MONTH'])
iowa['MONTH_YEAR'] = iowa['YEAR'] + iowa['M_X']
iowa['PURDUE_VS_INDUSTRY'] = np.where(iowa['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(iowa, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
iowa_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
iowa_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data16_A = pd.DataFrame(iowa_A.to_records())
data16_B = pd.DataFrame(iowa_B.to_records())
data16_A.fillna(0)
data16_B.fillna(0)
for col in data16_A.columns: 
    print(col)
data16_A.columns =['Month_Year', 
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



#KS/17
kansas_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-ks-statewide-itemized.csv')
variables_full_head = kansas_full.head()
kansas = kansas_full.copy()
kansas = kansas[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
kansas['Volume'] = kansas['DOSAGE_UNIT']*kansas['dos_str']
kansas['col'] = kansas['TRANSACTION_DATE'].astype(str)
kansas['YEAR'] = kansas['col'].str[-4:]
kansas['DAY_MONTH'] = kansas['col'].str[:-4]
kansas['DAY'] = kansas['DAY_MONTH'].str[-2:]
kansas['MONTH'] = kansas['DAY_MONTH'].str[:-2]
kansas.drop('col', axis=1, inplace=True)
kansas.drop('DAY_MONTH', axis=1, inplace=True)
kansas.drop('TRANSACTION_DATE', axis=1, inplace=True)
kansas['M_X'] = ('m' + kansas['MONTH'])
kansas['MONTH_YEAR'] = kansas['YEAR'] + kansas['M_X']
kansas['PURDUE_VS_INDUSTRY'] = np.where(kansas['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(kansas, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
kansas_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
kansas_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data17_A = pd.DataFrame(kansas_A.to_records())
data17_B = pd.DataFrame(kansas_B.to_records())
data17_A.fillna(0)
data17_B.fillna(0)
for col in data17_A.columns: 
    print(col)
data17_A.columns =['Month_Year', 
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



#KY/18
kentucky_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-ky-statewide-itemized.csv')
variables_full_head = kentucky_full.head()
kentucky = kentucky_full.copy()
kentucky = kentucky[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
kentucky['Volume'] = kentucky['DOSAGE_UNIT']*kentucky['dos_str']
kentucky['col'] = kentucky['TRANSACTION_DATE'].astype(str)
kentucky['YEAR'] = kentucky['col'].str[-4:]
kentucky['DAY_MONTH'] = kentucky['col'].str[:-4]
kentucky['DAY'] = kentucky['DAY_MONTH'].str[-2:]
kentucky['MONTH'] = kentucky['DAY_MONTH'].str[:-2]
kentucky.drop('col', axis=1, inplace=True)
kentucky.drop('DAY_MONTH', axis=1, inplace=True)
kentucky.drop('TRANSACTION_DATE', axis=1, inplace=True)
kentucky['M_X'] = ('m' + kentucky['MONTH'])
kentucky['MONTH_YEAR'] = kentucky['YEAR'] + kentucky['M_X']
kentucky['PURDUE_VS_INDUSTRY'] = np.where(kentucky['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(kentucky, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
kentucky_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
kentucky_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data18_A = pd.DataFrame(kentucky_A.to_records())
data18_B = pd.DataFrame(kentucky_B.to_records())
data18_A.fillna(0)
data18_B.fillna(0)
for col in data18_A.columns: 
    print(col)
data18_A.columns =['Month_Year', 
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



#LA/19
louisiana_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-la-statewide-itemized.csv')
variables_full_head = louisiana_full.head()
louisiana = louisiana_full.copy()
louisiana = louisiana[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
louisiana['Volume'] = louisiana['DOSAGE_UNIT']*louisiana['dos_str']
louisiana['col'] = louisiana['TRANSACTION_DATE'].astype(str)
louisiana['YEAR'] = louisiana['col'].str[-4:]
louisiana['DAY_MONTH'] = louisiana['col'].str[:-4]
louisiana['DAY'] = louisiana['DAY_MONTH'].str[-2:]
louisiana['MONTH'] = louisiana['DAY_MONTH'].str[:-2]
louisiana.drop('col', axis=1, inplace=True)
louisiana.drop('DAY_MONTH', axis=1, inplace=True)
louisiana.drop('TRANSACTION_DATE', axis=1, inplace=True)
louisiana['M_X'] = ('m' + louisiana['MONTH'])
louisiana['MONTH_YEAR'] = louisiana['YEAR'] + louisiana['M_X']
louisiana['PURDUE_VS_INDUSTRY'] = np.where(louisiana['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(louisiana, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
louisiana_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
louisiana_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data19_A = pd.DataFrame(louisiana_A.to_records())
data19_B = pd.DataFrame(louisiana_B.to_records())
data19_A.fillna(0)
data19_B.fillna(0)
for col in data19_A.columns: 
    print(col)
data19_A.columns =['Month_Year', 
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



#ME/20
maine_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-me-statewide-itemized.csv')
variables_full_head = maine_full.head()
maine = maine_full.copy()
maine = maine[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
maine['Volume'] = maine['DOSAGE_UNIT']*maine['dos_str']
maine['col'] = maine['TRANSACTION_DATE'].astype(str)
maine['YEAR'] = maine['col'].str[-4:]
maine['DAY_MONTH'] = maine['col'].str[:-4]
maine['DAY'] = maine['DAY_MONTH'].str[-2:]
maine['MONTH'] = maine['DAY_MONTH'].str[:-2]
maine.drop('col', axis=1, inplace=True)
maine.drop('DAY_MONTH', axis=1, inplace=True)
maine.drop('TRANSACTION_DATE', axis=1, inplace=True)
maine['M_X'] = ('m' + maine['MONTH'])
maine['MONTH_YEAR'] = maine['YEAR'] + maine['M_X']
maine['PURDUE_VS_INDUSTRY'] = np.where(maine['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(maine, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
maine_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
maine_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data20_A = pd.DataFrame(maine_A.to_records())
data20_B = pd.DataFrame(maine_B.to_records())
data20_A.fillna(0)
data20_B.fillna(0)
for col in data20_A.columns: 
    print(col)
data20_A.columns =['Month_Year', 
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



#MD/21
maryland_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-md-statewide-itemized.csv')
variables_full_head = maryland_full.head()
maryland = maryland_full.copy()
maryland = maryland[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
maryland['Volume'] = maryland['DOSAGE_UNIT']*maryland['dos_str']
maryland['col'] = maryland['TRANSACTION_DATE'].astype(str)
maryland['YEAR'] = maryland['col'].str[-4:]
maryland['DAY_MONTH'] = maryland['col'].str[:-4]
maryland['DAY'] = maryland['DAY_MONTH'].str[-2:]
maryland['MONTH'] = maryland['DAY_MONTH'].str[:-2]
maryland.drop('col', axis=1, inplace=True)
maryland.drop('DAY_MONTH', axis=1, inplace=True)
maryland.drop('TRANSACTION_DATE', axis=1, inplace=True)
maryland['M_X'] = ('m' + maryland['MONTH'])
maryland['MONTH_YEAR'] = maryland['YEAR'] + maryland['M_X']
maryland['PURDUE_VS_INDUSTRY'] = np.where(maryland['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(maryland, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
maryland_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
maryland_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data21_A = pd.DataFrame(maryland_A.to_records())
data21_B = pd.DataFrame(maryland_B.to_records())
data21_A.fillna(0)
data21_B.fillna(0)
for col in data21_A.columns: 
    print(col)
data21_A.columns =['Month_Year', 
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



#MA/22
massachusetts_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-ma-statewide-itemized.csv')
variables_full_head = massachusetts_full.head()
massachusetts = massachusetts_full.copy()
massachusetts = massachusetts[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
massachusetts['Volume'] = massachusetts['DOSAGE_UNIT']*massachusetts['dos_str']
massachusetts['col'] = massachusetts['TRANSACTION_DATE'].astype(str)
massachusetts['YEAR'] = massachusetts['col'].str[-4:]
massachusetts['DAY_MONTH'] = massachusetts['col'].str[:-4]
massachusetts['DAY'] = massachusetts['DAY_MONTH'].str[-2:]
massachusetts['MONTH'] = massachusetts['DAY_MONTH'].str[:-2]
massachusetts.drop('col', axis=1, inplace=True)
massachusetts.drop('DAY_MONTH', axis=1, inplace=True)
massachusetts.drop('TRANSACTION_DATE', axis=1, inplace=True)
massachusetts['M_X'] = ('m' + massachusetts['MONTH'])
massachusetts['MONTH_YEAR'] = massachusetts['YEAR'] + massachusetts['M_X']
massachusetts['PURDUE_VS_INDUSTRY'] = np.where(massachusetts['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(massachusetts, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
massachusetts_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
massachusetts_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data22_A = pd.DataFrame(massachusetts_A.to_records())
data22_B = pd.DataFrame(massachusetts_B.to_records())
data22_A.fillna(0)
data22_B.fillna(0)
for col in data22_A.columns: 
    print(col)
data22_A.columns =['Month_Year', 
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



#MI/23
michigan_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-mi-statewide-itemized.csv')
variables_full_head = michigan_full.head()
michigan = michigan_full.copy()
michigan = michigan[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
michigan['Volume'] = michigan['DOSAGE_UNIT']*michigan['dos_str']
michigan['col'] = michigan['TRANSACTION_DATE'].astype(str)
michigan['YEAR'] = michigan['col'].str[-4:]
michigan['DAY_MONTH'] = michigan['col'].str[:-4]
michigan['DAY'] = michigan['DAY_MONTH'].str[-2:]
michigan['MONTH'] = michigan['DAY_MONTH'].str[:-2]
michigan.drop('col', axis=1, inplace=True)
michigan.drop('DAY_MONTH', axis=1, inplace=True)
michigan.drop('TRANSACTION_DATE', axis=1, inplace=True)
michigan['M_X'] = ('m' + michigan['MONTH'])
michigan['MONTH_YEAR'] = michigan['YEAR'] + michigan['M_X']
michigan['PURDUE_VS_INDUSTRY'] = np.where(michigan['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(michigan, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
michigan_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
michigan_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data23_A = pd.DataFrame(michigan_A.to_records())
data23_B = pd.DataFrame(michigan_B.to_records())
data23_A.fillna(0)
data23_B.fillna(0)
for col in data23_A.columns: 
    print(col)
data23_A.columns =['Month_Year', 
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



#MN/24
minnesota_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-mn-statewide-itemized.csv')
variables_full_head = minnesota_full.head()
minnesota = minnesota_full.copy()
minnesota = minnesota[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
minnesota['Volume'] = minnesota['DOSAGE_UNIT']*minnesota['dos_str']
minnesota['col'] = minnesota['TRANSACTION_DATE'].astype(str)
minnesota['YEAR'] = minnesota['col'].str[-4:]
minnesota['DAY_MONTH'] = minnesota['col'].str[:-4]
minnesota['DAY'] = minnesota['DAY_MONTH'].str[-2:]
minnesota['MONTH'] = minnesota['DAY_MONTH'].str[:-2]
minnesota.drop('col', axis=1, inplace=True)
minnesota.drop('DAY_MONTH', axis=1, inplace=True)
minnesota.drop('TRANSACTION_DATE', axis=1, inplace=True)
minnesota['M_X'] = ('m' + minnesota['MONTH'])
minnesota['MONTH_YEAR'] = minnesota['YEAR'] + minnesota['M_X']
minnesota['PURDUE_VS_INDUSTRY'] = np.where(minnesota['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(minnesota, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
minnesota_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
minnesota_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data24_A = pd.DataFrame(minnesota_A.to_records())
data24_B = pd.DataFrame(minnesota_B.to_records())
data24_A.fillna(0)
data24_B.fillna(0)
for col in data24_A.columns: 
    print(col)
data24_A.columns =['Month_Year', 
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



#MS/25
mississippi_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-ms-statewide-itemized.csv')
variables_full_head = mississippi_full.head()
mississippi = mississippi_full.copy()
mississippi = mississippi[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
mississippi['Volume'] = mississippi['DOSAGE_UNIT']*mississippi['dos_str']
mississippi['col'] = mississippi['TRANSACTION_DATE'].astype(str)
mississippi['YEAR'] = mississippi['col'].str[-4:]
mississippi['DAY_MONTH'] = mississippi['col'].str[:-4]
mississippi['DAY'] = mississippi['DAY_MONTH'].str[-2:]
mississippi['MONTH'] = mississippi['DAY_MONTH'].str[:-2]
mississippi.drop('col', axis=1, inplace=True)
mississippi.drop('DAY_MONTH', axis=1, inplace=True)
mississippi.drop('TRANSACTION_DATE', axis=1, inplace=True)
mississippi['M_X'] = ('m' + mississippi['MONTH'])
mississippi['MONTH_YEAR'] = mississippi['YEAR'] + mississippi['M_X']
mississippi['PURDUE_VS_INDUSTRY'] = np.where(mississippi['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(mississippi, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
mississippi_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
mississippi_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data25_A = pd.DataFrame(mississippi_A.to_records())
data25_B = pd.DataFrame(mississippi_B.to_records())
data25_A.fillna(0)
data25_B.fillna(0)
for col in data25_A.columns: 
    print(col)
data25_A.columns =['Month_Year', 
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



#MO/26
missouri_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-mo-statewide-itemized.csv')
variables_full_head = missouri_full.head()
missouri = missouri_full.copy()
missouri = missouri[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
missouri['Volume'] = missouri['DOSAGE_UNIT']*missouri['dos_str']
missouri['col'] = missouri['TRANSACTION_DATE'].astype(str)
missouri['YEAR'] = missouri['col'].str[-4:]
missouri['DAY_MONTH'] = missouri['col'].str[:-4]
missouri['DAY'] = missouri['DAY_MONTH'].str[-2:]
missouri['MONTH'] = missouri['DAY_MONTH'].str[:-2]
missouri.drop('col', axis=1, inplace=True)
missouri.drop('DAY_MONTH', axis=1, inplace=True)
missouri.drop('TRANSACTION_DATE', axis=1, inplace=True)
missouri['M_X'] = ('m' + missouri['MONTH'])
missouri['MONTH_YEAR'] = missouri['YEAR'] + missouri['M_X']
missouri['PURDUE_VS_INDUSTRY'] = np.where(missouri['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(missouri, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
missouri_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
missouri_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data26_A = pd.DataFrame(missouri_A.to_records())
data26_B = pd.DataFrame(missouri_B.to_records())
data26_A.fillna(0)
data26_B.fillna(0)
for col in data26_A.columns: 
    print(col)
data26_A.columns =['Month_Year', 
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



#MT/27
montana_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-mt-statewide-itemized.csv')
variables_full_head = montana_full.head()
montana = montana_full.copy()
montana = montana[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
montana['Volume'] = montana['DOSAGE_UNIT']*montana['dos_str']
montana['col'] = montana['TRANSACTION_DATE'].astype(str)
montana['YEAR'] = montana['col'].str[-4:]
montana['DAY_MONTH'] = montana['col'].str[:-4]
montana['DAY'] = montana['DAY_MONTH'].str[-2:]
montana['MONTH'] = montana['DAY_MONTH'].str[:-2]
montana.drop('col', axis=1, inplace=True)
montana.drop('DAY_MONTH', axis=1, inplace=True)
montana.drop('TRANSACTION_DATE', axis=1, inplace=True)
montana['M_X'] = ('m' + montana['MONTH'])
montana['MONTH_YEAR'] = montana['YEAR'] + montana['M_X']
montana['PURDUE_VS_INDUSTRY'] = np.where(montana['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(montana, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
montana_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
montana_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data27_A = pd.DataFrame(montana_A.to_records())
data27_B = pd.DataFrame(montana_B.to_records())
data27_A.fillna(0)
data27_B.fillna(0)
for col in data27_A.columns: 
    print(col)
data27_A.columns =['Month_Year', 
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



#NE/28
nebraska_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-ne-statewide-itemized.csv')
variables_full_head = nebraska_full.head()
nebraska = nebraska_full.copy()
nebraska = nebraska[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
nebraska['Volume'] = nebraska['DOSAGE_UNIT']*nebraska['dos_str']
nebraska['col'] = nebraska['TRANSACTION_DATE'].astype(str)
nebraska['YEAR'] = nebraska['col'].str[-4:]
nebraska['DAY_MONTH'] = nebraska['col'].str[:-4]
nebraska['DAY'] = nebraska['DAY_MONTH'].str[-2:]
nebraska['MONTH'] = nebraska['DAY_MONTH'].str[:-2]
nebraska.drop('col', axis=1, inplace=True)
nebraska.drop('DAY_MONTH', axis=1, inplace=True)
nebraska.drop('TRANSACTION_DATE', axis=1, inplace=True)
nebraska['M_X'] = ('m' + nebraska['MONTH'])
nebraska['MONTH_YEAR'] = nebraska['YEAR'] + nebraska['M_X']
nebraska['PURDUE_VS_INDUSTRY'] = np.where(nebraska['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(nebraska, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
nebraska_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
nebraska_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data28_A = pd.DataFrame(nebraska_A.to_records())
data28_B = pd.DataFrame(nebraska_B.to_records())
data28_A.fillna(0)
data28_B.fillna(0)
for col in data28_A.columns: 
    print(col)
data28_A.columns =['Month_Year', 
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



#NV/29
nevada_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-nv-statewide-itemized.csv')
variables_full_head = nevada_full.head()
nevada = nevada_full.copy()
nevada = nevada[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
nevada['Volume'] = nevada['DOSAGE_UNIT']*nevada['dos_str']
nevada['col'] = nevada['TRANSACTION_DATE'].astype(str)
nevada['YEAR'] = nevada['col'].str[-4:]
nevada['DAY_MONTH'] = nevada['col'].str[:-4]
nevada['DAY'] = nevada['DAY_MONTH'].str[-2:]
nevada['MONTH'] = nevada['DAY_MONTH'].str[:-2]
nevada.drop('col', axis=1, inplace=True)
nevada.drop('DAY_MONTH', axis=1, inplace=True)
nevada.drop('TRANSACTION_DATE', axis=1, inplace=True)
nevada['M_X'] = ('m' + nevada['MONTH'])
nevada['MONTH_YEAR'] = nevada['YEAR'] + nevada['M_X']
nevada['PURDUE_VS_INDUSTRY'] = np.where(nevada['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(nevada, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
nevada_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
nevada_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data29_A = pd.DataFrame(nevada_A.to_records())
data29_B = pd.DataFrame(nevada_B.to_records())
data29_A.fillna(0)
data29_B.fillna(0)
for col in data29_A.columns: 
    print(col)
data29_A.columns =['Month_Year', 
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



#NH/30
newhampshire_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-nh-statewide-itemized.csv')
variables_full_head = newhampshire_full.head()
newhampshire = newhampshire_full.copy()
newhampshire = newhampshire[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
newhampshire['Volume'] = newhampshire['DOSAGE_UNIT']*newhampshire['dos_str']
newhampshire['col'] = newhampshire['TRANSACTION_DATE'].astype(str)
newhampshire['YEAR'] = newhampshire['col'].str[-4:]
newhampshire['DAY_MONTH'] = newhampshire['col'].str[:-4]
newhampshire['DAY'] = newhampshire['DAY_MONTH'].str[-2:]
newhampshire['MONTH'] = newhampshire['DAY_MONTH'].str[:-2]
newhampshire.drop('col', axis=1, inplace=True)
newhampshire.drop('DAY_MONTH', axis=1, inplace=True)
newhampshire.drop('TRANSACTION_DATE', axis=1, inplace=True)
newhampshire['M_X'] = ('m' + newhampshire['MONTH'])
newhampshire['MONTH_YEAR'] = newhampshire['YEAR'] + newhampshire['M_X']
newhampshire['PURDUE_VS_INDUSTRY'] = np.where(newhampshire['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(newhampshire, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
newhampshire_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
newhampshire_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data30_A = pd.DataFrame(newhampshire_A.to_records())
data30_B = pd.DataFrame(newhampshire_B.to_records())
data30_A.fillna(0)
data30_B.fillna(0)
for col in data30_A.columns: 
    print(col)
data30_A.columns =['Month_Year', 
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



#NJ/31
newjersey_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-nj-statewide-itemized.csv')
variables_full_head = newjersey_full.head()
newjersey = newjersey_full.copy()
newjersey = newjersey[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
newjersey['Volume'] = newjersey['DOSAGE_UNIT']*newjersey['dos_str']
newjersey['col'] = newjersey['TRANSACTION_DATE'].astype(str)
newjersey['YEAR'] = newjersey['col'].str[-4:]
newjersey['DAY_MONTH'] = newjersey['col'].str[:-4]
newjersey['DAY'] = newjersey['DAY_MONTH'].str[-2:]
newjersey['MONTH'] = newjersey['DAY_MONTH'].str[:-2]
newjersey.drop('col', axis=1, inplace=True)
newjersey.drop('DAY_MONTH', axis=1, inplace=True)
newjersey.drop('TRANSACTION_DATE', axis=1, inplace=True)
newjersey['M_X'] = ('m' + newjersey['MONTH'])
newjersey['MONTH_YEAR'] = newjersey['YEAR'] + newjersey['M_X']
newjersey['PURDUE_VS_INDUSTRY'] = np.where(newjersey['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(newjersey, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
newjersey_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
newjersey_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data31_A = pd.DataFrame(newjersey_A.to_records())
data31_B = pd.DataFrame(newjersey_B.to_records())
data31_A.fillna(0)
data31_B.fillna(0)
for col in data31_A.columns: 
    print(col)
data31_A.columns =['Month_Year', 
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


#NM/32
newmexico_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-nm-statewide-itemized.csv')
variables_full_head = newmexico_full.head()
newmexico = newmexico_full.copy()
newmexico = newmexico[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
newmexico['Volume'] = newmexico['DOSAGE_UNIT']*newmexico['dos_str']
newmexico['col'] = newmexico['TRANSACTION_DATE'].astype(str)
newmexico['YEAR'] = newmexico['col'].str[-4:]
newmexico['DAY_MONTH'] = newmexico['col'].str[:-4]
newmexico['DAY'] = newmexico['DAY_MONTH'].str[-2:]
newmexico['MONTH'] = newmexico['DAY_MONTH'].str[:-2]
newmexico.drop('col', axis=1, inplace=True)
newmexico.drop('DAY_MONTH', axis=1, inplace=True)
newmexico.drop('TRANSACTION_DATE', axis=1, inplace=True)
newmexico['M_X'] = ('m' + newmexico['MONTH'])
newmexico['MONTH_YEAR'] = newmexico['YEAR'] + newmexico['M_X']
newmexico['PURDUE_VS_INDUSTRY'] = np.where(newmexico['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(newmexico, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
newmexico_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
newmexico_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data32_A = pd.DataFrame(newmexico_A.to_records())
data32_B = pd.DataFrame(newmexico_B.to_records())
data32_A.fillna(0)
data32_B.fillna(0)
for col in data32_A.columns: 
    print(col)
data32_A.columns =['Month_Year', 
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



#NY/33
newyork_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-ny-statewide-itemized.csv')
variables_full_head = newyork_full.head()
newyork = newyork_full.copy()
newyork = newyork[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
newyork['Volume'] = newyork['DOSAGE_UNIT']*newyork['dos_str']
newyork['col'] = newyork['TRANSACTION_DATE'].astype(str)
newyork['YEAR'] = newyork['col'].str[-4:]
newyork['DAY_MONTH'] = newyork['col'].str[:-4]
newyork['DAY'] = newyork['DAY_MONTH'].str[-2:]
newyork['MONTH'] = newyork['DAY_MONTH'].str[:-2]
newyork.drop('col', axis=1, inplace=True)
newyork.drop('DAY_MONTH', axis=1, inplace=True)
newyork.drop('TRANSACTION_DATE', axis=1, inplace=True)
newyork['M_X'] = ('m' + newyork['MONTH'])
newyork['MONTH_YEAR'] = newyork['YEAR'] + newyork['M_X']
newyork['PURDUE_VS_INDUSTRY'] = np.where(newyork['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(newyork, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
newyork_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
newyork_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data33_A = pd.DataFrame(newyork_A.to_records())
data33_B = pd.DataFrame(newyork_B.to_records())
data33_A.fillna(0)
data33_B.fillna(0)
for col in data33_A.columns: 
    print(col)
data33_A.columns =['Month_Year', 
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



#NC/34
northcarolina_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-nc-statewide-itemized.csv')
variables_full_head = northcarolina_full.head()
northcarolina = northcarolina_full.copy()
northcarolina = northcarolina[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
northcarolina['Volume'] = northcarolina['DOSAGE_UNIT']*northcarolina['dos_str']
northcarolina['col'] = northcarolina['TRANSACTION_DATE'].astype(str)
northcarolina['YEAR'] = northcarolina['col'].str[-4:]
northcarolina['DAY_MONTH'] = northcarolina['col'].str[:-4]
northcarolina['DAY'] = northcarolina['DAY_MONTH'].str[-2:]
northcarolina['MONTH'] = northcarolina['DAY_MONTH'].str[:-2]
northcarolina.drop('col', axis=1, inplace=True)
northcarolina.drop('DAY_MONTH', axis=1, inplace=True)
northcarolina.drop('TRANSACTION_DATE', axis=1, inplace=True)
northcarolina['M_X'] = ('m' + northcarolina['MONTH'])
northcarolina['MONTH_YEAR'] = northcarolina['YEAR'] + northcarolina['M_X']
northcarolina['PURDUE_VS_INDUSTRY'] = np.where(northcarolina['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(northcarolina, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
northcarolina_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
northcarolina_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data34_A = pd.DataFrame(northcarolina_A.to_records())
data34_B = pd.DataFrame(northcarolina_B.to_records())
data34_A.fillna(0)
data34_B.fillna(0)
for col in data34_A.columns: 
    print(col)
data34_A.columns =['Month_Year', 
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



#ND/35
northdakota_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-nd-statewide-itemized.csv')
variables_full_head = northdakota_full.head()
northdakota = northdakota_full.copy()
northdakota = northdakota[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
northdakota['Volume'] = northdakota['DOSAGE_UNIT']*northdakota['dos_str']
northdakota['col'] = northdakota['TRANSACTION_DATE'].astype(str)
northdakota['YEAR'] = northdakota['col'].str[-4:]
northdakota['DAY_MONTH'] = northdakota['col'].str[:-4]
northdakota['DAY'] = northdakota['DAY_MONTH'].str[-2:]
northdakota['MONTH'] = northdakota['DAY_MONTH'].str[:-2]
northdakota.drop('col', axis=1, inplace=True)
northdakota.drop('DAY_MONTH', axis=1, inplace=True)
northdakota.drop('TRANSACTION_DATE', axis=1, inplace=True)
northdakota['M_X'] = ('m' + northdakota['MONTH'])
northdakota['MONTH_YEAR'] = northdakota['YEAR'] + northdakota['M_X']
northdakota['PURDUE_VS_INDUSTRY'] = np.where(northdakota['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(northdakota, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
northdakota_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
northdakota_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data35_A = pd.DataFrame(northdakota_A.to_records())
data35_B = pd.DataFrame(northdakota_B.to_records())
data35_A.fillna(0)
data35_B.fillna(0)
for col in data35_A.columns: 
    print(col)
data35_A.columns =['Month_Year', 
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



#OH/36
ohio_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-oh-statewide-itemized.csv')
variables_full_head = ohio_full.head()
ohio = ohio_full.copy()
ohio = ohio[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
ohio['Volume'] = ohio['DOSAGE_UNIT']*ohio['dos_str']
ohio['col'] = ohio['TRANSACTION_DATE'].astype(str)
ohio['YEAR'] = ohio['col'].str[-4:]
ohio['DAY_MONTH'] = ohio['col'].str[:-4]
ohio['DAY'] = ohio['DAY_MONTH'].str[-2:]
ohio['MONTH'] = ohio['DAY_MONTH'].str[:-2]
ohio.drop('col', axis=1, inplace=True)
ohio.drop('DAY_MONTH', axis=1, inplace=True)
ohio.drop('TRANSACTION_DATE', axis=1, inplace=True)
ohio['M_X'] = ('m' + ohio['MONTH'])
ohio['MONTH_YEAR'] = ohio['YEAR'] + ohio['M_X']
ohio['PURDUE_VS_INDUSTRY'] = np.where(ohio['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(ohio, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
ohio_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
ohio_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data36_A = pd.DataFrame(ohio_A.to_records())
data36_B = pd.DataFrame(ohio_B.to_records())
data36_A.fillna(0)
data36_B.fillna(0)
for col in data36_A.columns: 
    print(col)
data36_A.columns =['Month_Year', 
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



#OK/37
oklahoma_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-ok-statewide-itemized.csv')
variables_full_head = oklahoma_full.head()
oklahoma = oklahoma_full.copy()
oklahoma = oklahoma[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
oklahoma['Volume'] = oklahoma['DOSAGE_UNIT']*oklahoma['dos_str']
oklahoma['col'] = oklahoma['TRANSACTION_DATE'].astype(str)
oklahoma['YEAR'] = oklahoma['col'].str[-4:]
oklahoma['DAY_MONTH'] = oklahoma['col'].str[:-4]
oklahoma['DAY'] = oklahoma['DAY_MONTH'].str[-2:]
oklahoma['MONTH'] = oklahoma['DAY_MONTH'].str[:-2]
oklahoma.drop('col', axis=1, inplace=True)
oklahoma.drop('DAY_MONTH', axis=1, inplace=True)
oklahoma.drop('TRANSACTION_DATE', axis=1, inplace=True)
oklahoma['M_X'] = ('m' + oklahoma['MONTH'])
oklahoma['MONTH_YEAR'] = oklahoma['YEAR'] + oklahoma['M_X']
oklahoma['PURDUE_VS_INDUSTRY'] = np.where(oklahoma['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(oklahoma, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
oklahoma_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
oklahoma_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data37_A = pd.DataFrame(oklahoma_A.to_records())
data37_B = pd.DataFrame(oklahoma_B.to_records())
data37_A.fillna(0)
data37_B.fillna(0)
for col in data37_A.columns: 
    print(col)
data37_A.columns =['Month_Year', 
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



#OR/38
oregon_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-or-statewide-itemized.csv')
variables_full_head = oregon_full.head()
oregon = oregon_full.copy()
oregon = oregon[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
oregon['Volume'] = oregon['DOSAGE_UNIT']*oregon['dos_str']
oregon['col'] = oregon['TRANSACTION_DATE'].astype(str)
oregon['YEAR'] = oregon['col'].str[-4:]
oregon['DAY_MONTH'] = oregon['col'].str[:-4]
oregon['DAY'] = oregon['DAY_MONTH'].str[-2:]
oregon['MONTH'] = oregon['DAY_MONTH'].str[:-2]
oregon.drop('col', axis=1, inplace=True)
oregon.drop('DAY_MONTH', axis=1, inplace=True)
oregon.drop('TRANSACTION_DATE', axis=1, inplace=True)
oregon['M_X'] = ('m' + oregon['MONTH'])
oregon['MONTH_YEAR'] = oregon['YEAR'] + oregon['M_X']
oregon['PURDUE_VS_INDUSTRY'] = np.where(oregon['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(oregon, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
oregon_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
oregon_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data38_A = pd.DataFrame(oregon_A.to_records())
data38_B = pd.DataFrame(oregon_B.to_records())
data38_A.fillna(0)
data38_B.fillna(0)
for col in data38_A.columns: 
    print(col)
data38_A.columns =['Month_Year', 
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



#PA/39
pennsylvania_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-pa-statewide-itemized.csv')
variables_full_head = pennsylvania_full.head()
pennsylvania = pennsylvania_full.copy()
pennsylvania = pennsylvania[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
pennsylvania['Volume'] = pennsylvania['DOSAGE_UNIT']*pennsylvania['dos_str']
pennsylvania['col'] = pennsylvania['TRANSACTION_DATE'].astype(str)
pennsylvania['YEAR'] = pennsylvania['col'].str[-4:]
pennsylvania['DAY_MONTH'] = pennsylvania['col'].str[:-4]
pennsylvania['DAY'] = pennsylvania['DAY_MONTH'].str[-2:]
pennsylvania['MONTH'] = pennsylvania['DAY_MONTH'].str[:-2]
pennsylvania.drop('col', axis=1, inplace=True)
pennsylvania.drop('DAY_MONTH', axis=1, inplace=True)
pennsylvania.drop('TRANSACTION_DATE', axis=1, inplace=True)
pennsylvania['M_X'] = ('m' + pennsylvania['MONTH'])
pennsylvania['MONTH_YEAR'] = pennsylvania['YEAR'] + pennsylvania['M_X']
pennsylvania['PURDUE_VS_INDUSTRY'] = np.where(pennsylvania['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(pennsylvania, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
pennsylvania_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
pennsylvania_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data39_A = pd.DataFrame(pennsylvania_A.to_records())
data39_B = pd.DataFrame(pennsylvania_B.to_records())
data39_A.fillna(0)
data39_B.fillna(0)
for col in data39_A.columns: 
    print(col)
data39_A.columns =['Month_Year', 
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



#RI/40
rhodeisland_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-ri-statewide-itemized.csv')
variables_full_head = rhodeisland_full.head()
rhodeisland = rhodeisland_full.copy()
rhodeisland = rhodeisland[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
rhodeisland['Volume'] = rhodeisland['DOSAGE_UNIT']*rhodeisland['dos_str']
rhodeisland['col'] = rhodeisland['TRANSACTION_DATE'].astype(str)
rhodeisland['YEAR'] = rhodeisland['col'].str[-4:]
rhodeisland['DAY_MONTH'] = rhodeisland['col'].str[:-4]
rhodeisland['DAY'] = rhodeisland['DAY_MONTH'].str[-2:]
rhodeisland['MONTH'] = rhodeisland['DAY_MONTH'].str[:-2]
rhodeisland.drop('col', axis=1, inplace=True)
rhodeisland.drop('DAY_MONTH', axis=1, inplace=True)
rhodeisland.drop('TRANSACTION_DATE', axis=1, inplace=True)
rhodeisland['M_X'] = ('m' + rhodeisland['MONTH'])
rhodeisland['MONTH_YEAR'] = rhodeisland['YEAR'] + rhodeisland['M_X']
rhodeisland['PURDUE_VS_INDUSTRY'] = np.where(rhodeisland['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(rhodeisland, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
rhodeisland_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
rhodeisland_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data40_A = pd.DataFrame(rhodeisland_A.to_records())
data40_B = pd.DataFrame(rhodeisland_B.to_records())
data40_A.fillna(0)
data40_B.fillna(0)
for col in data40_A.columns: 
    print(col)
data40_A.columns =['Month_Year', 
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



#SC/41
southcarolina_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-sc-statewide-itemized.csv')
variables_full_head = southcarolina_full.head()
southcarolina = southcarolina_full.copy()
southcarolina = southcarolina[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
southcarolina['Volume'] = southcarolina['DOSAGE_UNIT']*southcarolina['dos_str']
southcarolina['col'] = southcarolina['TRANSACTION_DATE'].astype(str)
southcarolina['YEAR'] = southcarolina['col'].str[-4:]
southcarolina['DAY_MONTH'] = southcarolina['col'].str[:-4]
southcarolina['DAY'] = southcarolina['DAY_MONTH'].str[-2:]
southcarolina['MONTH'] = southcarolina['DAY_MONTH'].str[:-2]
southcarolina.drop('col', axis=1, inplace=True)
southcarolina.drop('DAY_MONTH', axis=1, inplace=True)
southcarolina.drop('TRANSACTION_DATE', axis=1, inplace=True)
southcarolina['M_X'] = ('m' + southcarolina['MONTH'])
southcarolina['MONTH_YEAR'] = southcarolina['YEAR'] + southcarolina['M_X']
southcarolina['PURDUE_VS_INDUSTRY'] = np.where(southcarolina['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(southcarolina, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
southcarolina_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
southcarolina_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data41_A = pd.DataFrame(southcarolina_A.to_records())
data41_B = pd.DataFrame(southcarolina_B.to_records())
data41_A.fillna(0)
data41_B.fillna(0)
for col in data41_A.columns: 
    print(col)
data41_A.columns =['Month_Year', 
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



#SD/42
southdakota_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-sd-statewide-itemized.csv')
variables_full_head = southdakota_full.head()
southdakota = southdakota_full.copy()
southdakota = southdakota[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
southdakota['Volume'] = southdakota['DOSAGE_UNIT']*southdakota['dos_str']
southdakota['col'] = southdakota['TRANSACTION_DATE'].astype(str)
southdakota['YEAR'] = southdakota['col'].str[-4:]
southdakota['DAY_MONTH'] = southdakota['col'].str[:-4]
southdakota['DAY'] = southdakota['DAY_MONTH'].str[-2:]
southdakota['MONTH'] = southdakota['DAY_MONTH'].str[:-2]
southdakota.drop('col', axis=1, inplace=True)
southdakota.drop('DAY_MONTH', axis=1, inplace=True)
southdakota.drop('TRANSACTION_DATE', axis=1, inplace=True)
southdakota['M_X'] = ('m' + southdakota['MONTH'])
southdakota['MONTH_YEAR'] = southdakota['YEAR'] + southdakota['M_X']
southdakota['PURDUE_VS_INDUSTRY'] = np.where(southdakota['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(southdakota, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
southdakota_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
southdakota_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data42_A = pd.DataFrame(southdakota_A.to_records())
data42_B = pd.DataFrame(southdakota_B.to_records())
data42_A.fillna(0)
data42_B.fillna(0)
for col in data42_A.columns: 
    print(col)
data42_A.columns =['Month_Year', 
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



#TN/43
tennessee_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-tn-statewide-itemized.csv')
variables_full_head = tennessee_full.head()
tennessee = tennessee_full.copy()
tennessee = tennessee[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
tennessee['Volume'] = tennessee['DOSAGE_UNIT']*tennessee['dos_str']
tennessee['col'] = tennessee['TRANSACTION_DATE'].astype(str)
tennessee['YEAR'] = tennessee['col'].str[-4:]
tennessee['DAY_MONTH'] = tennessee['col'].str[:-4]
tennessee['DAY'] = tennessee['DAY_MONTH'].str[-2:]
tennessee['MONTH'] = tennessee['DAY_MONTH'].str[:-2]
tennessee.drop('col', axis=1, inplace=True)
tennessee.drop('DAY_MONTH', axis=1, inplace=True)
tennessee.drop('TRANSACTION_DATE', axis=1, inplace=True)
tennessee['M_X'] = ('m' + tennessee['MONTH'])
tennessee['MONTH_YEAR'] = tennessee['YEAR'] + tennessee['M_X']
tennessee['PURDUE_VS_INDUSTRY'] = np.where(tennessee['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(tennessee, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
tennessee_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
tennessee_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data43_A = pd.DataFrame(tennessee_A.to_records())
data43_B = pd.DataFrame(tennessee_B.to_records())
data43_A.fillna(0)
data43_B.fillna(0)
for col in data43_A.columns: 
    print(col)
data43_A.columns =['Month_Year', 
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



#TX/44
texas_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-tx-statewide-itemized.csv')
variables_full_head = texas_full.head()
texas = texas_full.copy()
texas = texas[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
texas['Volume'] = texas['DOSAGE_UNIT']*texas['dos_str']
texas['col'] = texas['TRANSACTION_DATE'].astype(str)
texas['YEAR'] = texas['col'].str[-4:]
texas['DAY_MONTH'] = texas['col'].str[:-4]
texas['DAY'] = texas['DAY_MONTH'].str[-2:]
texas['MONTH'] = texas['DAY_MONTH'].str[:-2]
texas.drop('col', axis=1, inplace=True)
texas.drop('DAY_MONTH', axis=1, inplace=True)
texas.drop('TRANSACTION_DATE', axis=1, inplace=True)
texas['M_X'] = ('m' + texas['MONTH'])
texas['MONTH_YEAR'] = texas['YEAR'] + texas['M_X']
texas['PURDUE_VS_INDUSTRY'] = np.where(texas['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(texas, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
texas_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
texas_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data44_A = pd.DataFrame(texas_A.to_records())
data44_B = pd.DataFrame(texas_B.to_records())
data44_A.fillna(0)
data44_B.fillna(0)
for col in data44_A.columns: 
    print(col)
data44_A.columns =['Month_Year', 
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



#UT/45
utah_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-ut-statewide-itemized.csv')
variables_full_head = utah_full.head()
utah = utah_full.copy()
utah = utah[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
utah['Volume'] = utah['DOSAGE_UNIT']*utah['dos_str']
utah['col'] = utah['TRANSACTION_DATE'].astype(str)
utah['YEAR'] = utah['col'].str[-4:]
utah['DAY_MONTH'] = utah['col'].str[:-4]
utah['DAY'] = utah['DAY_MONTH'].str[-2:]
utah['MONTH'] = utah['DAY_MONTH'].str[:-2]
utah.drop('col', axis=1, inplace=True)
utah.drop('DAY_MONTH', axis=1, inplace=True)
utah.drop('TRANSACTION_DATE', axis=1, inplace=True)
utah['M_X'] = ('m' + utah['MONTH'])
utah['MONTH_YEAR'] = utah['YEAR'] + utah['M_X']
utah['PURDUE_VS_INDUSTRY'] = np.where(utah['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(utah, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
utah_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
utah_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data45_A = pd.DataFrame(utah_A.to_records())
data45_B = pd.DataFrame(utah_B.to_records())
data45_A.fillna(0)
data45_B.fillna(0)
for col in data45_A.columns: 
    print(col)
data45_A.columns =['Month_Year', 
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



#VT/46
vermont_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-vt-statewide-itemized.csv')
variables_full_head = vermont_full.head()
vermont = vermont_full.copy()
vermont = vermont[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
vermont['Volume'] = vermont['DOSAGE_UNIT']*vermont['dos_str']
vermont['col'] = vermont['TRANSACTION_DATE'].astype(str)
vermont['YEAR'] = vermont['col'].str[-4:]
vermont['DAY_MONTH'] = vermont['col'].str[:-4]
vermont['DAY'] = vermont['DAY_MONTH'].str[-2:]
vermont['MONTH'] = vermont['DAY_MONTH'].str[:-2]
vermont.drop('col', axis=1, inplace=True)
vermont.drop('DAY_MONTH', axis=1, inplace=True)
vermont.drop('TRANSACTION_DATE', axis=1, inplace=True)
vermont['M_X'] = ('m' + vermont['MONTH'])
vermont['MONTH_YEAR'] = vermont['YEAR'] + vermont['M_X']
vermont['PURDUE_VS_INDUSTRY'] = np.where(vermont['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(vermont, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
vermont_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
vermont_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data45_A = pd.DataFrame(vermont_A.to_records())
data45_B = pd.DataFrame(vermont_B.to_records())
data45_A.fillna(0)
data45_B.fillna(0)
for col in data45_A.columns: 
    print(col)
data45_A.columns =['Month_Year', 
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



#VA/47
virginia_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-va-statewide-itemized.csv')
variables_full_head = virginia_full.head()
virginia = virginia_full.copy()
virginia = virginia[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
virginia['Volume'] = virginia['DOSAGE_UNIT']*virginia['dos_str']
virginia['col'] = virginia['TRANSACTION_DATE'].astype(str)
virginia['YEAR'] = virginia['col'].str[-4:]
virginia['DAY_MONTH'] = virginia['col'].str[:-4]
virginia['DAY'] = virginia['DAY_MONTH'].str[-2:]
virginia['MONTH'] = virginia['DAY_MONTH'].str[:-2]
virginia.drop('col', axis=1, inplace=True)
virginia.drop('DAY_MONTH', axis=1, inplace=True)
virginia.drop('TRANSACTION_DATE', axis=1, inplace=True)
virginia['M_X'] = ('m' + virginia['MONTH'])
virginia['MONTH_YEAR'] = virginia['YEAR'] + virginia['M_X']
virginia['PURDUE_VS_INDUSTRY'] = np.where(virginia['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(virginia, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
virginia_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
virginia_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data46_A = pd.DataFrame(virginia_A.to_records())
data46_B = pd.DataFrame(virginia_B.to_records())
data46_A.fillna(0)
data46_B.fillna(0)
for col in data46_A.columns: 
    print(col)
data46_A.columns =['Month_Year', 
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



#WA/48
washington_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-wa-statewide-itemized.csv')
variables_full_head = washington_full.head()
washington = washington_full.copy()
washington = washington[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
washington['Volume'] = washington['DOSAGE_UNIT']*washington['dos_str']
washington['col'] = washington['TRANSACTION_DATE'].astype(str)
washington['YEAR'] = washington['col'].str[-4:]
washington['DAY_MONTH'] = washington['col'].str[:-4]
washington['DAY'] = washington['DAY_MONTH'].str[-2:]
washington['MONTH'] = washington['DAY_MONTH'].str[:-2]
washington.drop('col', axis=1, inplace=True)
washington.drop('DAY_MONTH', axis=1, inplace=True)
washington.drop('TRANSACTION_DATE', axis=1, inplace=True)
washington['M_X'] = ('m' + washington['MONTH'])
washington['MONTH_YEAR'] = washington['YEAR'] + washington['M_X']
washington['PURDUE_VS_INDUSTRY'] = np.where(washington['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(washington, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
washington_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
washington_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data47_A = pd.DataFrame(washington_A.to_records())
data47_B = pd.DataFrame(washington_B.to_records())
data47_A.fillna(0)
data47_B.fillna(0)
for col in data47_A.columns: 
    print(col)
data47_A.columns =['Month_Year', 
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



#WV/49
westvirginia_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-wv-statewide-itemized.csv')
variables_full_head = westvirginia_full.head()
westvirginia = westvirginia_full.copy()
westvirginia = westvirginia[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
westvirginia['Volume'] = westvirginia['DOSAGE_UNIT']*westvirginia['dos_str']
westvirginia['col'] = westvirginia['TRANSACTION_DATE'].astype(str)
westvirginia['YEAR'] = westvirginia['col'].str[-4:]
westvirginia['DAY_MONTH'] = westvirginia['col'].str[:-4]
westvirginia['DAY'] = westvirginia['DAY_MONTH'].str[-2:]
westvirginia['MONTH'] = westvirginia['DAY_MONTH'].str[:-2]
westvirginia.drop('col', axis=1, inplace=True)
westvirginia.drop('DAY_MONTH', axis=1, inplace=True)
westvirginia.drop('TRANSACTION_DATE', axis=1, inplace=True)
westvirginia['M_X'] = ('m' + westvirginia['MONTH'])
westvirginia['MONTH_YEAR'] = westvirginia['YEAR'] + westvirginia['M_X']
westvirginia['PURDUE_VS_INDUSTRY'] = np.where(westvirginia['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(westvirginia, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
westvirginia_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
westvirginia_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data49_A = pd.DataFrame(westvirginia_A.to_records())
data49_B = pd.DataFrame(westvirginia_B.to_records())
data49_A.fillna(0)
data49_B.fillna(0)
for col in data49_A.columns: 
    print(col)
data49_A.columns =['Month_Year', 
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



#WI/50
wisconsin_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-wi-statewide-itemized.csv')
variables_full_head = wisconsin_full.head()
wisconsin = wisconsin_full.copy()
wisconsin = wisconsin[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
wisconsin['Volume'] = wisconsin['DOSAGE_UNIT']*wisconsin['dos_str']
wisconsin['col'] = wisconsin['TRANSACTION_DATE'].astype(str)
wisconsin['YEAR'] = wisconsin['col'].str[-4:]
wisconsin['DAY_MONTH'] = wisconsin['col'].str[:-4]
wisconsin['DAY'] = wisconsin['DAY_MONTH'].str[-2:]
wisconsin['MONTH'] = wisconsin['DAY_MONTH'].str[:-2]
wisconsin.drop('col', axis=1, inplace=True)
wisconsin.drop('DAY_MONTH', axis=1, inplace=True)
wisconsin.drop('TRANSACTION_DATE', axis=1, inplace=True)
wisconsin['M_X'] = ('m' + wisconsin['MONTH'])
wisconsin['MONTH_YEAR'] = wisconsin['YEAR'] + wisconsin['M_X']
wisconsin['PURDUE_VS_INDUSTRY'] = np.where(wisconsin['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(wisconsin, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
wisconsin_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
wisconsin_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data50_A = pd.DataFrame(wisconsin_A.to_records())
data50_B = pd.DataFrame(wisconsin_B.to_records())
data50_A.fillna(0)
data50_B.fillna(0)
for col in data50_A.columns: 
    print(col)
data50_A.columns =['Month_Year', 
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



#WY/51
wyoming_full = pd.read_csv('/Volumes/ZOE ZIRLIN/arcos-wy-statewide-itemized.csv')
variables_full_head = wyoming_full.head()
wyoming = wyoming_full.copy()
wyoming = wyoming[['BUYER_STATE','BUYER_COUNTY','Combined_Labeler_Name','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]
wyoming['Volume'] = wyoming['DOSAGE_UNIT']*wyoming['dos_str']
wyoming['col'] = wyoming['TRANSACTION_DATE'].astype(str)
wyoming['YEAR'] = wyoming['col'].str[-4:]
wyoming['DAY_MONTH'] = wyoming['col'].str[:-4]
wyoming['DAY'] = wyoming['DAY_MONTH'].str[-2:]
wyoming['MONTH'] = wyoming['DAY_MONTH'].str[:-2]
wyoming.drop('col', axis=1, inplace=True)
wyoming.drop('DAY_MONTH', axis=1, inplace=True)
wyoming.drop('TRANSACTION_DATE', axis=1, inplace=True)
wyoming['M_X'] = ('m' + wyoming['MONTH'])
wyoming['MONTH_YEAR'] = wyoming['YEAR'] + wyoming['M_X']
wyoming['PURDUE_VS_INDUSTRY'] = np.where(wyoming['Combined_Labeler_Name'] == 'Purdue Pharma LP', 'Purdue', 'Industry')
fip = pd.read_excel('/Volumes/ZOE ZIRLIN/US_FIPS_Codes.xls', converters={'FIPS County': lambda x: str(x)})
fip['FIP_CODE'] = fip['STATE_AB'] + fip['FIPS County']
fip['County Name'] = fip['County Name'].str.upper()
fip.drop('FIPS State', axis=1, inplace=True)
fip.drop('State', axis=1, inplace=True)
fip.drop('FIPS County', axis=1, inplace=True)
fip = fip.rename(columns={'County Name':'BUYER_COUNTY'})
fip = fip.rename(columns={'STATE_AB':'BUYER_STATE'})
x = pd.merge(wyoming, fip, on=['BUYER_COUNTY','BUYER_STATE'], how='inner')
wyoming_A = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='PURDUE_VS_INDUSTRY',aggfunc=np.sum)
wyoming_B = pd.pivot_table(data=x, index = ['MONTH_YEAR', 'BUYER_COUNTY', 'YEAR', 'MONTH', 'BUYER_STATE', 'FIP_CODE'], values = ['MME', 'Volume', 'DOSAGE_UNIT'], columns='Combined_Labeler_Name',aggfunc=np.sum)
data51_A = pd.DataFrame(wyoming_A.to_records())
data51_B = pd.DataFrame(wyoming_B.to_records())
data51_A.fillna(0)
data51_B.fillna(0)
for col in data51_A.columns: 
    print(col)
data51_A.columns =['Month_Year', 
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














data_A = pd.concat([data1_A,
﻿                   data2_A,
﻿                   data3_A,
﻿                   data4_A,
﻿                   data5_A,
﻿                   data6_A,
                    data7_A,
﻿                   data8_A,
                    data9_A,
 data10_A,
﻿data11_A,
﻿data12_A,
﻿data13_A,
﻿data14_A,
﻿data15_A,
﻿data16_A,
﻿data17_A,
﻿data18_A,
﻿data19_A,
﻿data20_A,
﻿data21_A,
﻿data22_A,
﻿data23_A,
﻿data24_A,
﻿data25_A,
﻿data26_A,
﻿data27_A,
﻿data28_A,
﻿data29_A,
﻿data30_A,
﻿data31_A,
﻿data32_A,
﻿data33_A,
﻿data34_A,
﻿data35_A,
﻿data36_A,
﻿data37_A,
﻿data38_A,
﻿data39_A,
﻿data40_A,
﻿data41_A,
﻿data42_A,
﻿data43_A,
﻿data44_A,
﻿data45_A,
﻿data46_A,
﻿data47_A,
﻿data48_A,
﻿data49_A,
﻿data50_A   
﻿data51_A 
                    ])


#data_B = pd.concat([data1_B, 
#                    data2_B
#                    
#                    ])
