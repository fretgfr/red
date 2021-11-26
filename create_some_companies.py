from lib import Company
import json
import mysql.connector as con


with open('config.json') as config_file:
    config = json.load(config_file)

db_connection = con.connect(**config)

Company.create_company()