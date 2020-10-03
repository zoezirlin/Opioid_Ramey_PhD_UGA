# Github for WashPost https://github.com/wpinvestigative/arcos-api
# WashPost ARCOS API: https://arcos-api.ext.nile.works/__swagger__/
# WashPost instructions for download: https://www.washingtonpost.com/national/2019/07/18/how-download-use-dea-pain-pills-database/

# Dataset is 75GB
# Variables needed:
#   - monthyears
#   - Transaction_date 
#   - State
#   - County name
#   - County FIP Code
#   - Total Purdue Dosage_unit
#   - Total Purdue_MME
#   - Total Purdue Volume
#   - Total Industry_Dosage_unit unincluding Purdue
#   - Total Industry_MME unincluding Purdue
#   - Industry_Volume unincluding Purdue
#   - Dosage_unit (this is the number of pills per county per monthyear)
#   - MME  (Volume of Morphine mg Equivalent, this is Dosage_unit*MME*dos_str in the original dataset)
#   - Volume of pills (dosage_unit*dos_str)






# ALABAMA


# ALASKA


# ARIZONA


# ARKANSAS


# CALIFORNIA


# COLORADO


# CONNETICUT


# DELEWARE


# FLORIDA


# GEORGIA


# HAWAII


# IDAHO


# ILLINOIS


# INDIANA


# IOWA


# KANSAS


# KENTUCKY


# LOUISIANA


# MAINE


# MARYLAND


# MASSACHUSETTS


# MICHIGAN


# MINNESOTA


# MISSISSIPPI


# MISSOURI


# MONTANA


# NEBRASKA


# NEVADA


# NEW HAMPSHIRE


# NEW JERSEY


# NEW MEXICO


# NEW YORK


# NORTH CAROLINA


# OHIO


# OKLAHOMA


# OREGON


# PENNSYLVANIA


# RHODE ISLAND


# SOUTH CAROLINA


# SOUTH DAKOTA


# TENNESSEE


# TEXAS


# UTAH


# VERMONT


# VIRGINIA


# WASHINGTON


# WEST VIRGINIA
wv_full = pd.read_csv('/Users/zoezirlin/Desktop/arcos-wv-statewide-itemized.csv')
wv_full.head()

# Roughly 2.4 million observations
wv = wv_full[['BUYER_STATE','BUYER_COUNTY','TRANSACTION_DATE','DOSAGE_UNIT','MME','dos_str']]

# delete na's

wv['DOSAGE_UNIT'] = wv['DOSAGE_UNIT']*wv['dos_str']


# WISCONSIN


# WYOMING
















# FINAL CONCATENATION
FINAL_frames = [AL,
                AK, 
                      county_info_AR,
                      county_info_AZ,
                      county_info_CA,
                      county_info_CO,
                      county_info_CT,
                      county_info_DC,
                      county_info_DE,
                      county_info_FL,
                      county_info_GA,
                      county_info_HI,
                      county_info_IA,
                      county_info_ID,
                      county_info_IL,
                      county_info_IN,
                      county_info_KS,
                      county_info_KY,
                      county_info_LA,
                      county_info_MA,
                      county_info_MD,
                      county_info_ME,
                      county_info_MI,
                      county_info_MN,
                      county_info_MO,
                      county_info_MS,
                      county_info_MT,
                      county_info_NC,
                      county_info_ND,
                      county_info_NE,
                      county_info_NH,
                      county_info_NJ,
                      county_info_NM,
                      county_info_NV,
                      county_info_NY,
                      county_info_OH,
                      county_info_OK,
                      county_info_OR,
                      county_info_PA,
                      county_info_RI,
                      county_info_SC,
                      county_info_SD,
                      county_info_TN,
                      county_info_TX,
                      county_info_UT,
                      county_info_VA,
                      county_info_VT,
                      county_info_WA,
                      county_info_WI,
                      county_info_WV,
                      county_info_WY
                      ]
master_set = pd.concat(FINAL_frames)





















# To-Do List
# - Create github repository
# - Set up version control support





import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


!pip install arcospy
import arcospy

help(arcospy)




