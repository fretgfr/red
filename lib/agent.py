from dataclasses import dataclass

@dataclass
class Agent():
    """Represents an agent in our model who has clients and adds listings to the database"""
    license_number: int
    first_name: str
    middle_initial: str
    last_name: str
    office_area_code: int
    office_phone_number: int
    cell_area_code: int
    cell_phone_number: int
    email_address: str
    office_street_address: str
    office_city: str
    office_state: str
    office_zip_code: int
    company_id: int
    client_ids: list
    listing_ids: list

    @classmethod
    def from_license_number(cls, license_number: int) -> cls:
        """Returns an agent from the database based on their license number"""
        pass
    