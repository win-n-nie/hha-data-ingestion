##section1 
## in this section I will be importing in a .xls file from my local download folder
from lib2to3.pytree import _Results
import pandas as pd
import xlrd


## the following command is utilized to be able to read the file 
df = pd.read_excel('data/dataset.xlsx')
df

xls = xlrd.open_workbook('data/dataset.xlsx', on_demand=True)
xls.sheet_names()

tab1 = pd.read_excel('data/dataset.xlsx', sheet_name='tab1')
tab1

tab2 = pd.read_excel('data/dataset.xlsx', sheet_name='tab2')
tab2

##section 2 
import requests
import json
url = "https://data.cms.gov/data-api/v1/dataset/c8a139ee-9e31-444c-976f-bab6b287b871/data"
apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/c8a139ee-9e31-444c-976f-bab6b287b871/data').json()
apiDataset = apiDataset.json


## SECTION 3
## big query
# requirements
from google.cloud import bigquery
gcp_project = 'homework-361003'
client = bigquery.Client.from_service_account_json('/Users/wendyarias/Downloads/homework-361003-2547d6b22433.json') ## create bigquery client
## query public dataset
query_job = client.query("SELECT * FROM `sdoh_cms_dual_eligible_enrollment.table` LIMIT 100") ## query public dataset
## get results
results = query_job.result() ## get results
## putresults into dataframe
bigquery1 = pd.DataFrame(results.to_dataframe()) ## put results into dataframe

