from dataclasses import dataclass
import mysql.connector


@dataclass
class Company():
    """ Represents a company that has agents in our model """
    company_id: int
    hq_street: str
    hq_city: str
    hq_state: str
    hq_zip: int
    hq_phone_area: int
    hq_phone_number: int
    hq_fax_area: int
    hq_fax_number: int
    license_number: int
    agent_ids: list

    @classmethod
    def from_company_id(cls, company_id: int, cnx: mysql.connector.MySQLConnection):
        """Returns a company object from the database"""
        pass