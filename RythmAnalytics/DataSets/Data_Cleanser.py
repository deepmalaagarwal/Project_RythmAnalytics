# ### CSV Clean-Up Code


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "DataSets/albums.csv"

# Read Purchasing File and store into Pandas data frame
albums_data = pd.read_csv(file_to_load)

#Get an idea for what the data looks like 
albums_data.head()

albums_data['album_title'] = albums_data['album_title'].apply(lambda x: ''.join([" " if ord(i) < 32 or ord(i) > 126 else i for i in x]))
albums_data.head(500)

albums_data.to_csv('file2.csv', index=False)


# File to Load (Remember to Change These)
file_to_load2 = "DataSets/billboard_lyrics.csv"

# Read Purchasing File and store into Pandas data frame
billboard_lyrics_data = pd.read_csv(file_to_load2, encoding = "ISO-8859-1")

#Get an idea for what the data looks like 
billboard_lyrics_data.head(500)
billboard_lyrics_data.to_csv('cleaned_billboard_lyrics.csv', index=False)

import os 
import pandas as pd 
import numpy as np
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
rds_connection_string = "RythmAnalytics/RythmAnalytics.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///RythmAnalytics/RythmAnalytics.sqlite"
engine = create_engine(f'sqlite:///{rds_connection_string}')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
db = SQLAlchemy(app)

#albums 
# File to Load (Remember to Change These)
file_to_load = "RythmAnalytics/DataSets/clean_albums.csv"
billboard_lyrics_data = pd.read_csv("RythmAnalytics/DataSets/cleaned_billboard_lyrics.csv")
# # Read Purchasing File and store into Pandas data frame
albums_data = pd.read_csv(file_to_load)

# # Create table for Sales analysis of albums
albums_data.to_sql(name="db_albums", con=engine,if_exists = 'replace',index=False)
# # Create table for Lyrics analysis of albums
billboard_lyrics_data.to_sql(name="db_lyrics", con=engine,if_exists = 'replace',index=False)
# # pd.read_sql_query('SELECT * FROM "db_lyrics"', con=engine)