# Step 1: Create dataset with State, County name, County FIP Code
#   Step 1.A: Create 52 datasets for all 52 states, including all variables
#   Step 1.B: Merge 52 datasets into 1 dataframe
#   Step 1.C: Drop unnecessary variables until we only have state, county name and county FIP code


# Step 1.A information: creating datasets with variables=
#   - Buyer county
#   - Buyer state
#   - County FIPS
#   - State
#   - County number
#   - County name
#   - Name
#   - Variables
#   - Year
#   - Population





state_ab = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]




# Step 1.A

county_info_AL = arcospy.county_population(state=["AL"], key="WaPo")
monthly_info_AL = arcospy.summarized_county_monthly(state=["AL"], key="WaPo")

county_info_AK = arcospy.county_population(state=["AK"], key="WaPo")
monthly_info_AK = arcospy.summarized_county_monthly(state=["AK"], key="WaPo")

county_info_AR = arcospy.county_population(state=["AR"], key="WaPo")
monthly_info_AR = arcospy.summarized_county_monthly(state=["AR"], key="WaPo")

county_info_AZ = arcospy.county_population(state=["AZ"], key="WaPo")
monthly_info_AZ = arcospy.summarized_county_monthly(state=["AZ"], key="WaPo")

county_info_CA = arcospy.county_population(state=["CA"], key="WaPo")
monthly_info_CA = arcospy.summarized_county_monthly(state=["CA"], key="WaPo")

county_info_CO = arcospy.county_population(state=["CO"], key="WaPo")
monthly_info_CO = arcospy.summarized_county_monthly(state=["CO"], key="WaPo")

county_info_CT = arcospy.county_population(state=["CT"], key="WaPo")
monthly_info_CT = arcospy.summarized_county_monthly(state=["CT"], key="WaPo")

county_info_DC = arcospy.county_population(state=["DC"], key="WaPo")
monthly_info_DC = arcospy.summarized_county_monthly(state=["DC"], key="WaPo")

county_info_DE = arcospy.county_population(state=["DE"], key="WaPo")
monthly_info_DE = arcospy.summarized_county_monthly(state=["DE"], key="WaPo")

county_info_FL = arcospy.county_population(state=["FL"], key="WaPo")
monthly_info_FL = arcospy.summarized_county_monthly(state=["FL"], key="WaPo")

county_info_GA = arcospy.county_population(state=["GA"], key="WaPo")
monthly_info_GA = arcospy.summarized_county_monthly(state=["GA"], key="WaPo")

county_info_HI = arcospy.county_population(state=["HI"], key="WaPo")
monthly_info_HI = arcospy.summarized_county_monthly(state=["HI"], key="WaPo")

county_info_ID = arcospy.county_population(state=["ID"], key="WaPo")
monthly_info_ID = arcospy.summarized_county_monthly(state=["ID"], key="WaPo")

county_info_IL = arcospy.county_population(state=["IL"], key="WaPo")
monthly_info_IL = arcospy.summarized_county_monthly(state=["IL"], key="WaPo")

county_info_IN = arcospy.county_population(state=["IN"], key="WaPo")
monthly_info_IN = arcospy.summarized_county_monthly(state=["IN"], key="WaPo")

county_info_IA = arcospy.county_population(state=["IA"], key="WaPo")
monthly_info_IA = arcospy.summarized_county_monthly(state=["IA"], key="WaPo")

county_info_KS = arcospy.county_population(state=["KS"], key="WaPo")
monthly_info_KS = arcospy.summarized_county_monthly(state=["KS"], key="WaPo")

county_info_KY = arcospy.county_population(state=["KY"], key="WaPo")
monthly_info_KY = arcospy.summarized_county_monthly(state=["KY"], key="WaPo")

county_info_LA = arcospy.county_population(state=["LA"], key="WaPo")
monthly_info_LA = arcospy.summarized_county_monthly(state=["LA"], key="WaPo")

county_info_ME = arcospy.county_population(state=["ME"], key="WaPo")
monthly_info_ME = arcospy.summarized_county_monthly(state=["ME"], key="WaPo")

