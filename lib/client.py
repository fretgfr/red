from dataclasses import dataclass
import mysql.connector


@dataclass
class Client():
    """ Represents a client in our model who has an agent and views listings """
    client_id: int
    client_first_name: str
    client_middle_initial: str
    client_last_name: str
    client_area_code: int
    client_phone_number: int
    client_email_address: str
    client_agent_license_number: int
    LISTING_mls_number: int

    @classmethod
    def from_client_id(cls, client_id: int, db_connection: mysql.connector.MySQLConnection):
        """Returns a client from the database by their id.

        Args:
            client_id (int): The id to search for.
            db_connection (mysql.connector.MySQLConnection): The database to search in.

        Returns:
            Client: The found Client or None if an invalid id is given.
        """
        with db_connection.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM CLIENT WHERE client_id = %s", (client_id, ))
                client_data = cursor.fetchone()
                return cls(**client_data)
            except Exception:
                return None


    @classmethod
    def create_client(cls, db_connection: mysql.connector.MySQLConnection, client_id: int, first_name: str, middle_initial: str, last_name: str, phone_area_code: int, phone_number: int, email_address: str, agent_license_number: int, listing_mls_number: int):
        """Creates a Client in the database.

        Args:
            db_connection (mysql.connector.MySQLConnection): The database to operate on.
            client_id (int): The Client's id.
            first_name (str): The Client's first name.
            middle_initial (str): The Client's middle initial.
            last_name (str): The Client's last name.
            phone_area_code (int): The Client's phone area code.
            phone_number (int): The Client's phone number.
            email_address (str): The Client's email address
            agent_license_number (int): The license number of the Client's agent.
            listing_mls_number (int): The Listings the Client is interested in.

        Returns:
            Client: The created Client.
        """
        with db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO CLIENT (`client_id`, `client_first_name`, `client_middle_initial`, `client_last_name`,`client_area_code`, `client_phone_number`, `client_email_address`, `client_agent_license_number`, `LISTING_mls_number`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (client_id, first_name, middle_initial, last_name, phone_area_code, phone_number, email_address, agent_license_number, listing_mls_number))
            db_connection.commit()
        return cls(client_id, first_name, middle_initial, last_name, phone_area_code, phone_number, email_address, agent_license_number, listing_mls_number)
            

    @classmethod
    def delete_client(cls, client_id: int, db_connection: mysql.connector.MySQLConnection):
        """Delete's a Client from the database.

        Args:
            client_id (int): The id of the Client to remove.
            db_connection (mysql.connector.MySQLConnection): The database to operate on.
        """
        with db_connection.cursor() as cursor:
            cursor.execute("DELETE FROM CLIENT WHERE client_id = %s", (client_id,))
            db_connection.commit()

    @classmethod
    def get_all_clients(cls, db_connection: mysql.connector.MySQLConnection):
        """Retrieves all Clients from the database.

        Args:
            db_connection (mysql.connector.MySQLConnection): The database to operate on.

        Returns:
            List[Client]: The retrieved Clients.
        """
        with db_connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM CLIENT")
            clients = cursor.fetchall()
            return [cls(**client) for client in clients]