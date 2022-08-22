#import packages
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.types import String
engine=create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/demo_db", pool_recycle=-1)
db_engine=engine.connect()
print('engine created successfully')
#use pandas to read the csv
df=pd.read_csv('item_list.csv')
df.head()
print(df.head())

#insert dataframe to postgres table
df.to_sql('store_item', engine,if_exists='append',index=False, dtype={"item_id": String(),"item_name":String(),"quantity":String(),"cost_price":String(),"selling_price":String()})
print("inserted successful to database table")