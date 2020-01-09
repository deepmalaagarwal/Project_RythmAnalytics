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

