# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Import dependencies for SQAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask dependencies
from flask import Flask,jsonify

# Set up/acess the Database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect databese into classes
Base = automap_base()

# Reflect tables into SQLAlchemy
Base.prepare(engine, reflect=True)

# Save references to each table and create a variable for each of the classes 
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session link from Python to database
session = Session(engine)

# Set up Flask
app = Flask(__name__)

# Create Flask Routes
# Add routing information for each of the other routes
# add the precipitation, stations, tobs, and temp routes that we'll need for this module into our return statement and use f-strings to display them for our investors
# ROUTE 1
# Create a welcome route
# Create route
@app.route("/api/v1.0/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
# Run the flask run command in command prompt and copy link into browser

#ROUTE 2
# Precipitation Route
# create route
@app.route("/api/v1.0/precipitation")

# Create precipitation() function 
# Add code to calculate date one year from recent date
# Format results into a JSON structured file
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
       filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
# End current session in command prompt, Run the flask run command in command prompt and copy link into browser with end of route code in quotes at end of link

# ROUTE 3
# Stations Route
# Define route and route name
@app.route("/api/v1.0/stations")

# Create a new function for stations()
# Unravel results with one-dimensional array using functional np.ravel() with results as parameter
# Convert results to list using list function and jsonify the list and return it as JSON
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
# End current session in command prompt, Run the flask run command in command prompt and copy link into browser with end of route code in quotes at end of link

# ROUTE 4
# Monthly Temperature Route
# Create temperature observation route
@app.route("/api/v1.0/tobs")

# Create function temp_monthly()
# Calculate the date one year ago from the last date in the database
# Query the primary station for all the temperature observations from the previous year
# Unravel the results into a one-dimensional array and convert that array into a list
# jsonify the list and return our results
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
# End current session in command prompt, Run the flask run command in command prompt and copy link of web address into browser with end of route code in quotes at end of link





