import urllib.request
from bs4 import BeautifulSoup

url = "https://old.reddit.com/top/"
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
request = urllib.request.Request(url,headers={'User-Agent': user_agent})
html = urllib.request.urlopen(request).read()
soup = BeautifulSoup(html,'html.parser')

links = soup.find_all('a', attrs={'class':'author'})

for link in links:
    print(link.attrs['href'])
    print(link.string)
