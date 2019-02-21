from bs4 import BeautifulSoup
import requests
import io

file = io.open("250.txt", mode="w", encoding="utf-8")

url = "https://www.imdb.com/chart/top?sort=rk,asc&mode=simple&page=1"
headers = {"Accept-Language": "en-US,en;q=0.5"}
r = requests.get(url, timeout=10, headers=headers)
soup = BeautifulSoup(r.text, features="html5lib")

find_titles = soup.findAll("td", {"class": "titleColumn"})
for tag in find_titles:
    name = tag.findChild().text.replace(",", "&#44;")
    year = tag.findChildren()[1].text
    file.write(f"{name},{year}\n")

file.close()
print(f"Done")


