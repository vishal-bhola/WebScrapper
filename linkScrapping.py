import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
print(type(res.text))

soup = bs4.BeautifulSoup(res.text,'lxml')

links = soup.find_all('a', href=True)

for link in links:
    print(link['href'])
