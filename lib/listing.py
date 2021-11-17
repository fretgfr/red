from dataclasses import dataclass
from datetime import date
import mysql.connector

@dataclass
class Listing:
    """Represents a listing"""
    mls_number: int
    listing_type: str
    status: str
    description: str #Not in our model but necessary
    sale_yn: bool
    rent_yn: bool
    price: int
    original_price: int
    address_number: int
    address_street: str
    address_city: str
    address_state: str
    address_zip: int
    structure_style: str
    bedroom_count: int
    full_bathroom_count: int
    half_bathroom_count: int
    basement_yn: bool
    waterfront_yn: bool
    fireplace_yn: bool
    garage_yn: bool
    pool_yn: bool
    ownership: str
    school_district: str
    garage_car_count: int
    above_grade_sqft: int
    acreage: int
    year_built: int
    date_listed: date
    agent_license_number: int
    colisting_agent_license_number: int
    image_links: str

    @classmethod
    def from_listing_id(cls, id: int, db_connection: mysql.connector.MySQLConnection):
        with db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM listings WHERE mls_number = %s", (id,))
            listing_data = cursor.fetchone() # Haven't tested yet.
            return cls(**listing_data)

    @classmethod
    def create_listing(cls, db_connection: mysql.connector.MySQLConnection, listing_type: str, status: str, description: str, sale_yn: bool, rent_yn: bool, price: int, address_number: int, address_street: str, address_city: str, address_state: str, address_zip: int, structure_style: str, bedroom_count: int, full_bathroom_count: int, half_bathroom_count: int, basement_yn: bool, waterfront_yn: bool, fireplace_yn: bool, garage_yn: bool, pool_yn: bool, ownership: str, school_district: str, garage_car_count: int, above_grade_sqft: int, acreage: int, year_built: int, date_listed: date, agent_license_number: int, colisting_agent_license_number: int, image_link: str):
        #Creates a listing in the database
        pass
           

    def update_status_in_database(self, db_connection: mysql.connector.MySQLConnection, mls_number: int):
        #Updates the listing in the database, should update all of the fields except original price and listing date.
        with db_connection.cursor() as cursor:
            cursor.execute("UDPATE LISTING set listing_status = %s where listing_mls_number = %s", (mls_number,))
           
        pass

    def delete_listing(cls, db_connection: mysql.connector.MySQLConnection, mls_number: int):
        #Deletes the listing
        with db_connection.cursor() as cursor:
            cursor.execute("DELETE FROM LISTING WHERE listing_mls_number = %s", (mls_number))
           
        pass

    