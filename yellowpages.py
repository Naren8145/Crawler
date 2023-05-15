import requests
import pandas as pd
from bs4 import BeautifulSoup as BS
from requests import session
s=session()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0'

# Enter category url below

cat_url = 'https://www.yellow-pages.ph/category/electrical-equipment-appliance-and-component/page-1'
yellow_page_data = []
count = 0
# response = s.get(cat_url)
# next_page = cat_url
while True:
    response = s.get(cat_url)
    soup = BS(response.text,'html.parser')
    product = soup.find_all('div','search-listing')
    for detail in product:
        name = detail.find('h2','search-tradename').text.strip()

        if detail.find('span','search-capsule-rounded search-badge'):
            category  = detail.find('span','search-capsule-rounded search-badge').text
        else:
            category = ''
        
        address = detail.find('span','ellipsis').text

        d_url = "https://www.yellow-pages.ph" + soup.find('h2','search-tradename').find('a','yp-click').get('href')
        res = s.get(d_url)
        d_soup = BS(res.text,'html.parser')
        contact = d_soup.find_all('a','biz-link d-block ellipsis link-disabled-d')
        cont_list = []
        for telephone in contact:
            number = telephone.get('href')
            cont_list.append(number)

        data = {
            "NAME":name,
            "CATEGORY":category,
            "ADDRESS":address,
            # "CONTACT NO":cont_list
          }
        print(data)
        yellow_page_data.append(data)
    count = count + 1

    if soup.find('a',{'rel':'next'}):
        cat_url = 'https://www.yellow-pages.ph' + soup.find('a',{'rel':'next'}).get('href')
    else:
        break
    print(count)
    print(response)

print('!!!!!!*******complete******!!!!!!')
df = pd.DataFrame(yellow_page_data)
df.to_csv("yellow_data_pages.csv", index = False)