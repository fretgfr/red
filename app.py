from flask import Flask, render_template, url_for, request, redirect
import os
from datetime import datetime, date
import json
import mysql.connector as con

from lib import Agent, Client, Company, Listing, convert_yn

###############################################################################
####################### Setup MySQL Connection ################################
###############################################################################
with open('config.json') as config_file:
    config = json.load(config_file)

db_connection = con.connect(**config)


###############################################################################
############################# Setup Flask #####################################
###############################################################################
app = Flask(__name__)


@app.route("/")
def home():
    return "Home page"

@app.route("/agent/<agent_id>")
def agent(agent_id):
    """Renders the template for an agent

    Args:
        agent_id (str): the agent to render for

    Returns:
        rendered html template
    """

    try:
        agent_id = int(agent_id)
    except ValueError:
        return "Invalid agent id" #Probaby substitute with a 404 page

    agent = Agent.from_license_number(agent_id)
    company = Company.from_company_id(agent.company_id)

    return render_template("agent.html", agent=agent, company=company)

@app.route("/client/<client_id>")
def client(client_id: str):
    """Renders the template for a client

    Args:
        client_id (str): the client to render for

    Returns:
        rendered html template
    """

    try:
        client_id = int(client_id)
    except ValueError:
        return "Invalid client id" #Probaby substitute with a 404 page

    client = Client.from_client_id(client_id)
    return render_template("client.html", client=client)


#Maybe we need a company search page too?
@app.route("/company/<company_id>")
def company_view(company_id: str):
    """Renders the template for a company

    Args:
        company_id (str): the company to render for

    Returns:
        rendered html template
    """

    try:
        company_id = int(company_id)
    except ValueError:
        return "Invalid company id" #Probaby substitute with a 404 page

    company = Company.from_company_id(company_id)

    return render_template("company.html", company=company) #TODO doesn't exist yet



###############################################################################
############################ Listing Pages ####################################
###############################################################################
@app.route("/add_listing", methods=["GET", "POST"])
def add_listing():
    """Renders the template to add a listing

    Returns:
    rendered html template
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
            pool_yn = convert_yn(req.get("poolyn"))
            garage_yn = convert_yn(req.get("garageyn"))
            ownership = req.get("ownership")
            school_district = req.get("school_district")
            car_count = float(req.get("carcount"))
            sqft = int(req.get("sqft"))
            acreage = float(req.get("acreage"))
            year_built = int(req.get("year_built"))
            colist_agent_id = req.get("colist_agent_id")

            with db_connection.cursor() as cursor:
                cursor.execute(
                    """SQL GOES HERE
                    AND HERE
                    """
                )
                db_connection.commit()
                
        except ValueError:
            print("Something went wrong here. Most likely in a conversion.")
            return False


        return "Operation Successful" #Ideally this should take them to the page for the created listing

    return render_template("add_listing.html") #They're just viewing the form

@app.route("/listing/<listing_id>/edit", methods=["GET", "POST"])
def edit_listing(listing_id: str):

    if request.method == "POST":
        #Code to update the listing goes here
        return "Operation Successful"

    listing = Listing.from_listing_id(listing_id)

    return render_template("edit_listing.html", listing=listing)

@app.route("/listing/<listing_id>")
def listing_view(listing_id: str):
    """Renders the template for a listing

    Args:
        listing_id (str): The listing to render

    Returns:
        rendered html template
    """
    try:
        listing_id = int(listing_id)
    except ValueError:
        return "Invalid listing id" #Probaby substitute with a 404 page


    listing = Listing.from_listing_id(listing_id)
    agent = Agent.from_license_number(listing.agent_license_number)

    return render_template("listing.html", listing=listing, agent=agent)

@app.route("/listing")
def listing_search():
    """Renders the template to search for listings

    Returns:
        rendered html template
    """

    return render_template("listing_search.html")

###############################################################################
################################### Run #######################################
###############################################################################
if __name__ == "__main__":
    try:
        app.run()
    except Exception as e:
        print(e)
    finally:
        db_connection.close()

