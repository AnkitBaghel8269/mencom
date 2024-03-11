import json

import pymysql
import scrapy
from scrapy.cmdline import execute

from ics_v1_mencom.items import IcsV1SiteMapLinksItem
import ics_v1_mencom.db_config as db
# Define a class for links extracting
class Mencom_links(scrapy.Spider):
    #  Define spider name for run this file
    name = 'mancom_new_links'
    # Define vendor id for store in database which is given by client
    VENDOR_ID = "ACT-B7-002"
    # Define vendor name for store in database which is given by client
    VENDOR_NAME = "Mencom"
    # make inite function which is take start and end arguement for giving start and end value
    def __init__(self,start='',end='', name=None, **kwargs):
        super().__init__(name, **kwargs)
        # DATABASE CONNECTION
        self.con = pymysql.connect(host=db.db_host, user=db.db_user, password=db.db_password, db=db.db_name)
        self.cursor = self.con.cursor()
        self.start= start
        self.end=end

    def start_requests(self):
        # this is cookies for scrap data on site
        cookies = {
            'visid_incap_699049': 'CQfjeuDYQ+CGmcWxK6GynGcrDGUAAAAAQUIPAAAAAAAqEMSjlcfDQEL3oOfgUJL3',
            '_lfa': 'LF1.1.b95df4f6f318cd57.1695296365284',
            'incap_ses_883_699049': '0FCHHBHR6z6YSFFU4AtBDH0sDGUAAAAAObG4hWSI9ePOGMDO+41MYg==',
            'user_allowed_save_cookie': '%7B%221%22%3A1%7D',
            '_gid': 'GA1.2.450611667.1695296673',
            '_clck': '9zca6p|2|ff8|0|1359',
            'searchReport-log': '0',
            'incap_ses_715_699049': '72PdVUXJdjM8rD8CtDHsCTl0DWUAAAAA14xaSTL2WD9ONCbgrVVxDw==',
            'PHPSESSID': 'd41e4c5202e0013751dc0b9cc608399c',
            'form_key': 'WCy5ZOuXe6incRPG',
            'mage-cache-sessid': 'true',
            'mage-messages': '',
            'form_key': 'WCy5ZOuXe6incRPG',
            '_ga_P9JBZMY5X5': 'deleted',
            '_ga_P9JBZMY5X5': 'deleted',
            'incap_ses_1364_699049': 'UALCDOzhJg451m/ToOftEnSJDWUAAAAAElyHC68636C8GL1y2aGrmw==',
            '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2OTUyOTYzNjQsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1lbmNvbS5jb20vcGc3LWJsYWNrLXBsYXN0aWMtbnV0Lmh0bWwifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2OTUzODY0NTAsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1lbmNvbS5jb20vIn19',
            '_ga': 'GA1.2.907729905.1695296365',
            'aw_popup_viewed_page': '%5B%22078a683b1fc100af7f68bdabf091a6323b85d8d5464f780f3ed22c0d7f75b6bd%22%2C%22ea68962f02ad60a2f0074df56c737574a392ddcc543ce87792e351135df60c06%22%2C%22ae11dac5dc5aed05b2d39c51025fc505b8a0e68be50a62eb3bb7c06c4013684e%22%2C%227c526d0ade1c93c3760d3ca35a97e1161ddd84c3b11a760fbe76511e87ca8202%22%2C%228c681521fa6d510339b3c6143d220a2886d967f8393752bb087e3484d7edbee9%22%2C%22b35c57fe1da22473f05988f9e0b56b060b04c1b111cde4b86f4b681b657a1bad%22%2C%227cf33824e7d71f6179affc9bb172538ddc3441e4bbf70287dd5af5cdf79a9211%22%2C%220f88851e395f52198092c87571f9e2ed5c6133ddfbb858fa3de704bed2a19c2e%22%2C%2280413d881bb6f7ed75d595794af71e7c95d11f9f2639256636b3029f67009c92%22%2C%225dbc2f99d4ccd5a251203067f30b9194e22aefcd3e2e32e1d30766a5d9783074%22%2C%2281cc180cdd7c7ea9223a171811012eb8832b74b5219c8700d783f7557d8b7159%22%2C%22c68107f3023464839ef01ca54b87d9693eb2774357687508e32824ae97e3cce5%22%2C%22886894b2bec9b8ff99bca220b9ec08343a7546938ce32f1f2c91cad9286b7cc4%22%2C%2238f948d7207ccca335943dbdd258e840d16a96551c78d7d046b692e7264a7e29%22%5D',
            'private_content_version': '2972704f5d86bbf50d703047204721b3',
            'section_data_ids': '{%22customer%22:1695386453%2C%22compare-products%22:1695386453%2C%22last-ordered-items%22:1695386453%2C%22cart%22:1695386453%2C%22directory-data%22:1695386453%2C%22captcha%22:1695386453%2C%22instant-purchase%22:1695386453%2C%22loggedAsCustomer%22:1695386453%2C%22persistent%22:1695386453%2C%22review%22:1695386453%2C%22wishlist%22:1695386453%2C%22faq%22:1695386453%2C%22gtm%22:1695386454%2C%22mst-gtm-addtocart%22:1695386454%2C%22recently_viewed_product%22:1695386453%2C%22recently_compared_product%22:1695386453%2C%22product_data_storage%22:1695386453%2C%22paypal-billing-agreement%22:1695386453}',
            'incap_ses_868_699049': '7tN4NMUSqXZy6YdAqsELDKqSDWUAAAAAvUYxoanRFNe90OGSbdMxWg==',
            '_ga_P9JBZMY5X5': 'GS1.1.1695385819.3.1.1695388335.53.0.0',
            '_clsk': 'tywusf|1695389831469|21|1|z.clarity.ms/collect',
        }
        # this is headers for scrap data on site
        headers = {
            'authority': 'www.mencom.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'visid_incap_699049=CQfjeuDYQ+CGmcWxK6GynGcrDGUAAAAAQUIPAAAAAAAqEMSjlcfDQEL3oOfgUJL3; _lfa=LF1.1.b95df4f6f318cd57.1695296365284; incap_ses_883_699049=0FCHHBHR6z6YSFFU4AtBDH0sDGUAAAAAObG4hWSI9ePOGMDO+41MYg==; user_allowed_save_cookie=%7B%221%22%3A1%7D; _gid=GA1.2.450611667.1695296673; _clck=9zca6p|2|ff8|0|1359; searchReport-log=0; incap_ses_715_699049=72PdVUXJdjM8rD8CtDHsCTl0DWUAAAAA14xaSTL2WD9ONCbgrVVxDw==; PHPSESSID=d41e4c5202e0013751dc0b9cc608399c; form_key=WCy5ZOuXe6incRPG; mage-cache-sessid=true; mage-messages=; form_key=WCy5ZOuXe6incRPG; _ga_P9JBZMY5X5=deleted; _ga_P9JBZMY5X5=deleted; incap_ses_1364_699049=UALCDOzhJg451m/ToOftEnSJDWUAAAAAElyHC68636C8GL1y2aGrmw==; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2OTUyOTYzNjQsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1lbmNvbS5jb20vcGc3LWJsYWNrLXBsYXN0aWMtbnV0Lmh0bWwifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2OTUzODY0NTAsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1lbmNvbS5jb20vIn19; _ga=GA1.2.907729905.1695296365; aw_popup_viewed_page=%5B%22078a683b1fc100af7f68bdabf091a6323b85d8d5464f780f3ed22c0d7f75b6bd%22%2C%22ea68962f02ad60a2f0074df56c737574a392ddcc543ce87792e351135df60c06%22%2C%22ae11dac5dc5aed05b2d39c51025fc505b8a0e68be50a62eb3bb7c06c4013684e%22%2C%227c526d0ade1c93c3760d3ca35a97e1161ddd84c3b11a760fbe76511e87ca8202%22%2C%228c681521fa6d510339b3c6143d220a2886d967f8393752bb087e3484d7edbee9%22%2C%22b35c57fe1da22473f05988f9e0b56b060b04c1b111cde4b86f4b681b657a1bad%22%2C%227cf33824e7d71f6179affc9bb172538ddc3441e4bbf70287dd5af5cdf79a9211%22%2C%220f88851e395f52198092c87571f9e2ed5c6133ddfbb858fa3de704bed2a19c2e%22%2C%2280413d881bb6f7ed75d595794af71e7c95d11f9f2639256636b3029f67009c92%22%2C%225dbc2f99d4ccd5a251203067f30b9194e22aefcd3e2e32e1d30766a5d9783074%22%2C%2281cc180cdd7c7ea9223a171811012eb8832b74b5219c8700d783f7557d8b7159%22%2C%22c68107f3023464839ef01ca54b87d9693eb2774357687508e32824ae97e3cce5%22%2C%22886894b2bec9b8ff99bca220b9ec08343a7546938ce32f1f2c91cad9286b7cc4%22%2C%2238f948d7207ccca335943dbdd258e840d16a96551c78d7d046b692e7264a7e29%22%5D; private_content_version=2972704f5d86bbf50d703047204721b3; section_data_ids={%22customer%22:1695386453%2C%22compare-products%22:1695386453%2C%22last-ordered-items%22:1695386453%2C%22cart%22:1695386453%2C%22directory-data%22:1695386453%2C%22captcha%22:1695386453%2C%22instant-purchase%22:1695386453%2C%22loggedAsCustomer%22:1695386453%2C%22persistent%22:1695386453%2C%22review%22:1695386453%2C%22wishlist%22:1695386453%2C%22faq%22:1695386453%2C%22gtm%22:1695386454%2C%22mst-gtm-addtocart%22:1695386454%2C%22recently_viewed_product%22:1695386453%2C%22recently_compared_product%22:1695386453%2C%22product_data_storage%22:1695386453%2C%22paypal-billing-agreement%22:1695386453}; incap_ses_868_699049=7tN4NMUSqXZy6YdAqsELDKqSDWUAAAAAvUYxoanRFNe90OGSbdMxWg==; _ga_P9JBZMY5X5=GS1.1.1695385819.3.1.1695388335.53.0.0; _clsk=tywusf|1695389831469|21|1|z.clarity.ms/collect',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }
        # Sent request for get all data from main page
        yield scrapy.Request(url='https://www.mencom.com/',headers=headers,cookies=cookies, callback=self.parse)

    def parse(self, response):
        # for loop for scrape category1 links and name from response
        for iii in response.xpath('//div[@class="header-bottom-left"]//li[@class="item level0  level-top parent"]/a'):
            # create dictionary for store all category name and links
            dict1 = {}
            url = iii.xpath('.//@href').get('')
            if url.startswith('http'):
                cat1_url = url
            else:
                cat1_url = "https://www.mencom.com"+url
            name = ' '.join(iii.xpath('.//text()').getall()).strip()
            dict1[name] = cat1_url
            # check category label 2 is available or not
            if iii.xpath('.//..//ul/li//p[@class="groupdrop-title"]//a'):
                # for loop for scrape category lable 2
                for jjj in iii.xpath('.//..//ul/li//p[@class="groupdrop-title"]//a'):
                    url = jjj.xpath('.//@href').get('')
                    if url.startswith('http'):
                        cat2_url = url
                    else:
                        cat2_url = "https://www.mencom.com" + url
                    name = ' '.join(jjj.xpath('.//text()').getall()).strip()

                    dict1[name] = cat2_url
                    # dict1 copy to dict2
                    dict2 = dict1.copy()
                    # here remove last category from dict1
                    dict1.popitem()

                    # define a header for getting response category lable 2
                    headers = {
                        'authority': 'www.mencom.com',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'en-US,en;q=0.9',
                        'cache-control': 'max-age=0',
                        # 'cookie': 'visid_incap_699049=dFZaad/iSu+6jQfwsn1rGWb8C2UAAAAAQUIPAAAAAABrU4MAWdJ0wJKFyICsYveS; _lfa=LF1.1.cea0141b96b6a32d.1695284329734; _clck=1ae33qb|2|ffb|0|1359; searchReport-log=0; form_key=n1naXgMn6PFyBTHm; user_allowed_save_cookie=%7B%221%22%3A1%7D; _gid=GA1.2.345501821.1695628316; incap_ses_1211_699049=6dplKfhq5xrJbYWaHFfOELA8EWUAAAAAOi3j0wQLdVm/bSTcrDcZGQ==; incap_ses_886_699049=ty02YhEnNgqzqKhkarVLDPs8EWUAAAAAXSj68KlE0SlZ98Yq4LfigQ==; PHPSESSID=a97083c4b1c3c5e3396ef19b8079895c; incap_ses_715_699049=392nP+MKRX2upO4CtDHsCcdMEWUAAAAAHTBo2/OtWr9OazfllZWU4Q==; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; form_key=n1naXgMn6PFyBTHm; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2OTUyODQzMjksInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1lbmNvbS5jb20vIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjk1NjMzMTkxLCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5tZW5jb20uY29tL20yMy1jYWJsZXMtcmVjZXB0YWNsZXMuaHRtbD9wPTMifX0=; _ga=GA1.2.2106215483.1695284330; _gat=1; private_content_version=cc2a8b70a942e8db9bb2e6696ff7f5ec; _clsk=wbbikc|1695633191878|6|1|z.clarity.ms/collect; aw_popup_viewed_page=%5B%22a3b974f7c66c9045be14ca30bf630dade94da04eb1fb48cfac15e8867335e54a%22%2C%221be7f8348027b616f4c0e28126a2436273b25aba2c69f3dfd10badb98aca458d%22%2C%22d1997dbd0fe8d72c9e1ddc70a8dd6799cae5ed79e6409c45f5d1ecde1b927f2e%22%2C%22c6813e9e29cb835031f99857bd41ba9da94028e6d01775cd3d38ab49da5bdb68%22%2C%2255eabe1b3c3fe964f87596aa916f4beedb5d9cfa6897577abfdf63c93128f5ac%22%2C%22b6f4bf337913ad9ef9a26851483e94bbab3cbd0062ed3e1b52cdeee775fbf07b%22%2C%2280413d881bb6f7ed75d595794af71e7c95d11f9f2639256636b3029f67009c92%22%2C%22dfaa96540890092966458bf87fdef340f616a2aa74bbaf361fd187316d89d4e0%22%2C%229ab94a16bd4fd22b33876f75e0adca14a1a273b4d92fe027108ab77e5123946b%22%5D; _ga_P9JBZMY5X5=GS1.1.1695632588.7.1.1695633193.57.0.0; section_data_ids={%22customer%22:1695633192%2C%22compare-products%22:1695633192%2C%22last-ordered-items%22:1695633192%2C%22cart%22:1695633192%2C%22directory-data%22:1695633192%2C%22captcha%22:1695633192%2C%22instant-purchase%22:1695633192%2C%22loggedAsCustomer%22:1695633192%2C%22persistent%22:1695633192%2C%22review%22:1695633192%2C%22wishlist%22:1695633192%2C%22faq%22:1695633192%2C%22gtm%22:1695633193%2C%22mst-gtm-addtocart%22:1695633193%2C%22recently_viewed_product%22:1695633192%2C%22recently_compared_product%22:1695633192%2C%22product_data_storage%22:1695633192%2C%22paypal-billing-agreement%22:1695633192}',
                        'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41',
                    }
                    # sent request category lable 2
                    yield scrapy.Request(url=cat2_url,
                                         headers=headers,
                                         # cookies=cookies,
                                         callback=self.parse,meta={'list1' :dict2})

            else:
                # define headers
                headers = {
                    'authority': 'www.mencom.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    # 'cookie': 'visid_incap_699049=dFZaad/iSu+6jQfwsn1rGWb8C2UAAAAAQUIPAAAAAABrU4MAWdJ0wJKFyICsYveS; _lfa=LF1.1.cea0141b96b6a32d.1695284329734; _clck=1ae33qb|2|ffb|0|1359; searchReport-log=0; form_key=n1naXgMn6PFyBTHm; user_allowed_save_cookie=%7B%221%22%3A1%7D; _gid=GA1.2.345501821.1695628316; incap_ses_1211_699049=6dplKfhq5xrJbYWaHFfOELA8EWUAAAAAOi3j0wQLdVm/bSTcrDcZGQ==; incap_ses_886_699049=ty02YhEnNgqzqKhkarVLDPs8EWUAAAAAXSj68KlE0SlZ98Yq4LfigQ==; PHPSESSID=a97083c4b1c3c5e3396ef19b8079895c; incap_ses_715_699049=392nP+MKRX2upO4CtDHsCcdMEWUAAAAAHTBo2/OtWr9OazfllZWU4Q==; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; form_key=n1naXgMn6PFyBTHm; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2OTUyODQzMjksInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1lbmNvbS5jb20vIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjk1NjMzMTkxLCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5tZW5jb20uY29tL20yMy1jYWJsZXMtcmVjZXB0YWNsZXMuaHRtbD9wPTMifX0=; _ga=GA1.2.2106215483.1695284330; _gat=1; private_content_version=cc2a8b70a942e8db9bb2e6696ff7f5ec; _clsk=wbbikc|1695633191878|6|1|z.clarity.ms/collect; aw_popup_viewed_page=%5B%22a3b974f7c66c9045be14ca30bf630dade94da04eb1fb48cfac15e8867335e54a%22%2C%221be7f8348027b616f4c0e28126a2436273b25aba2c69f3dfd10badb98aca458d%22%2C%22d1997dbd0fe8d72c9e1ddc70a8dd6799cae5ed79e6409c45f5d1ecde1b927f2e%22%2C%22c6813e9e29cb835031f99857bd41ba9da94028e6d01775cd3d38ab49da5bdb68%22%2C%2255eabe1b3c3fe964f87596aa916f4beedb5d9cfa6897577abfdf63c93128f5ac%22%2C%22b6f4bf337913ad9ef9a26851483e94bbab3cbd0062ed3e1b52cdeee775fbf07b%22%2C%2280413d881bb6f7ed75d595794af71e7c95d11f9f2639256636b3029f67009c92%22%2C%22dfaa96540890092966458bf87fdef340f616a2aa74bbaf361fd187316d89d4e0%22%2C%229ab94a16bd4fd22b33876f75e0adca14a1a273b4d92fe027108ab77e5123946b%22%5D; _ga_P9JBZMY5X5=GS1.1.1695632588.7.1.1695633193.57.0.0; section_data_ids={%22customer%22:1695633192%2C%22compare-products%22:1695633192%2C%22last-ordered-items%22:1695633192%2C%22cart%22:1695633192%2C%22directory-data%22:1695633192%2C%22captcha%22:1695633192%2C%22instant-purchase%22:1695633192%2C%22loggedAsCustomer%22:1695633192%2C%22persistent%22:1695633192%2C%22review%22:1695633192%2C%22wishlist%22:1695633192%2C%22faq%22:1695633192%2C%22gtm%22:1695633193%2C%22mst-gtm-addtocart%22:1695633193%2C%22recently_viewed_product%22:1695633192%2C%22recently_compared_product%22:1695633192%2C%22product_data_storage%22:1695633192%2C%22paypal-billing-agreement%22:1695633192}',
                    'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41',
                }

                yield scrapy.Request(url=cat1_url,
                                     headers=headers,
                                     # cookies=cookies,
                                     callback=self.parse, meta={'list1': dict1})
        # check response is product listing page or not
        if response.xpath('//li[@class="item product product-item"]'):
            # get all category hirechy from meta data
            meta_data = response.meta.get('list1')
            # for loop for getting product links
            for pl in response.xpath('//li[@class="item product product-item"]//a[@class="product-item-link"]'):
                url = pl.xpath('.//@href').get('')
                if url.startswith('http'):
                    pro_url = url
                else:
                    pro_url = "https://www.mencom.com" + url
                # define item for store data
                item = IcsV1SiteMapLinksItem()

                item['vendor_id'] = self.VENDOR_ID
                item['vendor_name'] = self.VENDOR_NAME
                item['product_urls'] = pro_url
                item['meta_data'] = json.dumps(meta_data)
                # yield item for sent all data which is store in item and sent item in pipelines.py
                yield item
            #  check product listing page is store pagination or not
            if response.xpath('//div[contains(@class,"grid products-grid")]//following-sibling::div//div[@class="pages"]'):
                # for loop for getting pagination links
                for page in response.xpath('//div[contains(@class,"grid products-grid")]//following-sibling::div//div[@class="pages"]//li[@class="item current"]//following-sibling::li//a'):
                    next_page = page.xpath('.//@href').get('')

                    if next_page.startswith('http'):
                        next_url = next_page
                    else:
                        next_url = "https://www.mencom.com" + next_page
                    # cookies for getting response on next page data
                    cookies = {
                        'visid_incap_699049': 'dFZaad/iSu+6jQfwsn1rGWb8C2UAAAAAQUIPAAAAAABrU4MAWdJ0wJKFyICsYveS',
                        '_lfa': 'LF1.1.cea0141b96b6a32d.1695284329734',
                        '_clck': '1ae33qb|2|ffb|0|1359',
                        'searchReport-log': '0',
                        'incap_ses_715_699049': 'NQzyI3ohDwMVkOcCtDHsCTU6EWUAAAAAtNB3qZuwpbH0A6Phmoww8Q==',
                        'form_key': 'n1naXgMn6PFyBTHm',
                        'mage-cache-storage': '{}',
                        'mage-cache-storage-section-invalidation': '{}',
                        'mage-messages': '',
                        'recently_viewed_product': '{}',
                        'recently_viewed_product_previous': '{}',
                        'recently_compared_product': '{}',
                        'recently_compared_product_previous': '{}',
                        'product_data_storage': '{}',
                        'form_key': 'n1naXgMn6PFyBTHm',
                        'PHPSESSID': 'fc485996688e2e482a24d2413ad8ca1a',
                        'mage-cache-sessid': 'true',
                        'user_allowed_save_cookie': '%7B%221%22%3A1%7D',
                        '_gid': 'GA1.2.345501821.1695628316',
                        'incap_ses_1211_699049': '6dplKfhq5xrJbYWaHFfOELA8EWUAAAAAOi3j0wQLdVm/bSTcrDcZGQ==',
                        'incap_ses_886_699049': 'ty02YhEnNgqzqKhkarVLDPs8EWUAAAAAXSj68KlE0SlZ98Yq4LfigQ==',
                        '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2OTUyODQzMjksInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1lbmNvbS5jb20vIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjk1NjI4NTQxLCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5tZW5jb20uY29tL2NpcmN1bGFyLW1pbC1zcGVjLWNvbm5lY3RvcnMuaHRtbD9wPTUifX0=',
                        '_ga': 'GA1.2.2106215483.1695284330',
                        '_gat': '1',
                        '_clsk': 'ljuumm|1695628544345|9|1|z.clarity.ms/collect',
                        'aw_popup_viewed_page': '%5B%22a3b974f7c66c9045be14ca30bf630dade94da04eb1fb48cfac15e8867335e54a%22%2C%221be7f8348027b616f4c0e28126a2436273b25aba2c69f3dfd10badb98aca458d%22%2C%22d1997dbd0fe8d72c9e1ddc70a8dd6799cae5ed79e6409c45f5d1ecde1b927f2e%22%2C%22c6813e9e29cb835031f99857bd41ba9da94028e6d01775cd3d38ab49da5bdb68%22%2C%2255eabe1b3c3fe964f87596aa916f4beedb5d9cfa6897577abfdf63c93128f5ac%22%5D',
                        '_ga_P9JBZMY5X5': 'GS1.1.1695627829.6.1.1695628545.56.0.0',
                        'private_content_version': '9e3acc520ac1cdf08f5980c5671c3dc8',
                        'section_data_ids': '{%22gtm%22:1695628546%2C%22mst-gtm-addtocart%22:1695628546%2C%22customer%22:1695628544%2C%22compare-products%22:1695628544%2C%22last-ordered-items%22:1695628544%2C%22cart%22:1695628544%2C%22directory-data%22:1695628544%2C%22captcha%22:1695628544%2C%22instant-purchase%22:1695628544%2C%22loggedAsCustomer%22:1695628544%2C%22persistent%22:1695628544%2C%22review%22:1695628544%2C%22wishlist%22:1695628544%2C%22faq%22:1695628544%2C%22recently_viewed_product%22:1695628544%2C%22recently_compared_product%22:1695628544%2C%22product_data_storage%22:1695628544%2C%22paypal-billing-agreement%22:1695628544}',
                    }

                    headers = {
                        'authority': 'www.mencom.com',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'en-US,en;q=0.9',
                        'cache-control': 'max-age=0',
                        # 'cookie': 'visid_incap_699049=dFZaad/iSu+6jQfwsn1rGWb8C2UAAAAAQUIPAAAAAABrU4MAWdJ0wJKFyICsYveS; _lfa=LF1.1.cea0141b96b6a32d.1695284329734; _clck=1ae33qb|2|ffb|0|1359; searchReport-log=0; form_key=n1naXgMn6PFyBTHm; user_allowed_save_cookie=%7B%221%22%3A1%7D; _gid=GA1.2.345501821.1695628316; incap_ses_1211_699049=6dplKfhq5xrJbYWaHFfOELA8EWUAAAAAOi3j0wQLdVm/bSTcrDcZGQ==; incap_ses_886_699049=ty02YhEnNgqzqKhkarVLDPs8EWUAAAAAXSj68KlE0SlZ98Yq4LfigQ==; PHPSESSID=a97083c4b1c3c5e3396ef19b8079895c; incap_ses_715_699049=392nP+MKRX2upO4CtDHsCcdMEWUAAAAAHTBo2/OtWr9OazfllZWU4Q==; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; form_key=n1naXgMn6PFyBTHm; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2OTUyODQzMjksInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1lbmNvbS5jb20vIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjk1NjMzMTkxLCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5tZW5jb20uY29tL20yMy1jYWJsZXMtcmVjZXB0YWNsZXMuaHRtbD9wPTMifX0=; _ga=GA1.2.2106215483.1695284330; _gat=1; private_content_version=cc2a8b70a942e8db9bb2e6696ff7f5ec; _clsk=wbbikc|1695633191878|6|1|z.clarity.ms/collect; aw_popup_viewed_page=%5B%22a3b974f7c66c9045be14ca30bf630dade94da04eb1fb48cfac15e8867335e54a%22%2C%221be7f8348027b616f4c0e28126a2436273b25aba2c69f3dfd10badb98aca458d%22%2C%22d1997dbd0fe8d72c9e1ddc70a8dd6799cae5ed79e6409c45f5d1ecde1b927f2e%22%2C%22c6813e9e29cb835031f99857bd41ba9da94028e6d01775cd3d38ab49da5bdb68%22%2C%2255eabe1b3c3fe964f87596aa916f4beedb5d9cfa6897577abfdf63c93128f5ac%22%2C%22b6f4bf337913ad9ef9a26851483e94bbab3cbd0062ed3e1b52cdeee775fbf07b%22%2C%2280413d881bb6f7ed75d595794af71e7c95d11f9f2639256636b3029f67009c92%22%2C%22dfaa96540890092966458bf87fdef340f616a2aa74bbaf361fd187316d89d4e0%22%2C%229ab94a16bd4fd22b33876f75e0adca14a1a273b4d92fe027108ab77e5123946b%22%5D; _ga_P9JBZMY5X5=GS1.1.1695632588.7.1.1695633193.57.0.0; section_data_ids={%22customer%22:1695633192%2C%22compare-products%22:1695633192%2C%22last-ordered-items%22:1695633192%2C%22cart%22:1695633192%2C%22directory-data%22:1695633192%2C%22captcha%22:1695633192%2C%22instant-purchase%22:1695633192%2C%22loggedAsCustomer%22:1695633192%2C%22persistent%22:1695633192%2C%22review%22:1695633192%2C%22wishlist%22:1695633192%2C%22faq%22:1695633192%2C%22gtm%22:1695633193%2C%22mst-gtm-addtocart%22:1695633193%2C%22recently_viewed_product%22:1695633192%2C%22recently_compared_product%22:1695633192%2C%22product_data_storage%22:1695633192%2C%22paypal-billing-agreement%22:1695633192}',
                        'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41',
                    }
                    # sent request in next page
                    yield scrapy.Request(url=next_url,headers=headers,cookies=cookies, callback=self.parse, meta={'list1': meta_data})


# for run this file
if __name__ == '__main__':
    # cammand line for running this spider
    execute('scrapy crawl mancom_new_links'.split())
