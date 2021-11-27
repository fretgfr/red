from lib import Company
import json
import mysql.connector as con


with open('config.json') as config_file:
    config = json.load(config_file)

db_connection = con.connect(**config)

Company.create_company(db_connection, 1, "123 Main St", "Rochester Hills", "MI", 48309, 586, 5962110, 586, 5962111, 100, None)
Company.create_company(db_connection, 2, "567 South St", "Southfield", "MI", 48311, 586, 5962112, 586, 5962113, 200, None)
Company.create_company(db_connection, 3, "123 North St", "Detroit", "MI", 48311, 586, 5962114, 586, 5962115, 300, None)
Company.create_company(db_connection, 4, "456 East St", "Detroit", "MI", 48311, 586, 5962116, 586, 5962117, 400, None)