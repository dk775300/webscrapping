import bs4
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


handle = input("Whose tweets would you like to see? \n")
my_url = "https://twitter.com/"+handle
req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
uClient=urlopen(req)
page_byte= uClient.read()
page_html=page_byte.decode('utf-8')
uClient.close()

page_soup = soup(page_html, "html.parser")



print(page_soup.title.text)
"""
for foo in soup.findAll('a'):
    print(foo.get('href'))
"""
    
print(page_soup.find('div',{"class":"ProfileHeaderCard"}).find('p').text)

i=1
for tweets in page_soup.findAll('div',{"class":"content"}):
    print(i)
    print(tweets.find('p').text)
    i=i+1