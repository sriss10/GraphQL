import sqlite3
import pandas as pd

conn=sqlite3.connect('/Users/srish/Desktop/api/server/db.sqlite3')
df=pd.read_csv('/Users/srish/Desktop/api/bank_branches.csv')

df['id']=df.index
df =df[['ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state',
       'bank_name', 'id']]

df.to_sql('app_branch',conn, if_exists='replace', index=False)