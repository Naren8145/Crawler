import requests
import re
import pandas as pd
from bs4 import BeautifulSoup as BS
from requests import session
s=session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'


def crawl_cat_id(url):
    r=s.get(url)
    text=r.text
    cat_id=re.search("collection_id: '(.*?)',",text).group(1)
    list_url="https://www.21faves.com/api/collections/"+str(cat_id)+"/products"

    return list_url
    

DATA=[]


def crawl_list(list_url):
    cookies = {
    'client_id': '1668439328232412',
    '_c_id': '1668439328232927269',
    'sw_session': '63725d2076fb4',
    'store_locale': 'en-US',
    '__cf_bm': 'SZzw.myenqHoPXBvkaNaxC_xAvL_Ivme7DbmTYVFJfo-1668439328-0-AYqlgZ3dPySzwyvrB4uAzpu6ycPYEGP1My5UGQfLeQRB4wYw+LAbmidowdOccXvzy6yWcngQGgaEpLxdeW3gMBs=',
    'session_id': '1668439335172324',
    'shoplazza_source': '%7B%22%24first_visit_url%22%3A%22https%3A%2F%2Fwww.21faves.com%2F%22%2C%22%24latest_referrer_host%22%3A%22Google%22%2C%22expire%22%3A1669044135174%7D',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218476bbe6922e3-0db05cd471852e8-c535426-1049088-18476bbe693389%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%2218476bbe6922e3-0db05cd471852e8-c535426-1049088-18476bbe693389%22%7D',
    'sajssdk_2015_cross_new_user': '1',
    '_ga': 'GA1.2.1380354562.1668439340',
    '_gid': 'GA1.2.1188137229.1668439340',
    '_identity_cart': '3da38468-a1de-4f9d-9bc2-09bac025cd3f',
    '_fbp': 'fb.1.1668439346044.608936743',
    '_identity_popups': '6eba053a-1d6e-4060-87eb-7eacaa5a74e21668439385',
    '_identity_popups_bundle': '865b87cd-f136-435e-9994-bc3e96bca7d21668439385',
    '_gat_gtag_UA_83020630_37': '1',
    }
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'Alt-Used': 'www.21faves.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.21faves.com/collections/new?spm=',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'client_id=1668439328232412; _c_id=1668439328232927269; sw_session=63725d2076fb4; store_locale=en-US; __cf_bm=SZzw.myenqHoPXBvkaNaxC_xAvL_Ivme7DbmTYVFJfo-1668439328-0-AYqlgZ3dPySzwyvrB4uAzpu6ycPYEGP1My5UGQfLeQRB4wYw+LAbmidowdOccXvzy6yWcngQGgaEpLxdeW3gMBs=; session_id=1668439335172324; shoplazza_source=%7B%22%24first_visit_url%22%3A%22https%3A%2F%2Fwww.21faves.com%2F%22%2C%22%24latest_referrer_host%22%3A%22Google%22%2C%22expire%22%3A1669044135174%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218476bbe6922e3-0db05cd471852e8-c535426-1049088-18476bbe693389%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%2218476bbe6922e3-0db05cd471852e8-c535426-1049088-18476bbe693389%22%7D; sajssdk_2015_cross_new_user=1; _ga=GA1.2.1380354562.1668439340; _gid=GA1.2.1188137229.1668439340; _identity_cart=3da38468-a1de-4f9d-9bc2-09bac025cd3f; _fbp=fb.1.1668439346044.608936743; _identity_popups=6eba053a-1d6e-4060-87eb-7eacaa5a74e21668439385; _identity_popups_bundle=865b87cd-f136-435e-9994-bc3e96bca7d21668439385; _gat_gtag_UA_83020630_37=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
    }
    for i in range(1,pages+1):
        params = {
    'page': str(i),
    'sort_by': 'manual',
    'limit': '48',
    'tags': '',
    'price': '',
    }
        r = s.get(list_url, params=params, cookies=cookies, headers=headers)
        js=r.json()
        products=js['data']['products']
        for handles in products:
            imgurls=[]
            handle=handles['handle']
            durl='https://www.21faves.com/products/'+handle
            dr=s.get(durl)
            soup=BS(dr.text,"html.parser")
            img=soup.find('div','product-image col-12 col-md-6').find_all('div','swiper-slide hidden')
            trs = soup.find('div','product-info__desc-tab-content').find('table', attrs={'style': '99%'}).find_all('tr')
            des = []
            for tr in trs:
                raw = {}
                tds = tr.find_all('td')
                raw[tds[0].text.strip()] = tds[1].text.strip()
                des.append(raw)
            for imgurl in img:
                imgurl=imgurl.find('div','position-relative w-100').find('img').get('data-src').replace("{width}x_nw", '540x')
                imgurls.append(imgurl)
            d={"NAME":handle,"IMAGE URL":'|'.join(imgurls), "DESCRIPTION":des}
            print(d)
            DATA.append(d)


# x=int(input("enter the value of total products in the category"))
pages=int(142/48)
url='https://www.21faves.com/collections/wetsuit?spm='
list_url = crawl_cat_id(url)
crawl_list(list_url)

df=pd.DataFrame(DATA)
df.to_excel('21faves_data.xlsx',index=False)