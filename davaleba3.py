import sqlite3
import json
from json import JSONDecodeError
import requests

user_input = input("Enter Movie Name: ")

url = f'https://api.tvmaze.com/search/shows?q={user_input}'

result = requests.get(url).json()

data = json.dumps(result, indent=4)

print(data)

# connect to the database
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

while True:
    user_choice = input("Sheviyvanot bazashi? y/n: ")
    if user_choice == "y":
        genres = result[0]['show']['genres']

        genres_str = ""

        for i in genres:
            genres_str += i + " "

        name = result[0]['show']['name']

        rating = result[0]['show']['rating']['average']

        sql = ''' CREATE TABLE IF NOT EXISTS MOVIES (NAME NOT NULL, GENRE NOT NULL, RATING FLOAT) '''

        cursor.execute(sql)

        add_movie = f"INSERT INTO MOVIES (NAME, GENRE, RATING) VALUES ('{name}', '{genres_str}', {rating})"

        cursor.execute(add_movie)

        break

    elif user_choice == "n":
        break

# 'select * from data where genre="{user_genre}"'

res = cursor.execute("SELECT * FROM MOVIES")

rame = res.fetchall()

print(rame)

conn.commit()
conn.close()
