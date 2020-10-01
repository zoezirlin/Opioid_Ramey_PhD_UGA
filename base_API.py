# Github for WashPost https://github.com/wpinvestigative/arcos-api
# WashPost ARCOS API: https://arcos-api.ext.nile.works/__swagger__/
# WashPost instructions for download: https://www.washingtonpost.com/national/2019/07/18/how-download-use-dea-pain-pills-database/

# Dataset is 75GB
# This is a dataset of all opioid shipments to every pharmacy in the United States from 2006-2014.
# I would like the dataset in the following format
#   -	Panel dataset by county and monthyears
#   -	Time in month years. The month format should be 2006m1 for January 2006
#   -	Transaction_date is the original transaction date, collapse it into monthyears


# To-Do List
# - Create github repository
# - Set up version control support





import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


pip install arcospy
import arcospy

help(arcospy)

