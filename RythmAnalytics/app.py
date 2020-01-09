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
rds_connection_string = "db/RythmAnalytics.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/RythmAnalytics.sqlite"
engine = create_engine(f'sqlite:///{rds_connection_string}')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
db = SQLAlchemy(app)

#albums 
# File to Load (Remember to Change These)
file_to_load = "DataSets/clean_albums.csv"

# Read Purchasing File and store into Pandas data frame
albums_data = pd.read_csv(file_to_load)
billboard_lyrics_data = pd.read_csv("DataSets/cleaned_billboard_lyrics.csv")


# from .models import Pet
albums_data.to_sql(name="db_albums", con=engine,if_exists = 'replace',index=False)


# Create table for Sales analysis of albums
albums_data.to_sql(name="db_albums", con=engine,if_exists = 'replace',index=False)
# Create table for Lyrics analysis of albums
billboard_lyrics_data.to_sql(name="db_lyrics", con=engine,if_exists = 'replace',index=False)
# pd.read_sql_query('SELECT * FROM "db_lyrics"', con=engine)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/names")
def names():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    # stmt = db.session.query(Samples).statement
    # df = pd.read_sql_query(stmt, db.session.bind)
    print("inside py name")
    # Return a list of the column names (sample names)
    listYear= ['2015','2014','2013','2012','2011','2010','2009','2008','2007','2006']
    # df = pd.DataFrame(listYear,columns=["Year"])
    # yearData = [row for row in df["Word"]]
    YearTrace = {
      "Year": listYear
    }
    print(YearTrace["Year"])
    return jsonify(YearTrace)

@app.route("/album_sales/<sample>")
def album_sales(sample):
    """Return a list of sample names."""
    sqlQueryStr = 'SELECT "album_title", "num_of_sales" FROM "db_albums" WHERE "year_of_pub"= '+ sample + ' ORDER BY "num_of_sales" desc'
    df = pd.read_sql_query(sqlQueryStr, con=engine).head(5)
    album = [row[0:10] for row in df["album_title"]]
    sales = [int(row)-900000 for row in df["num_of_sales"]]
    trace1 = {
      "x": album,
      "y": sales,
      "type": "bar"
    }

    print(len(album), len(sales))
    # print(jsonify(trace1))
    
    # Return a list of the column names (sample names)
    # jsonify(trace1)
    return jsonify(trace1)


@app.route("/total_critic")
def total_critic1():
    """Return the MetaData for a given sample."""

    df = pd.read_sql_query('SELECT "album_title", "rolling_stone_critic" + "mtv_critic" + "music_maniac_critic" as "Total_Critic" FROM "db_albums" WHERE "year_of_pub"= "2006" ORDER BY "total_critic" desc', con=engine).head(10)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])


    print(sales)
    return jsonify(trace1)

@app.route("/total_critic/<sample>")
def total_critic(sample):
    sqlQueryStr = 'SELECT "album_title", "rolling_stone_critic" + "mtv_critic" + "music_maniac_critic" as "Total_Critic" FROM "db_albums" WHERE "year_of_pub"=' + sample + ' ORDER BY "total_critic" desc'
    df = pd.read_sql_query(sqlQueryStr, con=engine).head(10)
    album_critic = [row[0:10] for row in df["album_title"]]
    critic = [row for row in df["Total_Critic"]]
    trace2 = {
      "x": album_critic,
      "y": critic,
      "type": "bar"
    }
    print(len(album_critic), len(critic))
    return jsonify(trace2)

@app.route("/debut_artists/<sample>")
def debut_artists(sample):
    # sqlQueryStr ='SELECT "artist_id", COUNT("album_title") AS "CNT_albums" FROM "db_albums" WHERE "year_of_pub" = 2006 GROUP BY "artist_id" ORDER BY COUNT("album_title") DESC'
    # print(sqlQueryStr)
    # df = pd.read_sql_query(sqlQueryStr,con=engine).head(10)
    # album_artist = [row for row in df["artist_id"]]
    # sales = [row for row in df["CNT_albums"]]
    sqlQueryStr="SELECT * FROM db_lyrics WHERE Year="+ sample
    billboard_lyrics_df= pd.read_sql_query(sqlQueryStr, con=engine)
    a = pd.DataFrame(billboard_lyrics_df["Artist"].value_counts()).reset_index()
    a=a.head(5)
    a.columns =("Artist","Count of Albums")
    album_artist = [row for row in a["Artist"]]
    Count_Albums = [row for row in a["Count of Albums"]]
    trace3 = {
      "x": album_artist,
      "y": Count_Albums,
      "type":"bar"
    }
    return jsonify(trace3)

@app.route("/Lyrics_word_count/<sample>")
def getCountWordLyrics(sample):
    
    def word_count(str):
        counts = dict()
        words = str.split(" ")
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts
    
    print("inside lyrics")
    # billboard_lyrics_data.to_sql(name="db_lyrics", con=engine,if_exists = 'replace',index=False)
    billboard_lyrics_df= pd.read_sql_query('SELECT * FROM "db_lyrics"', con=engine)
    billboard_lyrics_data = billboard_lyrics_df[billboard_lyrics_df["Rank"].isin([1,2])]
    wordlist = []
    countlist = []
    yearList =[]
    sightWordsList = ['of','your','','you','a','the','i','na','it','to','if','that','had','into','on','is','its','and','she','so','x','yeah','im','in','this','p','up','let','me','my']
    for row in billboard_lyrics_data.itertuples():
        music_lyrics = billboard_lyrics_data["Lyrics"][row.Index]
        year = billboard_lyrics_data["Year"][row.Index]
        count = word_count(str(music_lyrics))
        for k,v in count.items():
            if k not in sightWordsList:
                wordlist.append(k)
                countlist.append(v)
                yearList.append(year)
    df = pd.DataFrame({"Year":yearList,"Word":wordlist,"Count":countlist})
    print(sample)
    df = df[(df["Count"]>15) & (df["Year"]==int(sample))]
    df = df.sort_values(by=["Year","Count"],ascending =False)
    WordData = [row for row in df["Word"]]
    CountData = [row for row in df["Count"]]
    trace4 = {
      "x": WordData,
      "y": CountData,
      "type": "bar"
    }
    print(trace4)
    return jsonify(trace4)

if __name__ == "__main__":
    app.run()

# album_sales(sample)
# total_critic()
# debut_artists()
# getCountWordLyrics()
