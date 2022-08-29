##section1 
import pandas as pd
import xlrd

df = pd.read_excel('data/dataset.xlsx')
df
xls = xlrd.open_workbook('data/dataset.xlsx', on_demand=True)
xls.sheet_names()

tab1 = pd.read_excel('data/dataset.xlsx', sheet_name='tab1')
tab1

tab2 = pd.read_excel('data/dataset.xlsx', sheet_name='tab2')
tab2

##section 2 ##
import requests
import json
url = "https://data.cms.gov/data-api/v1/dataset/c8a139ee-9e31-444c-976f-bab6b287b871/data"
apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/c8a139ee-9e31-444c-976f-bab6b287b871/data')
apiDataset = apiDataset.json
