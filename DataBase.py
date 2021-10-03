import sqlite3
conn = sqlite3.connect('News.sqlite')
cur = conn.cursor()


def createDb():
    try:
        cur.execute(
            'CREATE TABLE News(Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, Headline TEXT NOT NULL UNIQUE, Source TEXT NOT NULL, Date DATE NOT NULL)')
    except:
        print('Table is already created')


def addData(Headline, Source, Date):
    try:

        cur.execute(
            'INSERT INTO News (Headline, Source, Date) VALUES (?, ?, ?)', (Headline, Source, Date))
        conn.commit()
    except:
        print('An exception occurred')
