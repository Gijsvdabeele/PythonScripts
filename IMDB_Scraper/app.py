from bs4 import BeautifulSoup
import requests
import time
import os
from multiprocessing import Process
import fileinput
import io

years = ["2018","2017","2016","2015"]


def get_total(year):
    url = f"https://www.imdb.com/search/title?title_type=feature&year={year}-01-01,{year}-12-31&start=1&ref_=adv_nxt"
    r = requests.get(url,timeout=10)
    soup = BeautifulSoup(r.text, features="html5lib")
    find_total = soup.find("div", {"class":"desc"})
    total = find_total.find('span')
    num = total.text[total.text.find('of'):]
    num = num[3:]
    num = num[:num.find('titles.')].strip().replace(',', '')
    return int(num)


def worker1():
    file = io.open("temp1.csv", mode="w", encoding="utf-8")
    old = time.time()

    total = get_total(years[0])
    print(total)
    i = 1
    while i < total:
        try:
            # Create url with looping index
            url = f"https://www.imdb.com/search/title?title_type=feature&year={years[0]}-01-01,{years[0]}-12-31&start={i}&ref_=adv_nxt"
            # Get html
            r = requests.get(url,timeout=10)
            if not r.status_code == 404:
                soup = BeautifulSoup(r.text, features="html5lib")
                # Get title & rating data
                find_titles = soup.findAll("h3", {"class": "lister-item-header"})
                find_ratings = soup.findAll('div',{'class':'inline-block ratings-imdb-rating'})

                for c, t in enumerate(find_titles):
                    title = t.find('a')
                    title = title.text.replace(",", "&#44;")
                    rating = find_ratings[c].find('strong')

                    try:
                        file.write(f"{title},{rating.text}\n")
                    except UnicodeEncodeError:
                        continue
                i += 50
        except (AttributeError, IndexError):
            i += 50
            continue
    file.close()
    print(f"T1 Done: {time.time()-old}s")


def worker2():
    file = io.open("temp2.csv", mode="w", encoding="utf-8")
    old = time.time()

    total = get_total(years[1])
    i = 1
    while i < total:
        try:
            # Create url with looping index
            url = f"https://www.imdb.com/search/title?title_type=feature&year={years[1]}-01-01,{years[1]}-12-31&start={i}&ref_=adv_nxt"
            # Get html
            r = requests.get(url, timeout=10)
            if not r.status_code == 404:
                soup = BeautifulSoup(r.text, features="html5lib")
                # Get title & rating data
                find_titles = soup.findAll("h3", {"class": "lister-item-header"})
                find_ratings = soup.findAll('div',{'class':'inline-block ratings-imdb-rating'})

                for c, t in enumerate(find_titles):
                    title = t.find('a')
                    title = title.text.replace(",", "&#44;")
                    rating = find_ratings[c].find('strong')

                    try:
                        file.write(f"{title},{rating.text}\n")
                    except UnicodeEncodeError:
                        continue
                i += 50
        except (AttributeError, IndexError):
            i += 50
            continue
    file.close()
    print(f"T2 Done: {time.time()-old}s")


def worker3():
    file = io.open("temp3.csv", mode="w", encoding="utf-8")
    old = time.time()

    total = get_total(years[2])
    i = 1
    while i < total:
        try:
            # Create url with looping index
            url = f"https://www.imdb.com/search/title?title_type=feature&year={years[2]}-01-01,{years[2]}-12-31&start={i}&ref_=adv_nxt"
            # Get html
            r = requests.get(url, timeout=10)
            if not r.status_code == 404:
                soup = BeautifulSoup(r.text, features="html5lib")
                # Get title & rating data
                find_titles = soup.findAll("h3", {"class": "lister-item-header"})
                find_ratings = soup.findAll('div',{'class':'inline-block ratings-imdb-rating'})

                for c, t in enumerate(find_titles):
                    title = t.find('a')
                    title = title.text.replace(",", "&#44;")
                    rating = find_ratings[c].find('strong')

                    try:
                        file.write(f"{title},{rating.text}\n")
                    except UnicodeEncodeError:
                        continue
                i += 50
        except (AttributeError, IndexError):
            i += 50
            continue
    file.close()
    print(f"T3 Done: {time.time()-old}s")


def worker4():
    file = io.open("temp4.csv", mode="w", encoding="utf-8")
    old = time.time()

    total = get_total(years[3])
    i = 1
    while i < total:
        try:
            # Create url with looping index
            url = f"https://www.imdb.com/search/title?title_type=feature&year={years[3]}-01-01,{years[3]}-12-31&start={i}&ref_=adv_nxt"
            # Get html
            r = requests.get(url, timeout=10)
            if not r.status_code == 404:
                soup = BeautifulSoup(r.text, features="html5lib")
                # Get title & rating data
                find_titles = soup.findAll("h3", {"class": "lister-item-header"})
                find_ratings = soup.findAll('div',{'class':'inline-block ratings-imdb-rating'})

                for c, t in enumerate(find_titles):
                    title = t.find('a')
                    title = title.text.replace(",", "&#44;")
                    rating = find_ratings[c].find('strong')

                    try:
                        file.write(f"{title},{rating.text}\n")
                    except UnicodeEncodeError:
                        continue
                i += 50
        except (AttributeError, IndexError):
            i += 50
            continue
    file.close()
    print(f"T4 Done: {time.time()-old}s")


if __name__ == '__main__':
    t1 = Process(target=worker1)
    t2 = Process(target=worker2)
    t3 = Process(target=worker3)
    t4 = Process(target=worker4)
    threads = [t1,t2,t3,t4]

    for i in threads:
        i.start()
    for i in threads:
        i.join()

    file_list = ["temp1.csv","temp2.csv","temp3.csv","temp4.csv"]
    with io.open('imdb_data.csv', mode='rb', encoding="utf-8") as file:
        input_lines = fileinput.input(file_list)
        file.writelines(input_lines)
    for i in range(len(file_list)):
        os.remove(file_list[i])
