import xml.etree.ElementTree as ET #Module implements a simple and efficient API for parsing and creating XML data.
import sqlite3 #Must import SQLlite in order to use it


conn = sqlite3.connect('trackdb.sqlite') #The connect() function initiates a 3-way handshake with the server socket and establishes the connection
cur = conn.cursor()  #The cursor function  is used to execute statements to communicate with the SQL database.
 
# Make some fresh tables using executescript()
#Begins my Reseting and Deleting any existing tables
#Then Creates the 3 Tables
#INTEGER NOT NULL PRIMARY KEW AUTOINCREMENT UNIQUE - Column not accept null values, assigns a non similar value to primary key ever time a new record is inserted
cur.executescript('''
DROP TABLE IF EXISTS Artist;  
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE   
    
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


fname = input('Enter file name: ') #Prompt User to input the file
if ( len(fname) < 1 ) : fname = 'Library.xml'  #Allows user to simply press enter to open specific file
 
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
#Outlines how the lookup function will work within this program
def lookup(d, key):  #Always need to define a function, Finds the value with the associated key
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None
#Finds the key by making sure the tag is <key> and knowing that the next value is the important one
# d is dictionary <key>Track ID</key>  --> is a "child tag"/ looks through all the values in the dictionary
stuff = ET.parse(fname) #Creates a Data tree from the XML file
all = stuff.findall('dict/dict/dict') #finds only elements with a tag which are direct children of the current element, returns a list, 3 Dictionaries to Find the actual song names 
print('Dict count:', len(all)) #Prints the total amount of dictionaries present within the file
#Utilizes the lookup function to grab the important data from the XML file.
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None : 
        continue

    #print(name, artist, genre, album, count, rating, length) #Finds and prints all track names/artists/albums/count/rating/length in the file

#INSERT/IGNORE, Adds multiple rows to a table and if an error occurs during the processing, SQL terminates the statement and returns an error and are ignored only inserting valid data
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
#Fetches the next row (case) from the active dataset
    artist_id = cur.fetchone()[0]
    
    #Not al Tracks have genre_id so must be initialized 
    genre_id = 0
    if genre != None :
        cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ))
        cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
        #Fetches the next row (case) from the active dataset
        genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

#Title, album_id, len, rating, count are all attributes to the Track Table, followed by subsequent ? value placeholders & labels
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )
    
    cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3''')
#On is clause on how to join the table, "temporary table", Scalability Purposes, matchin up ID's & Data
    conn.commit()
