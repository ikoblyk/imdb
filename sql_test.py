from sqlalchemy import create_engine
import pymysql
import pandas as pd
from pprint import pprint
import mysql.connector
from imdb_ver2 import df_concat
import sqlalchemy

tableName = "imdb"

sqlEngine = create_engine('mysql+pymysql://ivan:Cherikcr7!@localhost/mydatabase', pool_recycle=3600)

dbConnection = sqlEngine.connect()

try:

  frame = df_concat.to_sql(tableName, dbConnection, if_exists='fail')

except ValueError as vx:

  print(vx)

except Exception as ex:

  print(ex)

else:

  print("Table %s created successfully." % tableName)

finally:

  dbConnection.close()