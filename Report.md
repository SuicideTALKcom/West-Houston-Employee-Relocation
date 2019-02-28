# West Houston Homes for Sale

## Data Sources

SQL Database: zipcodes_2011.sql
Flat file: zipcodesWH.csv
Web-scraped: Har.com, SQLzipcodes.ipynb

## Detailing the process of the extraction, transformation, and loading steps

We built a query to pull from the sql database the zip-codes specifically in the West Houston, pulled home listings from har.com filtering out homes not included in the zip-code list and pushed to csv file.


## What data sources you chose, and why

We started off pulling data from zillow.com but we ran into roadblocks with scraping their website as it was loading a captcha screen when running the url. We learned there are terms on the zillow site We pivoted and changed our source to har.com and pulling the data was much easier. 


## Explication why you have performed the types of transformations you did

We needed to standardize the information to make the data homogeneous. 


## Why you chose the type of the final database

The database was structured because the data sources were organized homogeneous. 


## Schema of the tables/collections in the final database

The organization of the data includes the street address and indexed on the zip-code of the home listings that were pulled from har.com. 

## Hypothetical use cases for your database

Employee re-location looking for homes for sale in the West Houston location. 
