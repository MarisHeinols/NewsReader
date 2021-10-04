import certifi
import pymongo
import sqlite3


# SQLite variables
conn = sqlite3.connect('News.sqlite')
cur = conn.cursor()
ca = certifi.where()

# MongoDb variables
myclient = pymongo.MongoClient(
    'mongodb+srv://user:OBxIoqsu4yDflTQq@news.ray5r.mongodb.net/News?retryWrites=true&w=majority', tlsCAFile=ca)
mydb = myclient["News"]
mycol = mydb["News"]

# Gets eveything from server db


def getDataFromMongo():
    data = mycol.find({})
    return data

# Ads data to local database


def addData(Headline, Source, Date):
    try:
        cur.execute(
            'INSERT INTO News (Headline, Source, Date) VALUES (?, ?, ?)', (Headline, Source, Date))
        conn.commit()
    except:
        print('Data is already in database')
# Adding data from server db to local db


def addDataFromMongo():
    dataArray = getDataFromMongo()
    for post in dataArray:
        addData(post.get("Headline"), post.get(
            "Source"), post.get("Date"))

# Create local databse if not exists and insert data from server db


def createDb():
    try:
        cur.execute(
            'CREATE TABLE News(Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, Headline TEXT NOT NULL UNIQUE, Source TEXT NOT NULL, Date DATE NOT NULL)')
        addDataFromMongo()
    except:
        print('Table is already created')
        cur.execute('DELETE FROM News')
        conn.commit()
        addDataFromMongo()


# Adding data to server db


def addDataToMongo(Headline, Source, Date):

    isInDb = False
    dataArray = getDataFromMongo()
    # Check if news post exists on server db
    for post in dataArray:
        if(post.get("Headline") == Headline):
            isInDb = True

    if (isInDb == False):
        data = {"Headline": Headline, "Source": Source, "Date": Date}
        # If data does not exists on server add it to local db and server db
        x = mycol.insert_one(data)
        addData(Headline, Source, Date)
