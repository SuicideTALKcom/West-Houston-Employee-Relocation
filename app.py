from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_homes

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/app"
mongo = PyMongo(app)

listings = mongo.db.listings
# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/app")


@app.route("/")
def index():
    listings = mongo.db.listings.find_one()
    return render_template("index.html", listings=listings)


@app.route("/scrape")
def scraper():
    listings_data = scrape_homes.scrape()
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