county_info_MD = arcospy.county_population(state=["MD"], key="WaPo")
monthly_info_MD = arcospy.summarized_county_monthly(state=["MD"], key="WaPo")

county_info_MA = arcospy.county_population(state=["MA"], key="WaPo")
monthly_info_MA = arcospy.summarized_county_monthly(state=["MA"], key="WaPo")

county_info_MI = arcospy.county_population(state=["MI"], key="WaPo")
monthly_info_MI = arcospy.summarized_county_monthly(state=["MI"], key="WaPo")

county_info_MN = arcospy.county_population(state=["MN"], key="WaPo")
monthly_info_MN = arcospy.summarized_county_monthly(state=["MN"], key="WaPo")

county_info_MS = arcospy.county_population(state=["MS"], key="WaPo")
monthly_info_MS = arcospy.summarized_county_monthly(state=["MS"], key="WaPo")

county_info_MO = arcospy.county_population(state=["MO"], key="WaPo")
monthly_info_MO = arcospy.summarized_county_monthly(state=["MO"], key="WaPo")

county_info_MT = arcospy.county_population(state=["MT"], key="WaPo")
monthly_info_MT = arcospy.summarized_county_monthly(state=["MT"], key="WaPo")

county_info_NE = arcospy.county_population(state=["NE"], key="WaPo")
monthly_info_NE = arcospy.summarized_county_monthly(state=["NE"], key="WaPo")

county_info_NV = arcospy.county_population(state=["NV"], key="WaPo")
monthly_info_NV = arcospy.summarized_county_monthly(state=["NV"], key="WaPo")

county_info_NH = arcospy.county_population(state=["NH"], key="WaPo")
monthly_info_NH = arcospy.summarized_county_monthly(state=["NH"], key="WaPo")

county_info_NJ = arcospy.county_population(state=["NJ"], key="WaPo")
monthly_info_NJ = arcospy.summarized_county_monthly(state=["NJ"], key="WaPo")

county_info_NM = arcospy.county_population(state=["NM"], key="WaPo")
monthly_info_NM = arcospy.summarized_county_monthly(state=["NM"], key="WaPo")

county_info_NY = arcospy.county_population(state=["NY"], key="WaPo")
monthly_info_NY = arcospy.summarized_county_monthly(state=["NY"], key="WaPo")

county_info_NC = arcospy.county_population(state=["NC"], key="WaPo")
monthly_info_NC = arcospy.summarized_county_monthly(state=["NC"], key="WaPo")

county_info_ND = arcospy.county_population(state=["ND"], key="WaPo")
monthly_info_ND = arcospy.summarized_county_monthly(state=["ND"], key="WaPo")

county_info_OH = arcospy.county_population(state=["OH"], key="WaPo")
monthly_info_OH = arcospy.summarized_county_monthly(state=["OH"], key="WaPo")

county_info_OK = arcospy.county_population(state=["OK"], key="WaPo")
monthly_info_OK = arcospy.summarized_county_monthly(state=["OK"], key="WaPo")

county_info_OR = arcospy.county_population(state=["OR"], key="WaPo")
monthly_info_OR = arcospy.summarized_county_monthly(state=["OR"], key="WaPo")

county_info_PA = arcospy.county_population(state=["PA"], key="WaPo")
monthly_info_PA = arcospy.summarized_county_monthly(state=["PA"], key="WaPo")

county_info_RI = arcospy.county_population(state=["RI"], key="WaPo")
monthly_info_RI = arcospy.summarized_county_monthly(state=["RI"], key="WaPo")

county_info_SC = arcospy.county_population(state=["SC"], key="WaPo")
monthly_info_SC = arcospy.summarized_county_monthly(state=["SC"], key="WaPo")

county_info_SD = arcospy.county_population(state=["SD"], key="WaPo")
monthly_info_SD = arcospy.summarized_county_monthly(state=["SD"], key="WaPo")

county_info_TN = arcospy.county_population(state=["TN"], key="WaPo")
monthly_info_TN = arcospy.summarized_county_monthly(state=["TN"], key="WaPo")

