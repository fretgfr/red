from dataclasses import dataclass
import mysql.connector


@dataclass
class Company():
    """ Represents a company that has agents in our model """
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
    company_agent_license_number: list

    @classmethod
    def from_company_id(cls, company_id: int, db_connection: mysql.connector.MySQLConnection):
        #Returns a company object from the database
        with db_connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM COMPANY WHERE company_id = %s", (company_id))
            company_data = cursor.fetchone()
            return cls(**company_data)
        
    @classmethod
    def create_company(cls, db_connection: mysql.connector.MySQLConnection, company_id: int, hq_street: str, hq_city: str, hq_state: str, hq_zip: int, hq_phone_area: int, hq_phone_number: int, hq_fax_area: int, hq_fax_number: int, license_number: int, agent_ids: list):
        #Insert a company
        with db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO COMPANY (`company_id`, `company_hq_street`, `company_hq_city`,`company_hq_state`, `company_hq_zip`, `company_hq_phone_area`, `company_hq_phone_number`,`company_hq_fax_area`, `company_hq_fax_number`,`company_license_number`,`AGENT_license_number`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (company_id, hq_street, hq_city, hq_state, hq_zip, hq_phone_area, hq_phone_number, hq_fax_area, hq_fax_number, license_number, agent_ids))
            db_connection.commit()
 
    