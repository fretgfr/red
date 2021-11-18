import mysql.connector as con
import json
from datetime import date


with open('config.json') as config_file:
    config = json.load(config_file)

db_connection = con.connect(**config)

with db_connection.cursor(dictionary=True) as cursor:
    cursor.execute("""
        SELECT * FROM LISTING WHERE listing_mls_number = %s;
        """, (1,))
    for item in cursor:
        print(item)
        acreage = float(item['listing_acreage'])
        print(acreage)
        

db_connection.close()