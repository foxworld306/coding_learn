# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bs = BeautifulSoup(html, "html.parser")
# # nameList = bs.findAll('span', {'class': 'green'})
# # for name in nameList:
# #     print(name.get_text())

# # alltext = bs.findAll(id="text")
# # print(alltext[0].get_text())
# # print(bs.findAll(lambda tag: len(tag.attrs) == 2))

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'lxml')

for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)
