import os, pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Database Setup
#################################################
from flask_sqlalchemy import SQLAlchemy
rds_connection_string = "db/RythmAnalytics.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/RythmAnalytics.sqlite"
engine = create_engine(f'sqlite:///{rds_connection_string}')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(‘DATABASE_URL’, ‘’)
db = SQLAlchemy(app)
#albums
# File to Load (Remember to Change These)
file_to_load = "DataSets/artists.csv"
# Read Purchasing File and store into Pandas data frame
artists_data = pd.read_csv(file_to_load)
# from .models import Pet
artists_data.to_sql(name="db_artists", con=engine,if_exists = 'replace',index=False)
pd.read_sql_query('SELECT * FROM “db_albums"', con=engine).head()
