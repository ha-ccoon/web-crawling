# BestSellerTitle: a-column a-span8
# BasePath: https://www.amazon.com/
# Product: a-carousel-row-inner
# Number: zg-bdg-text
# ProductTitle: a-link-normal[1]
# Review:   a-link-normal[2]
# url: a-link-normal[1]['href']

import requests
from bs4 import BeautifulSoup

soup = requests.get('https://www.amazon.com/Best-Sellers/zgbs', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'})
html = BeautifulSoup(soup.text, 'html.parser')

categories = html.select('div.a-column.a-span8')
print(len(categories))

category_list = []


for category in categories:
  category_list.append(category.text)

# print(category_list)
category_list.reverse()

divs = html.select('div.a-carousel-row-inner')

for div in divs:
  print('-' * 100)
  print(category_list[-1]) 
  print('-' * 100)
  
    
  
  lis = div.select('li.a-carousel-card')
  for li in lis:
    num = li.select_one('span.zg-bdg-text').text
    # print(num)
    
    title = li.select('a.a-link-normal')[1].text
    # print(title)
    
    url = 'https://www.amazon.com/' + li.select('a.a-link-normal')[1]['href']
    # print(url)
    
    rating = li.select('a.a-link-normal')[2].text
    # print(rating)
    
    price = li.select('a.a-link-normal')[3].text
    
    print(num, rating, title, price, sep='\t')
    print(url)
    
  category_list.pop()

