# Key: eb28d336
# Title, Desc, Rating, release date, duration, img
import requests
import io
import json

file = io.open("top250.csv", mode="w", encoding="utf-8")
file.write(f"Title,Desc,Rating,Release date,Duration,Img\n")
for line in io.open("250.txt", mode="r", encoding="utf-8"):
    content = line.split(',')
    name = content[0]
    year = content[1].replace('(', '').replace(')', '')
    url = f"http://www.omdbapi.com/?apikey=eb28d336&t={name}&y={year}&plot=full"
    myResponse = requests.get(url)
    data = json.loads(myResponse.text)
    title = data['Title'].replace(',', '&#44;')
    desc = data['Plot'].replace(',', '&#44;')
    file.write(f"{title},{desc},{data['imdbRating']},{data['Released']},{data['Runtime']},{data['Poster']}\n")
file.close()
