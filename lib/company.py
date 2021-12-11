from dataclasses import dataclass
import mysql.connector


@dataclass
class Company():
    """ Represents a company."""    
    company_id: int
    company_hq_street: str
    company_hq_city: str
    company_hq_state: str
    company_hq_zip: int
    company_hq_phone_area: int
    company_hq_phone_number: int
    company_hq_fax_area: int
    company_hq_fax_number: int
    company_license_number: int
    AGENT_license_number: list

    @classmethod
    def from_company_id(cls, company_id: int, db_connection: mysql.connector.MySQLConnection):
        """Retrieves a company from the database by its id.

        Args:
            company_id (int): The id of the company to retrieve.
            db_connection (mysql.connector.MySQLConnection): The database connection to retrieve from.

        Returns:
            Company: The retrieved Company or None if no company was found.
        """        
        with db_connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM COMPANY WHERE company_id = %s", (company_id,))
            company_data = cursor.fetchone()
            try:
                return cls(**company_data)
            except Exception:
                return None
        
    @classmethod
    def create_company(cls, db_connection: mysql.connector.MySQLConnection, company_id: int, hq_street: str, hq_city: str, hq_state: str, hq_zip: int, hq_phone_area: int, hq_phone_number: int, hq_fax_area: int, hq_fax_number: int, license_number: int, agent_ids: list):
        """Creates a company in the database.

        Args:
            db_connection (mysql.connector.MySQLConnection): The database to insert into.
            company_id (int): The id of the company to be created.
            hq_street (str): The street address of the company's headquarters
            hq_city (str): The city of the company's headquarters.
            hq_state (str): The state of the company's headquarters.
            hq_zip (int): The zip code of the company's headquarters.
            hq_phone_area (int): The area code of the company's main phone.
            hq_phone_number (int): The phone number of the company's main phone.
            hq_fax_area (int): The area code of the company's main fax.
            hq_fax_number (int): The phone number of the company's main fax.
            license_number (int): The company's license number
            agent_ids (Optional[list]): The agents that the company employs
        
        Returns:
            Company: The company that was created.
        """
        with db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO COMPANY (`company_id`, `company_hq_street`, `company_hq_city`,`company_hq_state`, `company_hq_zip`, `company_hq_phone_area`, `company_hq_phone_number`,`company_hq_fax_area`, `company_hq_fax_number`,`company_license_number`,`AGENT_license_number`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (company_id, hq_street, hq_city, hq_state, hq_zip, hq_phone_area, hq_phone_number, hq_fax_area, hq_fax_number, license_number, agent_ids))
            db_connection.commit()
        return cls(company_id, hq_street, hq_city, hq_state, hq_zip, hq_phone_area, hq_phone_number, hq_fax_area, hq_fax_number, license_number, agent_ids)
 
    @classmethod
    def get_all_companies(cls, db_connection: mysql.connector.MySQLConnection):
        """Retreives all companies from the database.

        Args:
            db_connection (mysql.connector.MySQLConnection): The database connection to retrieve from.

        Returns:
            List[Company]: The companies that were retrieved
        """
        with db_connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM COMPANY")
            companies = cursor.fetchall()
            return [cls(**company) for company in companies]
    