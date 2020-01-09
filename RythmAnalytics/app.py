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
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
db = SQLAlchemy(app)

#albums 
# File to Load (Remember to Change These)
file_to_load = "DataSets/clean_albums.csv"

# Read Purchasing File and store into Pandas data frame
albums_data = pd.read_csv(file_to_load)


# from .models import Pet
albums_data.to_sql(name="db_albums", con=engine,if_exists = 'replace',index=False)


# Create table for Sales analysis of albums
albums_data.to_sql(name="db_albums", con=engine,if_exists = 'replace',index=False)
# Create table for Lyrics analysis of albums
billboard_lyrics_data.to_sql(name="db_lyrics", con=engine,if_exists = 'replace',index=False)
pd.read_sql_query('SELECT * FROM "db_lyrics"', con=engine)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/album_sales")
def album_sales():
    """Return a list of sample names."""

<<<<<<< HEAD
    df = pd.read_sql_query('SELECT "album_title", "num_of_sales" FROM "db_albums" WHERE "year_of_pub"= "2006" ORDER BY "num_of_sales" desc', con=engine).head(10)
    album = [row for row in df["album_title"]]
    sales = [row for row in df["num_of_sales"]]
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

@app.route("/debut_artists")
def debut_artists():
    """Return a list of sample names."""

    df = pd.read_sql_query('SELECT "artist_id", COUNT("album_title") AS "Cnt_albums" FROM "db_albums" WHERE "year_of_pub" = "2006" GROUP BY "artist_id" ORDER BY COUNT("album_title") DESC', con=engine).head(10)
    album = [row for row in df["artist_id"]]
    sales = [row for row in df["Cnt_albums"]]
=======
    df = pd.read_sql_query('SELECT "album_title", "num_of_sales" FROM "db_albums" WHERE "year_of_pub"= "2006" ORDER BY "num_of_sales" desc', con=engine).head(5)
    album = [row[0:10] for row in df["album_title"]]
    sales = [int(row)-900000 for row in df["num_of_sales"]]
>>>>>>> f8d2552b62ca7a1a106cef13f54a221b9bdacfdd
    trace1 = {
      "x": album,
      "y": sales,
      "type": "bar"
    }
<<<<<<< HEAD

    print(len(album), len(sales))
    # print(jsonify(trace1))
    
    # Return a list of the column names (sample names)
    # jsonify(trace1)
    return jsonify(trace1)


@app.route("/total_critic")
def total_critic():
    """Return the MetaData for a given sample."""

    df = pd.read_sql_query('SELECT "album_title", "rolling_stone_critic" + "mtv_critic" + "music_maniac_critic" as "Total_Critic" FROM "db_albums" WHERE "year_of_pub"= "2006" ORDER BY "total_critic" desc', con=engine).head(10)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])

=======
>>>>>>> f8d2552b62ca7a1a106cef13f54a221b9bdacfdd

    print(sales)
    return jsonify(trace1)

@app.route("/total_critic")
def total_critic():
    df = pd.read_sql_query('SELECT "album_title", "rolling_stone_critic" + "mtv_critic" + "music_maniac_critic" as "Total_Critic" FROM "db_albums" WHERE "year_of_pub"= "2006" ORDER BY "total_critic" desc', con=engine).head(10)
    album_critic = [row[0:10] for row in df["album_title"]]
    critic = [row for row in df["Total_Critic"]]
    trace2 = {
      "x": album_critic,
      "y": critic,
      "type": "bar"
    }
    print(len(album_critic), len(critic))
    return jsonify(trace2)

@app.route("/debut_artists")
def debut_artists():
    sqlQueryStr ='SELECT "artist_id", COUNT("album_title") AS "CNT_albums" FROM "db_albums" WHERE "year_of_pub" = 2006 GROUP BY "artist_id" ORDER BY COUNT("album_title") DESC'
    print(sqlQueryStr)
    df = pd.read_sql_query(sqlQueryStr,con=engine).head(10)
    album_artist = [row for row in df["artist_id"]]
    sales = [row for row in df["CNT_albums"]]
    trace3 = {
      "x": album_artist,
      "y": sales,
      "type":"bar"
    }
    print(album_artist)
    print(sales)
    return jsonify(trace3)

@app.route("/lyrics_analysis")
def word_count(str):
    counts = dict()
    words = str.split(" ")
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def getCountWordLyrics(billboard_lyrics_data):
    billboard_lyrics_data = billboard_lyrics_data[billboard_lyrics_data["Rank"].isin([1,2])]
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
    df= pd.DataFrame({"Year":yearList,"Word":wordlist,"Count":countlist})
    df = df[(df["Count"]>15)]
    df= df.sort_values(by=["Year","Count"],ascending =False)
    # df.head()
    return jsonify(list(df.columns)[2:])

if __name__ == "__main__":
    app.run()

<<<<<<< HEAD
album_sales()
=======
album_sales()
total_critic()
getCountWordLyrics(billboard_lyrics_data)
>>>>>>> f8d2552b62ca7a1a106cef13f54a221b9bdacfdd
