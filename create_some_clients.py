from lib import Client
import json
import mysql.connector as con


with open('config.json') as config_file:
    config = json.load(config_file)

db_connection = con.connect(**config)

Client.create_client(db_connection, 1, "John", "C", "Doe", 586, 2110000, "jcdoe@gmail.com", 1, None)

Client.create_client(db_connection, 2, "Jane", "A", "Doe", 586, 2110001, "janeadoe@gmail.com", 2, None)

Client.create_client(db_connection, 3, "Joe", "B", "Doe", 586, 2110002, "joebdoe@gmail.com", 1, None)

Client.create_client(db_connection, 4, "Jill", "C", "Doe", 586, 2110003, "jillcdoe@gmail.com", 2, None)