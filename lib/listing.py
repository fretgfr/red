from dataclasses import dataclass
from datetime import date
import mysql.connector
from .helpers import convert_01_yn

@dataclass
class Listing:
    """Represents a listing"""
    listing_mls_number: int
    listing_type: str
    listing_status: str
    listing_description: str #Not in our model but necessary
    listing_sale_yn: bool
    listing_rent_yn: bool
    listing_price: int
    listing_original_price: int
    listing_address_number: int
    listing_address_street: str
    listing_address_city: str
    listing_address_state: str
    listing_address_zip: int
    listing_structure_style: str
    listing_bedroom_count: int
    listing_full_bath_count: int
    listing_half_bath_count: int
    listing_basement_yn: bool
    listing_waterfront_yn: bool
    listing_fireplace_yn: bool
    listing_garage_yn: bool
    listing_pool_yn: bool
    listing_ownership: str
    listing_school_district: str
    listing_garage_car_count: int
    listing_above_grade_sqft: int
    listing_acreage: int
    listing_year_built: int
    listing_date: date
    listing_agent_license_number: int
    listing_colisting_agent_license_number: int
    listing_image_links: str

    @classmethod
    def get_listings_in_zip(cls, db_connection: mysql.connector.MySQLConnection, zip_code: int):
        with db_connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM LISTING WHERE listing_address_zip = %s", (zip_code,))
            listings = cursor.fetchall()
            return [cls(**listing) for listing in listings]

    @classmethod
    def get_all_listings(cls, db_connection: mysql.connector.MySQLConnection):
        with db_connection.cursor(dictionary=True) as cursor:
            listings = []
            cursor.execute("SELECT listing_mls_number FROM LISTING;")
            for listing in cursor.fetchall():
                listings.append(Listing.from_listing_id(listing['listing_mls_number'], db_connection))
            return listings

    @classmethod
    def from_listing_id(cls, id: int, db_connection: mysql.connector.MySQLConnection):
        with db_connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM LISTING WHERE listing_mls_number = %s", (id,))
            listing_data = cursor.fetchone() # Haven't tested yet.
            return cls(**listing_data)

    @classmethod
    def create_listing(cls, db_connection: mysql.connector.MySQLConnection, listing_type: str, status: str, description: str, sale_yn: bool, rent_yn: bool, price: int, address_number: int, address_street: str, address_city: str, address_state: str, address_zip: int, structure_style: str, bedroom_count: int, full_bath_count: int, half_bath_count: int, basement_yn: bool, waterfront_yn: bool, fireplace_yn: bool, garage_yn: bool, pool_yn: bool, ownership: str, school_district: str, garage_car_count: int, above_grade_sqft: int, acreage: int, year_built: int, date_listed: date, agent_license_number: int, colisting_agent_license_number: int, image_link: str):
        with db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO LISTING (listing_type, listing_status, listing_description, listing_sale_yn, listing_rent_yn, listing_price, listing_original_price, listing_address_number, listing_address_street, listing_address_city, listing_address_state, listing_address_zip, listing_structure_style, listing_bedroom_count, listing_full_bath_count, listing_half_bath_count, listing_basement_yn, listing_waterfront_yn, listing_fireplace_yn, listing_garage_yn, listing_pool_yn, listing_ownership, listing_school_district, listing_garage_car_count, listing_above_grade_sqft, listing_acreage, listing_year_built, listing_date, listing_agent_license_number, listing_colisting_agent_license_number, listing_image_links) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (listing_type, status, description, sale_yn, rent_yn, price, price, address_number, address_street, address_city, address_state, address_zip, structure_style, bedroom_count, full_bath_count, half_bath_count, basement_yn, waterfront_yn, fireplace_yn, garage_yn, pool_yn, ownership, school_district, garage_car_count, above_grade_sqft, acreage, year_built, date_listed, agent_license_number, colisting_agent_license_number, image_link))
            mls_number = cursor.lastrowid
            db_connection.commit()
            return cls.from_listing_id(mls_number, db_connection)
           

    def update_listing(self, db_connection: mysql.connector.MySQLConnection):
        with db_connection.cursor() as cursor:
            cursor.execute("UPDATE LISTING SET listing_type = %s, listing_status = %s, listing_description = %s, listing_sale_yn = %s, listing_rent_yn = %s, listing_price = %s, listing_original_price = %s, listing_address_number = %s, listing_address_street = %s, listing_address_city = %s, listing_address_state = %s, listing_address_zip = %s, listing_structure_style = %s, listing_bedroom_count = %s, listing_full_bath_count = %s, listing_half_bath_count = %s, listing_basement_yn = %s, listing_waterfront_yn = %s, listing_fireplace_yn = %s, listing_garage_yn = %s, listing_pool_yn = %s, listing_ownership = %s, listing_school_district = %s, listing_garage_car_count = %s, listing_above_grade_sqft = %s, listing_acreage = %s, listing_year_built = %s, listing_date = %s, listing_agent_license_number = %s, listing_colisting_agent_license_number = %s, listing_image_links = %s WHERE listing_mls_number = %s", (self.listing_type, self.listing_status, self.listing_description, self.listing_sale_yn, self.listing_rent_yn, self.listing_price, self.listing_price, self.listing_address_number, self.listing_address_street, self.listing_address_city, self.listing_address_state, self.listing_address_zip, self.listing_structure_style, self.listing_bedroom_count, self.listing_full_bath_count, self.listing_half_bath_count, self.listing_basement_yn, self.listing_waterfront_yn, self.listing_fireplace_yn, self.listing_garage_yn, self.listing_pool_yn, self.listing_ownership, self.listing_school_district, self.listing_garage_car_count, self.listing_above_grade_sqft, self.listing_acreage, self.listing_year_built, self.listing_date, self.listing_agent_license_number, self.listing_colisting_agent_license_number, self.listing_image_links, self.listing_mls_number))
            db_connection.commit()
        return self

           

    def delete_listing(self, db_connection: mysql.connector.MySQLConnection, mls_number: int):
        #Deletes the listing
        with db_connection.cursor() as cursor:
            cursor.execute("DELETE FROM LISTING WHERE listing_mls_number = %s", (self.listing_mls_number,))
            db_connection.commit()            

    @property
    def sale(self) -> str:
        return convert_01_yn(self.listing_sale_yn)

    @property
    def rent(self) -> str:
        return convert_01_yn(self.listing_rent_yn)
    
    @property
    def basement(self) -> str:
        return convert_01_yn(self.listing_basement_yn)
    
    @property
    def waterfront(self) -> str:
        return convert_01_yn(self.listing_waterfront_yn)
    
    @property
    def fireplace(self) -> str:
        return convert_01_yn(self.listing_fireplace_yn)
    
    @property
    def pool(self) -> str:
        return convert_01_yn(self.listing_pool_yn)
    
    @property
    def garage(self) -> str:
        return convert_01_yn(self.listing_garage_yn)

    @property
    def has_colisting_agent(self) -> bool:
        return self.listing_colisting_agent_license_number != 0

    @property
    def pretty_price(self) -> str:
        return f"${self.listing_price:,}"
    
    @property
    def pretty_original_price(self) -> str:
        return f"${self.listing_original_price:,}"
    
    @property
    def pretty_sqft(self) -> str:
        return f"{self.listing_above_grade_sqft:,}"

    @property
    def str_days_on_market(self) -> str:
        today = date.today()
        delta = today - self.listing_date_listed
        return f"{delta.days}"
