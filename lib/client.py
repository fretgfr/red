from dataclasses import dataclass
import mysql.connector


@dataclass
class Client():
    """ Represents a client in our model who has an agent and views listings """
    client_id: int
    first_name: str
    middle_initial: str
    last_name: str
    phone_area_code: int
    phone_number: int
    email_address: str
    agent_license_number: int
    listing_mls_numbers: list

    @classmethod
    def from_client_id(cls, client_id: int, db_connection: mysql.connector.MySQLConnection):
        #Returns a client from the database
         with db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM CLIENT WHERE client_id = %s", (client_id))
            client_data = cursor.fetchone()
            return cls(**client_data)
        pass


@classmethod
    def create_client(cls, client_id: int, db_connection: mysql.connector.MySQLConnection, client_id: int, first_name: str, middle_initial: str, last_name: str, phone_area_code: int, phone_number: int, email_address: str, agent_license_number: int, listing_mls_numbers: list):
        #Creates a client in database
         with db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO CLIENT "
            "(`client_id`, `client_first_name`, `client_middle_initial`, `client_last_name`,`client_area_code`, `client_phone_number`, `client_email_address`, `client_agent_license_number`) "
            "values (%s, %s, %s, %s, %s, %s, %s, %s, %s,)", (client_id, first_name, middle_initial, last_name, phone_area_code, phone_number, email_address, agent_license_number, listing_mls_numbers))
            
        pass

 @classmethod
    def delete_client(cls, client_id: int, db_connection: mysql.connector.MySQLConnection):
        #Delete a client from the database
         with db_connection.cursor() as cursor:
            cursor.execute("DELETE FROM CLIENT WHERE client_id = %s", (client_id))
            client_data = cursor.fetchone()
            return cls(**client_data)
        pass