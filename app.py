"""
Main application file
"""

from flask import Flask, render_template, request, redirect
from datetime import datetime
import json
import subprocess
import platform
import sys
import mysql.connector as con

from lib import Agent, Client, Company, Listing, convert_yn

###############################################################################
####################### Setup MySQL Connection ################################
###############################################################################

# config.json holds the credentials for the database
try:
    with open('config.json') as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    print("Please create a configuration file named `conffig.json` from the template with the information necessary to connect to your database instance.")
    if platform.system() == 'Darwin': # macOS
        subprocess.call(['open', "configtemplate.json"])
    elif platform.system() == "Windows": # windows
        subprocess.call(['notepad.exe', 'configtemplate.json'])
    sys.exit(1)

# Connect to the database

try:
    db_connection = con.connect(**config)
except Exception:
    print("Failed to connect to the database, please check your connection settings and try again.")
    input()
    sys.exit(1)


###############################################################################
############################# Setup Flask #####################################
###############################################################################

# Initialize Flask
app = Flask(__name__)

@app.route("/")
def home():
    """Returns the home page for the application

    Returns:
        str: Rendered html page.
    """
    return render_template("home.html")

@app.route("/agent/<agent_id>")
def agent(agent_id: str):
    """Renders an agents information.
    Uses `Agent.from_license_number` to get the agent's information.
    Uses `Company.from_company_id` to get the agent's company information.

    Args:
        agent_id (str): The id of the agent to be rendered. Will be converted to an integer for the query.

    Returns:
        str: Rendered html page.
    """ 

    try:
        agent_id = int(agent_id)
    except ValueError:
        return "Invalid agent id" # Probaby substitute with a 404 page if time permits

    agent = Agent.from_license_number(agent_id,db_connection)
    company = Company.from_company_id(agent.agent_company_id, db_connection)

    return render_template("agent.html", agent=agent, company=company)

@app.route("/client/<client_id>")
def client(client_id: str):
    """Renders a clients information.
    Uses `Client.from_client_id` to get the client information.

    Args:
        client_id (str): The id of the client to be rendered. Will be converted to an integer for the query.

    Returns:
        str: Rendered html page.
    """    

    try:
        client_id = int(client_id)
    except ValueError:
        return "Invalid client id" #Probaby substitute with a 404 page if time permits.

    client = Client.from_client_id(client_id, db_connection)
    return render_template("client.html", client=client)


@app.route("/company/<company_id>")
def company_view(company_id: str):
    """Renders a companies information.
    Uses `Company.from_company_id` to get the company information.

    Args:
        company_id (str): The id of the company to be rendered. Will be converted to an integer for the query.

    Returns:
        str: Rendered html page.
    """    

    try:
        company_id = int(company_id)
    except ValueError:
        return "Invalid company id" #Probaby substitute with a 404 page if time permits.

    company = Company.from_company_id(company_id, db_connection)

    return render_template("company.html", company=company)



###############################################################################
############################ Listing Pages ####################################
###############################################################################
@app.route("/add_listing", methods=["GET", "POST"])
def add_listing():
    """Presents the form to add a new listing if a GET request is received.
    Creates the listing using `Listing.create_listing`


    Returns:
        str | redirect: Rendered html page or redirect to page of the listing added.
    """    

    if request.method == "POST": #if they're adding a listing
        try:
            req = request.form

            listing_date = datetime.now().date() #listing date is the date they added it

            listing_type = req.get("listing_type")
            status = req.get("status")
            description = req.get("description")
            saleyn = convert_yn(req.get("saleyn"))
            rentyn = convert_yn(req.get("rentyn"))
            price = int(req.get("price"))
            address_number = int(req.get("address_number"))
            address_street = req.get("address_street")
            address_city = req.get("address_city")
            address_state = req.get("address_state")
            address_zip = int(req.get("address_zip"))
            structure_style = req.get("structure_style")
            bedrooms = int(req.get("bedrooms"))
            full_bathrooms = int(req.get("full_bathrooms"))
            half_bathrooms = int(req.get("half_bathrooms"))
            basement_yn = convert_yn(req.get("basementyn"))
            waterfront_yn = convert_yn(req.get("waterfrontyn"))
            fireplace_yn = convert_yn(req.get("fireplaceyn"))
            pool_yn = convert_yn(req.get("poolyn"))
            garage_yn = convert_yn(req.get("garageyn"))
            ownership = req.get("ownership")
            school_district = req.get("school_district")
            car_count = int(req.get("carcount"))
            sqft = int(req.get("sqft"))
            acreage = float(req.get("acreage"))
            year_built = int(req.get("year_built"))
            listing_agent_id = int(req.get("listing_agent_id"))
            colist_agent_id = int(req.get("colist_agent_id")) if req.get("colist_agent_id") != "0" else None
            image_link = req.get("image_link")

            listing = Listing.create_listing(db_connection, listing_type, status, description, saleyn, rentyn, price, address_number, address_street, address_city, address_state, address_zip, structure_style, bedrooms, full_bathrooms, half_bathrooms, basement_yn, waterfront_yn, fireplace_yn, garage_yn, pool_yn, ownership, school_district, car_count, sqft, acreage, year_built, listing_date, listing_agent_id, colist_agent_id, image_link)

            return redirect(f"/listing/{listing.listing_mls_number}")
                
        except ValueError:
            print("Something went wrong here. Most likely in a conversion.")
            return "Something went wrong." # replace with something more useful if time permits.

    return render_template("add_listing.html") #They're just viewing the form

