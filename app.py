from flask import Flask, render_template, url_for
import os
from lib import Agent, Client, Company, Listing


app = Flask(__name__)

@app.route("/")
def home():
    return "Home page"

@app.route("/listing/<listing_id>")
def listing_view(listing_id: str):
    """Renders the template for a listing

    Args:
        listing_id (int): The listing to render

    Returns:
        rendered html template
    """



    kwargs = {
        "description": "Test Desc",
        "images": [f"/static/{listing_id}/images/{item}" for item in os.listdir(f"./static/{listing_id}/images")]
    }

    # temporary variables above
    return render_template("listing.html", **kwargs)

@app.route("/agent/<agent_id>")
def agent(agent_id):
    """Renders the template for an agent

    Args:
        agent_id (int): the agent to render for

    Returns:
        rendered html template
    """

    kwargs = {
        "name": "Robert"
    }
    return render_template("agent.html", **kwargs)

if __name__ == "__main__":
    app.run()
