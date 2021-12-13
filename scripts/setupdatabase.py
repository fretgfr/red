"""
File to run to setup the database.
"""

import mysql.connector as con
import json

with open("./sql/create_schema.sql", "r") as fp: setup_sql = fp.read()
with open('config.json') as config_file:
    config = json.load(config_file)

db_connection = con.connect(**config)

with db_connection.cursor() as cursor:
    cursor.execute(setup_sql, multi=True)
    db_connection.commit()

db_connection.close()