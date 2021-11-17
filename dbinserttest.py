import mysql.connector as con
import json
from datetime import date


with open('config.json') as config_file:
    config = json.load(config_file)

db_connection = con.connect(**config)

with db_connection.cursor() as cursor:
    results = cursor.execute("""
        INSERT INTO LISTING (listing_type, listing_status, listing_description, listing_sale_yn, listing_rent_yn, listing_price, listing_original_price, listing_address_number, listing_address_street, listing_address_city, listing_address_state, listing_address_zip, listing_structure_style, listing_bedroom_count, listing_full_bath_count, listing_half_bath_count, listing_basement_yn, listing_waterfront_yn, listing_fireplace_yn, listing_garage_yn, listing_pool_yn, listing_ownership, listing_school_district, listing_garage_car_count, listing_above_grade_sqft, listing_acreage, listing_year_built, listing_date, listing_agent_license_number, listing_colisting_agent_license_number, listing_image_links)
        VALUES ("Single Family", "Active", "A BEAUTIFUL HOUSE", 1, 0, 150000, 150000, 123, "Main St", "Rochester Hills", "MI", 48309, "Ranch", 3, 1, 1, 1, 0, 1, 1, 0, "Private", "Rochester Public Schools", 2, 1390, .25, 2010, %s, 1, 1, "https://google.com")""", (date.today(), ))
    db_connection.commit()
    new_listing_id = cursor.lastrowid #gets the id for the entry that was just inserted.
    print(new_listing_id)

db_connection.close()