@app.route("/listing/<listing_id>/edit", methods=["GET", "POST"])
def edit_listing(listing_id: str):
    """Presents the form to edit a listing if a GET request is received.
    Parses updated listing data if a POST request is received.

    Uses `Listing.from_mls_number` to get the listing information.
    Uses `Listing.update_listing` to update the listing.

    Args:
        listing_id (str): The id of the listing to be edited. Will be converted to an integer for the query.

    Returns:
        str | redirect: Rendered html page or redirect to page of the listing edited.
    """    
    try:
        listing_id = int(listing_id)
    except ValueError:
        return "Invalid listing id" # Probably replace with something more useful if time permits.

    listing = Listing.from_listing_id(listing_id, db_connection)

    if request.method == "POST":
        try:
            req = request.form

            if convert_yn(req.get("delete")):
                listing.delete_listing(db_connection)
                return "Listing Deleted"

            listing.listing_type = req.get("listing_type")
            listing.listing_status = req.get("status")
            listing.listing_description = req.get("description")
            listing.listing_sale_yn = convert_yn(req.get("saleyn"))
            listing.listing_rent_yn = convert_yn(req.get("rentyn"))
            listing.listing_price = int(req.get("price"))
            listing.listing_address_number = int(req.get("address_number"))
            listing.listing_address_street = req.get("address_street")
            listing.listing_address_city = req.get("address_city")
            listing.listing_address_state = req.get("address_state")
            listing.listing_address_zip = int(req.get("address_zip"))
            listing.listing_structure_style = req.get("structure_style")
            listing.listing_bedroom_count = int(req.get("bedrooms"))
            listing.listing_full_bath_count = int(req.get("full_bathrooms"))
            listing.listing_half_bath_count = int(req.get("half_bathrooms"))
            listing.listing_basement_yn = convert_yn(req.get("basementyn"))
            listing.listing_waterfront_yn = convert_yn(req.get("waterfrontyn"))
            listing.listing_fireplace_yn = convert_yn(req.get("fireplaceyn"))
            listing.listing_pool_yn = convert_yn(req.get("poolyn"))
            listing.listing_garage_yn = convert_yn(req.get("garageyn"))
            listing.listing_ownership = req.get("ownership")
            listing.listing_school_district = req.get("school_district")
            listing.listing_garage_car_count = int(req.get("carcount"))
            listing.listing_above_grade_sqft = int(req.get("sqft"))
            listing.listing_acreage = float(req.get("acreage"))
            listing.listing_year_built = int(req.get("year_built"))
            listing.listing_colisting_agent_license_number = int(req.get("colist_agent_id")) if req.get("colist_agent_id") != "0" else None
            listing.listing_image_links = req.get("image_link")

            listing.update_listing(db_connection)
            
            return redirect(f"/listing/{listing_id}")

        except ValueError:
            print("Something went wrong here. Most likely in a conversion.")
            return "Something went wrong." # Replace with something more useful if time permits.


    return render_template("edit_listing.html", listing=listing)

@app.route("/listing/<listing_id>")
def listing_view(listing_id: str):
    """Renders the template to view a listing's information.
    Uses `Listing.from_mls_number` to get the listing information.
    Uses `Agent.from_license_number` to get the agent information.

    Args:
        listing_id (str): The id of the listing to be viewed. Will be converted to an integer for the query.

    Returns:
        str: Rendered html page.
    """    
    try:
        listing_id = int(listing_id)
    except ValueError:
        return "Invalid listing id" #Probaby substitute with a 404 page if time permits.


    listing = Listing.from_listing_id(listing_id,db_connection)
    agent = Agent.from_license_number(listing.listing_agent_license_number, db_connection)

    return render_template("listing.html", listing=listing, agent=agent)

@app.route("/listing")
def listing_search():
    """Renders the template to search for listings.
    Uses `Listing.get_all_listings` to get all listings.
    Uses `Listing.get_listings_in_zip` to get listings in a specific zip code.

    Returns:
        str: Rendered html page.
    """    
    listings = Listing.get_all_listings(db_connection)

    zip_code = request.args.get('listing_address_zip')
    if zip_code:
        try:
            zip_code = int(zip_code)
        except ValueError:
            return "Invalid zip code"
        listings = Listing.get_listings_in_zip(db_connection, zip_code)

    return render_template("listing_search.html", listings=listings)

@app.route("/all_agents")
def all_agents():
    """Displays all agents in the database.
    Uses `Agent.get_all_agents` to get all agents.

    Returns:
        str: Rendered html page.
    """
    agents = Agent.get_all_agents(db_connection)

    return render_template("all_agents.html", agents=agents)

@app.route("/all_companies")
def all_companies():
    """Displays all companies in the database.
    Uses `Company.get_all_companies` to get all companies.

    Returns:
        str: Rendered html page.
    """

    companies = Company.get_all_companies(db_connection)

    return render_template("all_companies.html", companies=companies)

@app.route("/all_clients")
def all_clients():
    """Displays all clients in the database.
    Uses `Client.get_all_clients` to get all clients.

    Returns:
        str: Rendered html page.
    """    

    clients = Client.get_all_clients(db_connection)

    return render_template("all_clients.html", clients=clients)

###############################################################################
################################### Run #######################################
###############################################################################
if __name__ == "__main__":
    try:
        app.run()
    except Exception as e:
        print(e)
    finally:
        db_connection.close() # Cleanup database connection on app termination.

