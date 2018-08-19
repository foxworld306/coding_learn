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

<<<<<<< HEAD
for child in bs.find('table',{'id':'giftList'}).children:
    print(child)
    print()
=======
for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)
>>>>>>> a994ee957b3bfad09801b2c67cbf96420a0fabc4
