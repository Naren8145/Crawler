import requests
import pandas as pd
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%a %b %d %Y %X")+str(" GMT+0530 (India Standard Time)")

cat_url = 'https://www.ajio.com/s/clothing-4461-74581'
ProductsData = list() 

cookies = {
    '_gaexp': 'GAX1.2.EXUvxSPIQuKLD2P6Eux2rQ.19515.1!9TcsvHvXQ8SZ3Qf9pl540w.19523.1!Tw9V8JeoSbWSlRKyRTws8A.19593.1!Dk6-HYGJSziWIAz-RfQ6jA.19544.1',
    'V': '201',
    '_gcl_aw': 'GCL.1685860409.CjwKCAjwyeujBhA5EiwA5WD7_XVC3BfA1R946mbnw7gshPpxArN7gYUEcBgDkOmxfSUHHqLEbTvWORoCbzYQAvD_BwE',
    '_gcl_au': '1.1.1628632661.1685860376',
    'sessionStatus': 'true|undefined',
    'FirstPage': dt_string,
    'AB': 'B',
    'plpAds': 'true',
    '_scid': 'f0ae52e9-e3f6-46a8-ae63-6e4e45eea404',
    '_ga': 'GA1.2.607764523.1685860406',
    '_gid': 'GA1.2.1022613460.1685860406',
    '_fpuuid': 'SEEcvAqRBczgKOt2unlWR',
    'ImpressionCookie': '0',
    '_gac_UA-68002030-1': '1.1685860427.CjwKCAjwyeujBhA5EiwA5WD7_XVC3BfA1R946mbnw7gshPpxArN7gYUEcBgDkOmxfSUHHqLEbTvWORoCbzYQAvD_BwE',
    '_fbp': 'fb.1.1685860414552.2100674269',
    'ifa': '1b6a1f00-a410-4f07-b3b1-975856ed82e1',
    'os': '4',
    'vr': 'WEB-1.15.1',
    'jioAdsFeatureVariant': 'false',
    'cdigiMrkt': 'utm_source%3A%7Cutm_medium%3A%7Cdevice%3Ad%7Cexpires%3ATue%2C%2004%20Jul%202023%2006%3A39%3A46%20GMT%7C',
    '_sctr': '1%7C1685817000000',
    'g_state': '{"i_p":1685867646680,"i_l":1}',
    'ADRUM_BT': 'R:42|i:6333|g:b2f25ff1-f362-43de-8027-7ca5a7ce590c18064283|e:547|n:customer1_be12de70-87be-45ee-86d9-ba878ff9a400',
    '_dc_gtm_UA-68002030-1': '1',
    '_scid_r': 'f0ae52e9-e3f6-46a8-ae63-6e4e45eea404',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': cat_url,
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    # 'Cookie': '_gaexp=GAX1.2.EXUvxSPIQuKLD2P6Eux2rQ.19515.1!9TcsvHvXQ8SZ3Qf9pl540w.19523.1!Tw9V8JeoSbWSlRKyRTws8A.19593.1!Dk6-HYGJSziWIAz-RfQ6jA.19544.1; V=201; _gcl_aw=GCL.1685860409.CjwKCAjwyeujBhA5EiwA5WD7_XVC3BfA1R946mbnw7gshPpxArN7gYUEcBgDkOmxfSUHHqLEbTvWORoCbzYQAvD_BwE; _gcl_au=1.1.1628632661.1685860376; sessionStatus=true|undefined; FirstPage=Sun Jun 04 2023 12:09:40 GMT+0530 (India Standard Time); AB=B; plpAds=true; _scid=f0ae52e9-e3f6-46a8-ae63-6e4e45eea404; _ga=GA1.2.607764523.1685860406; _gid=GA1.2.1022613460.1685860406; _fpuuid=SEEcvAqRBczgKOt2unlWR; ImpressionCookie=0; _gac_UA-68002030-1=1.1685860427.CjwKCAjwyeujBhA5EiwA5WD7_XVC3BfA1R946mbnw7gshPpxArN7gYUEcBgDkOmxfSUHHqLEbTvWORoCbzYQAvD_BwE; _fbp=fb.1.1685860414552.2100674269; ifa=1b6a1f00-a410-4f07-b3b1-975856ed82e1; os=4; vr=WEB-1.15.1; jioAdsFeatureVariant=false; cdigiMrkt=utm_source%3A%7Cutm_medium%3A%7Cdevice%3Ad%7Cexpires%3ATue%2C%2004%20Jul%202023%2006%3A39%3A46%20GMT%7C; _sctr=1%7C1685817000000; g_state={"i_p":1685867646680,"i_l":1}; ADRUM_BT=R:42|i:6333|g:b2f25ff1-f362-43de-8027-7ca5a7ce590c18064283|e:547|n:customer1_be12de70-87be-45ee-86d9-ba878ff9a400; _dc_gtm_UA-68002030-1=1; _scid_r=f0ae52e9-e3f6-46a8-ae63-6e4e45eea404',
}

Current_Page = 203 # we apply an condition at the end of loop. IF Current_Page > total page(in pagination) THEN loop will break

while True:
    params = {
        'currentPage': Current_Page,
        'pageSize': '45',
        'format': 'json',
        'query': ':relevance',
        'sortBy': 'relevance',
        'curated': 'true',
        'curatedid': cat_url.split('/')[-1],
        'gridColumns': '3',
        'facets': '',
        'advfilter': 'true',
        'platform': 'Desktop',
        'showAdsOnNextPage': 'false',
        'is_ads_enable_plp': 'true',
        'displayRatings': 'true',
    }

    response = requests.get('https://www.ajio.com/api/category/83', params=params, cookies=cookies, headers=headers)
    print(response,"response of page number",Current_Page)
    js = response.json()
    Products = js.get('products')
    if Products:
        for product in Products:
            Product_code = product.get('code')
            Brand = product.get('brandTypeName')
            Name = product.get('name')
            mrp = product['wasPriceData'].get('value')
            discount = product.get('discountPercent')
            sellingPrice = product['price'].get('value')
            BBSprice = product['offerPrice'].get('value')
            product_url = "https://www.ajio.com"+product.get('url')
            imglist = list()
            img = product.get('extraImages')
            if img :
                for imgurl in img:
                    image_url = imgurl['images'][0].get('url')
                    imglist.append(image_url)

            d = {
                "BRAND NAME": Brand,
                "PRODUCT NAME":Name,
                "M.R.P":mrp,
                "DISCOUNT (%)": discount,
                "SELLING PRICE": sellingPrice,
                "BIG BILLION SALE PRICE": BBSprice,
                "PRODUCT URL": product_url,
                "IMAGE URL": '|'.join(imglist) # list of image url is seperated by '|' (pipe)
            }

            print(d)
            ProductsData.append(d)   

    Total_pages = js['pagination'].get('totalPages')
    print("Total pages are",Total_pages)
    print("Current page is",Current_Page)
    Current_Page += 1
    if Current_Page >= Total_pages or Products == None:
        break

    if Current_Page % 25 == 0:

        df = pd.DataFrame(ProductsData)
        df.to_excel("AJIO Mens Clothing Data2.xlsx",index=False)







