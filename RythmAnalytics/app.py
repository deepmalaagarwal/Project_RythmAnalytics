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



@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/album_sales")
def album_sales():
    """Return a list of sample names."""

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
def total_critic():
    """Return the MetaData for a given sample."""

    df = pd.read_sql_query('SELECT "album_title", "rolling_stone_critic" + "mtv_critic" + "music_maniac_critic" as "Total_Critic" FROM "db_albums" WHERE "year_of_pub"= "2006" ORDER BY "total_critic" desc', con=engine).head(10)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])



if __name__ == "__main__":
    app.run()

album_sales()