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
    image_link: str

    @classmethod
    def from_listing_id(cls, id: int, db_connection: mysql.connector.MySQLConnection):
        with db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM listings WHERE mls_number = %s", (id,))
            listing_data = cursor.fetchone() # Haven't tested yet.
            return cls(**listing_data)

    @classmethod
    def create_listing(cls, db_connection: mysql.connector.MySQLConnection, listing_type: str, status: str, description: str, sale_yn: bool, rent_yn: bool, price: int, address_number: int, address_street: str, address_city: str, address_state: str, address_zip: int, structure_style: str, bedroom_count: int, full_bathroom_count: int, half_bathroom_count: int, basement_yn: bool, waterfront_yn: bool, fireplace_yn: bool, garage_yn: bool, pool_yn: bool, ownership: str, school_district: str, garage_car_count: int, above_grade_sqft: int, acreage: int, year_built: int, date_listed: date, agent_license_number: int, colisting_agent_license_number: int, image_link: str):
        #Creates a listing in the database
        with db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO LISTING"
            "( `listing_mls_number`,`listing_type`,`listing_status`, `listing_description`, `listing_sale_yn`,`listing_rent_yn`,`listing_price`,`listing_original_price`,`listing_address_number`, `listing_address_street`, `listing_address_city`, `listing_address_state`, `listing_address_zip`,`listing_structure_style`,`listing_bedroom_count`, `listing_full_bath_count`, `listing_half_bath_count`,`listing_basement_yn`,`listing_waterfront_yn`,`listing_fireplace_yn`, `listing_garage_yn`, `listing_pool_yn`, `listing_ownership`,`listing_school_district`,`listing_garage_car_count`, `listing_above_grade_sqft`,`listing_acreage`,`listing_year_built`,`listing_date`,`listing_agent_license_number`, `listing_colisting_agent_license_number`, `listing_image_links`)"
            "values", (listing_type, status, description, sale_yn, rent_yn, price, address_number, address_street, address_city, address_state, address_zip, structure_style, bedroom_count, full_bathroom_count, half_bathroom_count, basement_yn, waterfront_yn, fireplace_yn, garage_yn, pool_yn, ownership, school_district, garage_car_count, above_grade_sqft, acreage, year_built, date_listed, agent_license_number, colisting_agent_license_number, image_link))
           

        pass

    def update_in_database(self, db_connection: mysql.connector.MySQLConnection):
        #Updates the listing in the database
        with db_connection.cursor() as cursor:
            cursor.execute("UDPATE LISTING set listing_status = %s where listing_mls_number = %s", (status, mls_number))
           
        pass

    def delete_listing(cls, db_connection: mysql.connector.MySQLConnection):
        #Deletes the listing
        with db_connection.cursor() as cursor:
            cursor.execute("DELETE FROM LISTING WHERE listing_mls_number = %s", (mls_number))
           
        pass

    