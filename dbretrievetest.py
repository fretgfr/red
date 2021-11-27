import mysql.connector as con
import json


with open('config.json') as config_file:
    config = json.load(config_file)

db_connection = con.connect(**config)

with db_connection.cursor() as cursor:
    cursor.execute("SELECT * from CLIENT")
    for item in cursor:
        print(item)

db_connection.close()