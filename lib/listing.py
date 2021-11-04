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
    def from_listing_id(cls, id: int) -> cls:
        """Returns a listing from the database"""
        pass