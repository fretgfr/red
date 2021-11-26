from lib import Agent
import json
import mysql.connector as con


with open('config.json') as config_file:
    config = json.load(config_file)

db_connection = con.connect(**config)

Agent.create_agent(db_connection, 1, "Joe", "C", "McKenzie", 586, "123456", 586, "123457", "jmckenzie@gmail.com", "50592 Van Dyke Ave", "Shelby Twp", "MI", 48309, 1, None, None)