county_info_TX = arcospy.county_population(state=["TX"], key="WaPo")
monthly_info_TX = arcospy.summarized_county_monthly(state=["TX"], key="WaPo")

county_info_UT = arcospy.county_population(state=["UT"], key="WaPo")
monthly_info_UT = arcospy.summarized_county_monthly(state=["UT"], key="WaPo")

county_info_VT = arcospy.county_population(state=["VT"], key="WaPo")
monthly_info_VT = arcospy.summarized_county_monthly(state=["VT"], key="WaPo")

county_info_VA = arcospy.county_population(state=["VA"], key="WaPo")
monthly_info_VA = arcospy.summarized_county_monthly(state=["VA"], key="WaPo")

county_info_WA = arcospy.county_population(state=["WA"], key="WaPo")
monthly_info_WA = arcospy.summarized_county_monthly(state=["WA"], key="WaPo")

county_info_WV = arcospy.county_population(state=["WV"], key="WaPo")
monthly_info_WV = arcospy.summarized_county_monthly(state=["WV"], key="WaPo")

county_info_WI = arcospy.county_population(state=["WI"], key="WaPo")
monthly_info_WI = arcospy.summarized_county_monthly(state=["WI"], key="WaPo")

county_info_WY = arcospy.county_population(state=["WY"], key="WaPo")
monthly_info_WY = arcospy.summarized_county_monthly(state=["WY"], key="WaPo")






# Step 1.B

county_info_frames = [county_info_AL,
                      county_info_AK, 
                      county_info_AR,
                      county_info_AZ,
                      county_info_CA,
                      county_info_CO,
                      county_info_CT,
                      county_info_DC,
                      county_info_DE,
                      county_info_FL,
                      county_info_GA,
                      county_info_HI,
                      county_info_IA,
                      county_info_ID,
                      county_info_IL,
                      county_info_IN,
                      county_info_KS,
                      county_info_KY,
                      county_info_LA,
                      county_info_MA,
                      county_info_MD,
                      county_info_ME,
                      county_info_MI,
                      county_info_MN,
                      county_info_MO,
                      county_info_MS,
                      county_info_MT,
                      county_info_NC,
                      county_info_ND,
                      county_info_NE,
                      county_info_NH,
                      county_info_NJ,
                      county_info_NM,
                      county_info_NV,
                      county_info_NY,
                      county_info_OH,
                      county_info_OK,
                      county_info_OR,
                      county_info_PA,
                      county_info_RI,
                      county_info_SC,
                      county_info_SD,
                      county_info_TN,
                      county_info_TX,
                      county_info_UT,
                      county_info_VA,
                      county_info_VT,
                      county_info_WA,
                      county_info_WI,
                      county_info_WV,
                      county_info_WY
                      ]
county_info = pd.concat(county_info_frames)











monthly_info_frames = [monthly_info_AL,
                      monthly_info_AK, 
                      monthly_info_AR,
                      monthly_info_AZ,
                      monthly_info_CA,
                      monthly_info_CO,
                      monthly_info_CT,
                      monthly_info_DC,
                      monthly_info_DE,
                      monthly_info_FL,
                      monthly_info_GA,
                      monthly_info_HI,
                      monthly_info_IA,
                      monthly_info_ID,
                      monthly_info_IL,
                      monthly_info_IN,
                      monthly_info_KS,
                      monthly_info_KY,
                      monthly_info_LA,
                      monthly_info_MA,
                      monthly_info_MD,
                      monthly_info_ME,
                      monthly_info_MI,
                      monthly_info_MN,
                      monthly_info_MO,
                      monthly_info_MS,
                      monthly_info_MT,
                      monthly_info_NC,
                      monthly_info_ND,
                      monthly_info_NE,
                      monthly_info_NH,
                      monthly_info_NJ,
                      monthly_info_NM,
                      monthly_info_NV,
                      monthly_info_NY,
                      monthly_info_OH,
                      monthly_info_OK,
                      monthly_info_OR,
                      monthly_info_PA,
                      monthly_info_RI,
                      monthly_info_SC,
                      monthly_info_SD,
                      monthly_info_TN,
                      monthly_info_TX,
                      monthly_info_UT,
                      monthly_info_VA,
                      monthly_info_VT,
                      monthly_info_WA,
                      monthly_info_WI,
                      monthly_info_WV,
                      monthly_info_WY
                      ]
