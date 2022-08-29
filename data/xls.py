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