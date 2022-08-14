import requests
import bs4

res = requests.get('https://suryatech.neocities.org/')
print(type(res))
print(res)
#print(res.text)

print(" ")
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(type(soup))

print(" ")
title = soup.select('h1')
print(title[0])
print(title[0].getText())

print(" ")
divs = soup.select('div')
print(divs)