monthly_info = pd.concat(monthly_info_frames)















# Target pharmaceutical: Purdue Pharma LP

# Step 2: Get the state, county, manufacturer, total dosage units, and total records for every state
    # Step 2.A: Create dataframe for each
    # Step 2.B: Concatenate one on top of the other
    #


manuf_state_AL = arcospy.total_manufacturers_state(state=['AL'], key = 'WaPo')

manuf_state_AL = arcospy.total_manufacturers_state(state=["AL"], key="WaPo")

manuf_state_AK = arcospy.total_manufacturers_state(state=["AK"], key="WaPo")

manuf_state_AR = arcospy.total_manufacturers_state(state=["AR"], key="WaPo")

manuf_state_AZ = arcospy.total_manufacturers_state(state=["AZ"], key="WaPo")

manuf_state_CA = arcospy.total_manufacturers_state(state=["CA"], key="WaPo")

manuf_state_CO = arcospy.total_manufacturers_state(state=["CO"], key="WaPo")

manuf_state_CT = arcospy.total_manufacturers_state(state=["CT"], key="WaPo")

manuf_state_DC = arcospy.total_manufacturers_state(state=["DC"], key="WaPo")

manuf_state_DE = arcospy.total_manufacturers_state(state=["DE"], key="WaPo")

manuf_state_FL = arcospy.total_manufacturers_state(state=["FL"], key="WaPo")

manuf_state_GA = arcospy.total_manufacturers_state(state=["GA"], key="WaPo")

manuf_state_HI = arcospy.total_manufacturers_state(state=["HI"], key="WaPo")

manuf_state_ID = arcospy.total_manufacturers_state(state=["ID"], key="WaPo")

manuf_state_IL = arcospy.total_manufacturers_state(state=["IL"], key="WaPo")

manuf_state_IN = arcospy.total_manufacturers_state(state=["IN"], key="WaPo")

manuf_state_IA = arcospy.total_manufacturers_state(state=["IA"], key="WaPo")

manuf_state_KS = arcospy.total_manufacturers_state(state=["KS"], key="WaPo")

manuf_state_KY = arcospy.total_manufacturers_state(state=["KY"], key="WaPo")

manuf_state_LA = arcospy.total_manufacturers_state(state=["LA"], key="WaPo")

manuf_state_ME = arcospy.total_manufacturers_state(state=["ME"], key="WaPo")

manuf_state_MD = arcospy.total_manufacturers_state(state=["MD"], key="WaPo")

manuf_state_MA = arcospy.total_manufacturers_state(state=["MA"], key="WaPo")

manuf_state_MI = arcospy.total_manufacturers_state(state=["MI"], key="WaPo")

manuf_state_MN = arcospy.total_manufacturers_state(state=["MN"], key="WaPo")

manuf_state_MS = arcospy.total_manufacturers_state(state=["MS"], key="WaPo")

manuf_state_MO = arcospy.total_manufacturers_state(state=["MO"], key="WaPo")

manuf_state_MT = arcospy.total_manufacturers_state(state=["MT"], key="WaPo")

manuf_state_NE = arcospy.total_manufacturers_state(state=["NE"], key="WaPo")

manuf_state_NV = arcospy.total_manufacturers_state(state=["NV"], key="WaPo")

manuf_state_NH = arcospy.total_manufacturers_state(state=["NH"], key="WaPo")

manuf_state_NJ = arcospy.total_manufacturers_state(state=["NJ"], key="WaPo")

manuf_state_NM = arcospy.total_manufacturers_state(state=["NM"], key="WaPo")

manuf_state_NY = arcospy.total_manufacturers_state(state=["NY"], key="WaPo")

manuf_state_NC = arcospy.total_manufacturers_state(state=["NC"], key="WaPo")

manuf_state_ND = arcospy.total_manufacturers_state(state=["ND"], key="WaPo")

