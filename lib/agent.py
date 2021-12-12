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
    CLIENT_id: int
    LISTING_mls_number: int

    @classmethod
    def from_license_number(cls, license_number: int, db_connection: mysql.connector.MySQLConnection):
        """Retrieves an Agent from the database using their license number.

        Args:
            license_number (int): The license number to search for.
            db_connection (mysql.connector.MySQLConnection): The database to operate on.

        Returns:
            Agent: The found Agent or None if an invalid license number was passed.
        """
        with db_connection.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM AGENT WHERE agent_license_number = %s", (license_number,))
                agent_data = cursor.fetchone()
                return cls(**agent_data)
            except Exception:
                return None

    @classmethod
    def create_agent(cls, db_connection: mysql.connector.MySQLConnection,  license_number: int, first_name: str, middle_initial: str, last_name: str, office_area_code: int, office_phone_number: int, cell_area_code: int, cell_phone_number: int, email_address: str, office_street_address: str, office_city: str, office_state: str, office_zip_code: int, company_id: int, client_ids: list, listing_ids: list):
        """Creates a agent in the database.

        Args:
            db_connection (mysql.connector.MySQLConnection): The database to operate on.
            license_number (int): The license number of the agent.
            first_name (str): The first name of the agent.
            middle_initial (str): The middle initial of the agent.
            last_name (str): The last name of the agent.
            office_area_code (int): The agents office phone number area code.
            office_phone_number (int): The agents office phone number.
            cell_area_code (int): The agents cell phone area code.
            cell_phone_number (int): The agents cell phone number.
            email_address (str): The agents email address.
            office_street_address (str): The agents office street address.
            office_city (str): The agents office address city.
            office_state (str): The agents office address state.
            office_zip_code (int): The agents office address zip code.
            company_id (int): The id of the Company the agent works for.
            client_ids (list): The ids of the Clients the agent has.
            listing_ids (list): The ids of the Listings the agent has.

        Returns:
            Agent: The created Agent.
        """
        with db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO AGENT (`agent_license_number`, `agent_first_name`, `agent_middle_initial`,`agent_last_name`, `agent_office_area_code`, `agent_office_phone_number`, `agent_mobile_area_code`,`agent_mobile_phone_number`, `agent_email_address`, `agent_office_street`, `agent_office_city`,`agent_office_state`, `agent_office_zip`, `agent_company_id`, `CLIENT_id`, `LISTING_mls_number`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (license_number, first_name, middle_initial,last_name, office_area_code, office_phone_number, cell_area_code, cell_phone_number, email_address, office_street_address, office_city, office_state, office_zip_code, company_id, client_ids, listing_ids))
            db_connection.commit()
        return cls(license_number, first_name, middle_initial, last_name, office_area_code, office_phone_number, cell_area_code, cell_phone_number, email_address, office_street_address, office_city, office_state, office_zip_code, company_id, client_ids, listing_ids)


    @classmethod
    def delete_agent(cls, license_number: int, db_connection: mysql.connector.MySQLConnection):
        """Deletes an Agent from the database using their license number.

        Args:
            license_number (int): The license number to remove.
            db_connection (mysql.connector.MySQLConnection): The database to operate on.
        """
        with db_connection.cursor() as cursor:
            cursor.execute("DELETE FROM AGENT WHERE license_number = %s", (license_number,))
            db_connection.commit()

        
    @classmethod
    def get_all_agents(cls, db_connection: mysql.connector.MySQLConnection):
        """Returns all Agents from the database.

        Args:
            db_connection (mysql.connector.MySQLConnection): The database to operate on.

        Returns:
            List[Agent]: The Agents retrieved from the database.
        """
        with db_connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM AGENT")
            agents = cursor.fetchall()
            return [cls(**agent) for agent in agents]