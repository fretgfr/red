from dataclasses import dataclass
import mysql.connector

@dataclass
class Agent():
    """Represents an agent in our model who has clients and adds listings to the database"""
    agent_license_number: int
    agent_first_name: str
    agent_middle_initial: str
    agent_last_name: str
    agent_office_area_code: int
    agent_office_phone_number: int
    agent_mobile_area_code: int
    agent_mobile_phone_number: int
    agent_email_address: str
    agent_office_street: str
    agent_office_city: str
    agent_office_state: str
    agent_office_zip: int
    agent_company_id: int
    agent_client_ids: list
    agent_listing_ids: list

    @classmethod
    def from_license_number(cls, license_number: int, db_connection: mysql.connector.MySQLConnection):
        #Returns an agent from the database based on their license number
         with db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM AGENT WHERE agent_license_number = %s", (license_number,))
            agent_data = cursor.fetchone()
            return cls(**agent_data)

    @classmethod
    def create_agent(cls, db_connection: mysql.connector.MySQLConnection,  license_number: int, first_name: str, middle_initial: str, last_name: str, office_area_code: int, office_phone_number: int, cell_area_code: int, cell_phone_number: int, email_address: str, office_street_address: str, office_city: str, office_state: str, office_zip_code: int, company_id: int, client_ids: list, listing_ids: list):
        #Creates a listing in the database
        with db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO AGENT " 
            "(`agent_license_number`, `agent_first_name`, `agent_middle_initial`,`agent_last_name`, `agent_office_area_code`, `agent_office_phone_number`, `agent_mobile_area_code`,`agent_mobile_phone_number`, `agent_email_address`, `agent_office_street`, `agent_office_city`,`agent_office_state`, `agent_office_zip`, `agent_company_id`, `CLIENT_id`, `LISTING_mls_number`) "
            "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)", (license_number, first_name, middle_initial,last_name, office_area_code, office_phone_number, cell_area_code, cell_phone_number, email_address, office_street_address, office_city, office_state, office_zip_code, company_id, client_ids, listing_ids))

        pass

    @classmethod
    def delete_agent(cls, license_number: int, db_connection: mysql.connector.MySQLConnection):
        #Deletes agent
         with db_connection.cursor() as cursor:
            cursor.execute("DELETE FROM AGENT WHERE license_number = %s", (license_number,))
            agent_data = cursor.fetchone()
            return cls(**agent_data)
        