manuf_state_OH = arcospy.total_manufacturers_state(state=["OH"], key="WaPo")

manuf_state_OK = arcospy.total_manufacturers_state(state=["OK"], key="WaPo")

manuf_state_OR = arcospy.total_manufacturers_state(state=["OR"], key="WaPo")

manuf_state_PA = arcospy.total_manufacturers_state(state=["PA"], key="WaPo")

manuf_state_RI = arcospy.total_manufacturers_state(state=["RI"], key="WaPo")

manuf_state_SC = arcospy.total_manufacturers_state(state=["SC"], key="WaPo")

manuf_state_SD = arcospy.total_manufacturers_state(state=["SD"], key="WaPo")

manuf_state_TN = arcospy.total_manufacturers_state(state=["TN"], key="WaPo")

manuf_state_TX = arcospy.total_manufacturers_state(state=["TX"], key="WaPo")

manuf_state_UT = arcospy.total_manufacturers_state(state=["UT"], key="WaPo")

manuf_state_VT = arcospy.total_manufacturers_state(state=["VT"], key="WaPo")

manuf_state_VA = arcospy.total_manufacturers_state(state=["VA"], key="WaPo")

manuf_state_WA = arcospy.total_manufacturers_state(state=["WA"], key="WaPo")

manuf_state_WV = arcospy.total_manufacturers_state(state=["WV"], key="WaPo")

manuf_state_WI = arcospy.total_manufacturers_state(state=["WI"], key="WaPo")

manuf_state_WY = arcospy.total_manufacturers_state(state=["WY"], key="WaPo")







manuf_state_frames = [manuf_state_AL,
                      manuf_state_AK, 
                      manuf_state_AR,
                      manuf_state_AZ,
                      manuf_state_CA,
                      manuf_state_CO,
                      manuf_state_CT,
                      manuf_state_DC,
                      manuf_state_DE,
                      manuf_state_FL,
                      manuf_state_GA,
                      manuf_state_HI,
                      manuf_state_IA,
                      manuf_state_ID,
                      manuf_state_IL,
                      manuf_state_IN,
                      manuf_state_KS,
                      manuf_state_KY,
                      manuf_state_LA,
                      manuf_state_MA,
                      manuf_state_MD,
                      manuf_state_ME,
                      manuf_state_MI,
                      manuf_state_MN,
                      manuf_state_MO,
                      manuf_state_MS,
                      manuf_state_MT,
                      manuf_state_NC,
                      manuf_state_ND,
                      manuf_state_NE,
                      manuf_state_NH,
                      manuf_state_NJ,
                      manuf_state_NM,
                      manuf_state_NV,
                      manuf_state_NY,
                      manuf_state_OH,
                      manuf_state_OK,
                      manuf_state_OR,
                      manuf_state_PA,
                      manuf_state_RI,
                      manuf_state_SC,
                      manuf_state_SD,
                      manuf_state_TN,
                      manuf_state_TX,
                      manuf_state_UT,
                      manuf_state_VA,
                      manuf_state_VT,
                      manuf_state_WA,
                      manuf_state_WI,
                      manuf_state_WV,
                      manuf_state_WY
                      ]
manuf_state_info = pd.concat(manuf_state_frames)



# DATAFRAME A: county_info

# DATAFRAME B: monthly_info

# DATAFRAME C: manuf_state_info

county_info.head()
# BUYER_COUNTY	BUYER_STATE	countyfips	STATE	COUNTY	county_name	NAME	variable	year	population
monthly_info.head()
# BUYER_COUNTY	BUYER_STATE	year	month	count	DOSAGE_UNIT	countyfips
manuf_state_info.head()
# buyer_state	buyer_county	combined_labeler_name	total_dosage_unit	total_records


#MERGE A AND B INTO DF1 BY year buyer_state buyer_county
#MERGE DF1 AND C INTO DF2 by 







# 14 million records
DF1 = pd.merge(county_info, monthly_info, left_on='BUYER_COUNTY', right_on='BUYER_COUNTY')
DF1.head()

# DF2 = pd.merge(manuf_state_info, DF1, left_on='buyer_county', right_on='BUYER_COUNTY')
