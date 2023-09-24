import pandas as pd
import numpy as np
import sqlite3 as sql
import datetime
import csv
import json
import os



# something 



# retrieve from database 
table_name="HelloInputs"
con = sql.connect(f"InputData.db")
df=pd.read_sql_query(f'SELECT * FROM {table_name}', con)  # because stored var as text, it does not save the decimal positions and leads to int. 
con.close()

# some calculation 
# print(df)
constant=100    # some constant for calcs.
df["Units"]=0   # some new var to be populated.     
# dict_FE={}      # store data in dict.

# add some loop 
for customer in list(df["Client"].unique()):
    print(customer)
    # create units var.
    purchase_val=df.loc[df["Client"]==customer, "Purchase"]
    units_val=purchase_val*constant
    df.loc[df["Client"]==customer, "Units"]=units_val

# save to database 
def save_table_to_database(df, database_name, table_name):
    conn = sql.connect(f"{database_name}")  # Portfolio_Complex - trades sorted by close_datetime. 
    cur = conn.cursor()
    # Save trades table as a datatable
    df.to_sql( table_name, conn, if_exists= 'replace' ) # create a trades table for current trader
    conn.close()

save_table_to_database(df=df, database_name="OutputData.db", table_name="HelloOutputs")

####################
print("\n>>> FE Complete")




