import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
#print(type(res))

soup = bs4.BeautifulSoup(res.text, 'lxml')
#print(type(soup))

data = soup.select('.toc .toctext')  # selecting class

for i in data:
    print(i.getText())
