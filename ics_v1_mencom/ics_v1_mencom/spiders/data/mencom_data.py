

import scrapy
import hashlib
import json
import os.path

import re,time

from datetime import datetime


import pymysql
from itemloaders import ItemLoader
from itemloaders.processors import TakeFirst
from scrapy.cmdline import execute

import html

import ics_v1_mencom.db_config as db
from ics_v1_mencom.items import IcsV1AssetItem, IcsV1PricingItem, IcsV1PDPItem



def check_status(x):
    return True if x else False


cookies = {
    'searchReport-log': '0',
    'visid_incap_699049': 'tg8LHGydT5y7ecvqeRnnteAaFGUAAAAAQUIPAAAAAAC4R6z/4mIhcrZAwVEAV0V2',
    'incap_ses_281_699049': 'PhLkXo8dQ0JdYzZ1xlDmA+IaFGUAAAAAaOTjDjTbe2RRtdjaNP0l7w==',
    '_clck': '6vtq5l|2|ffd|0|1365',
    '_ga': 'GA1.1.1776158744.1695816423',
    '_lfa': 'LF1.1.f8ec69c5a2b5a588.1695816423188',
    'PHPSESSID': 'be7df770ee993d18450b255d6fb0ad38',
    'aw_popup_viewed_page': '%5B%2267d9d7c3fa8b5726b8723723052d66c27eff814aed47a77741845b4d09300c58%22%5D',
    'form_key': '6DpRMzyGMu3sFXvE',
    'mage-cache-storage': '{}',
    'mage-cache-storage-section-invalidation': '{}',
    'mage-cache-sessid': 'true',
    'form_key': '6DpRMzyGMu3sFXvE',
    'mage-messages': '',
    'recently_viewed_product': '{}',
    'recently_viewed_product_previous': '{}',
    'recently_compared_product': '{}',
    'recently_compared_product_previous': '{}',
    'product_data_storage': '{}',
    '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2OTU4MTY0MjIsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1lbmNvbS5jb20vY2lyY3VsYXItbWlsLXNwZWMtY29ubmVjdG9ycy9taWwtc3BlYy1zaXplLTE4LTVkLWNvcmRzZXQtNS1wb2xlLW1hbGUtc3RyYWlnaHQtMm0tOGEteWVsbG93LXB2Yy5odG1sIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjk1ODE2NDQ3LCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5tZW5jb20uY29tL2NpcmN1bGFyLW1pbC1zcGVjLWNvbm5lY3RvcnMvbWlsLXNwZWMtc2l6ZS0xOC01ZC1jb3Jkc2V0LTUtcG9sZS1tYWxlLXN0cmFpZ2h0LTJtLThhLXllbGxvdy1wdmMuaHRtbCJ9fQ==',
    '_clsk': '1jehf1p|1695816448768|2|1|v.clarity.ms/collect',
    'private_content_version': 'c7c2a5d66438b81ef30b369513645cdd',
    '_ga_P9JBZMY5X5': 'GS1.1.1695816422.1.1.1695816456.26.0.0',
    'section_data_ids': '{%22customer%22:1695816453%2C%22compare-products%22:1695816453%2C%22last-ordered-items%22:1695816453%2C%22cart%22:1695816453%2C%22directory-data%22:1695816453%2C%22captcha%22:1695816453%2C%22instant-purchase%22:1695816453%2C%22loggedAsCustomer%22:1695816453%2C%22persistent%22:1695816453%2C%22review%22:1695816453%2C%22wishlist%22:1695816453%2C%22faq%22:1695816453%2C%22gtm%22:1695816455%2C%22mst-gtm-addtocart%22:1695816456%2C%22recently_viewed_product%22:1695816453%2C%22recently_compared_product%22:1695816453%2C%22product_data_storage%22:1695816453%2C%22paypal-billing-agreement%22:1695816453}',
}

headers = {
    'authority': 'www.mencom.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'searchReport-log=0; visid_incap_699049=tg8LHGydT5y7ecvqeRnnteAaFGUAAAAAQUIPAAAAAAC4R6z/4mIhcrZAwVEAV0V2; incap_ses_281_699049=PhLkXo8dQ0JdYzZ1xlDmA+IaFGUAAAAAaOTjDjTbe2RRtdjaNP0l7w==; _clck=6vtq5l|2|ffd|0|1365; _ga=GA1.1.1776158744.1695816423; _lfa=LF1.1.f8ec69c5a2b5a588.1695816423188; PHPSESSID=be7df770ee993d18450b255d6fb0ad38; aw_popup_viewed_page=%5B%2267d9d7c3fa8b5726b8723723052d66c27eff814aed47a77741845b4d09300c58%22%5D; form_key=6DpRMzyGMu3sFXvE; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; form_key=6DpRMzyGMu3sFXvE; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2OTU4MTY0MjIsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1lbmNvbS5jb20vY2lyY3VsYXItbWlsLXNwZWMtY29ubmVjdG9ycy9taWwtc3BlYy1zaXplLTE4LTVkLWNvcmRzZXQtNS1wb2xlLW1hbGUtc3RyYWlnaHQtMm0tOGEteWVsbG93LXB2Yy5odG1sIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjk1ODE2NDQ3LCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5tZW5jb20uY29tL2NpcmN1bGFyLW1pbC1zcGVjLWNvbm5lY3RvcnMvbWlsLXNwZWMtc2l6ZS0xOC01ZC1jb3Jkc2V0LTUtcG9sZS1tYWxlLXN0cmFpZ2h0LTJtLThhLXllbGxvdy1wdmMuaHRtbCJ9fQ==; _clsk=1jehf1p|1695816448768|2|1|v.clarity.ms/collect; private_content_version=c7c2a5d66438b81ef30b369513645cdd; _ga_P9JBZMY5X5=GS1.1.1695816422.1.1.1695816456.26.0.0; section_data_ids={%22customer%22:1695816453%2C%22compare-products%22:1695816453%2C%22last-ordered-items%22:1695816453%2C%22cart%22:1695816453%2C%22directory-data%22:1695816453%2C%22captcha%22:1695816453%2C%22instant-purchase%22:1695816453%2C%22loggedAsCustomer%22:1695816453%2C%22persistent%22:1695816453%2C%22review%22:1695816453%2C%22wishlist%22:1695816453%2C%22faq%22:1695816453%2C%22gtm%22:1695816455%2C%22mst-gtm-addtocart%22:1695816456%2C%22recently_viewed_product%22:1695816453%2C%22recently_compared_product%22:1695816453%2C%22product_data_storage%22:1695816453%2C%22paypal-billing-agreement%22:1695816453}',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}
# Define class for scrap mencom data
class MencomDataSpider(scrapy.Spider):
    # define spider name
    name = "mancom_data"
    # Define vendor_id
    VENDOR_ID = "ACT-B7-002"
    # Define vendor_name
    VENDOR_NAME = "Mencom"
    # Define page save path for save pdp page
    page_save = 'E:/Ankit_Live/working_live/HTMLS/mencom/pdp/' + VENDOR_ID + "-" + VENDOR_NAME + "/"
    # for handle status code list
    # handle_httpstatus_list = [404, 429, 403, 429, 520, 400, 401, 503]
    # define inite function and it is take argument start and end
    def __init__(self, name=None, start='', end='', **kwargs):
        super().__init__(name, **kwargs)
        # DATABASE CONNECTION
        self.con = pymysql.connect(host=db.db_host, user=db.db_user, password=db.db_password, db=db.db_name)
        self.cursor = self.con.cursor()
        if not os.path.exists(self.page_save):
            os.makedirs(self.page_save)
        # assign start and end arguement
        self.start = start
        self.end = end


    # Define start_requests functions for sending pdp request
    def start_requests(self):
        # write query for fetch all data which i want
        select_query = [
            f"select id, product_urls,meta_data from {db.sitemap_table} where",
            f"vendor_id = '{self.VENDOR_ID}'and ",
            f"status = 'pending' and ",
            f"id between {self.start} and {self.end}"
        ]
        # query execute for getting all data
        self.cursor.execute(" ".join(select_query))
        # for loop for fetching all data one by one
        for data in self.cursor.fetchall():
            url = data[1]
            # make page save path using id
            file_name = f'{self.page_save}{data[0]}.html'
            # check is page save already saved or not
            if os.path.exists(file_name):
                yield scrapy.FormRequest(url=f'file:///{file_name}', callback=self.parse,meta={'product_url': url},cb_kwargs={"id": data[0],'meta_data':data[2]})
            else:
                yield scrapy.Request(url=url,callback=self.parse,headers=headers,cookies=cookies,meta={'product_url': url},cb_kwargs={"id": data[0],'meta_data':data[2]})


    # making parse functions which is take arguement response and kwargs keyword and getting all response which is came from start_requests functions
    def parse(self, response, **kwargs):
        # getting product_url from meta
        pro_url = response.meta.get('product_url')
        # making hashkey which is unique of every product
        hash_key = hashlib.sha256(pro_url.encode()).hexdigest()
        id = kwargs['id']
        meta_data = kwargs['meta_data']
        # check response is 200 or not
        if response.status == 200:
            # if response status is 200 then write code for page saving
            open(self.page_save + str(id) + ".html", "wb").write(response.body)
            # create a product loader which is store all data of product_table
            product_loader = ItemLoader(item=IcsV1PDPItem(), selector=response)
            product_loader.default_output_processor = TakeFirst()
            # for getting name value
            product_name = response.xpath("//div[@class='page-title-wrapper product']/h1/span/text()").get('')
            if product_name:
                # remove junk char from the name
                product_name = html.unescape(product_name).strip()
            # add every value in product loader
            product_loader.add_value('id', id)
            product_loader.add_value('vendor_id', self.VENDOR_ID)
            product_loader.add_value('vendor_name', self.VENDOR_NAME)
            product_loader.add_value('hash_key', hash_key)
            product_loader.add_value('pdp_url', pro_url)
            product_loader.add_value('name', product_name)
            # write xpath for getting sku value
            sku1= response.xpath("//div[@class='product attribute sku']/div[@class='value']/text()").get('')
            if sku1:
                sku = html.unescape(sku1).strip()
            product_loader.add_value('sku', sku)
            product_loader.add_value('manufacturer', "Mencom")
            # write xpath for getting instock is available or not
            in_stock = ' '.join(response.xpath("//div[@class='product-info-stock-sku']//span//text()").getall())
            if in_stock:
                if "stock" in in_stock.lower():
                    in_stock = True
                else:
                    in_stock = False
                product_loader.add_value('in_stock', in_stock)
            # write xpath for checking add to cart button is available or not
            available = ' '.join(response.xpath('//div[contains(@class,"tocart")]//button//text()').getall())
            if available:
                if 'add to cart' in available.lower():
                    available_to_checkout = True
                else:
                    available_to_checkout = False
            else:
                available_to_checkout = False
            product_loader.add_value('available_to_checkout', available_to_checkout)

            # write xpath getting descripion value
            desc = response.xpath("//div[@class='product attribute description']//div[@class='value']//text()").getall()
            # write xpath for getting description html
            desc_html  = response.xpath("//div[@class='product attribute description']//div[@class='value']").getall()
            # remove unnecessary space from the description
            desc = re.sub(' +',' '," ".join(desc).strip())
            # remove unnecessary space from the description html
            desc_html = " ".join(desc_html).strip()
            product_loader.add_value('description_html',html.unescape(desc_html))

            product_loader.add_value('description',html.unescape(desc))
            # create mt dictionary for stor category name and category url
            scrape_metadata = dict()
            scrape_metadata['url'] = pro_url
            # create mt list for store category name and url
            breadcrumbs = list()
            dic_home = {"url": "https://www.mencom.com/",
                        "name": "Home"
                        }


            breadcrumbs.append(dic_home)
            category = []
            for ii in list(eval(meta_data).items()):

                category.append(ii[0])
                breadcrumbs.append({
                    "name": ii[0],
                    "url": ii[1]
                })



            product_loader.add_value('category', category)

            product_loader.replace_value('category', json.dumps(product_loader.get_collected_values('category')),ensure_ascii=False)

            scrape_metadata['breadcrumbs'] = breadcrumbs
            # for getting current date time value
            scrape_metadata['date_visited'] = str(datetime.now()).replace(" ", "T")[:-3] + "Z"

            product_loader.add_value('_scrape_metadata', json.dumps(scrape_metadata))
            # making mt list for store attributes value
            attributes = list()
            atr=response.xpath("//div[@class='additional-attributes-wrapper table-wrapper']//table[@class='data table additional-attributes']//tbody/tr")
            for attribute in atr:
                name = attribute.xpath(".//th//text()").get('').strip()

                value = attribute.xpath("./td/text()").get('').strip()
                if value:
                    value = value
                else:
                    value = ' '
                if name:
                    attributes.append({
                        'name': name,
                        'value': html.unescape(value),
                        'group': 'Specifications',
                    })


            product_loader.add_value('attributes', json.dumps(attributes))

            product_loader.add_value('status', 'Done')
            # here finish prodoct table data
            # ----------------------------------------------------------------------------------------------
            # EXTRACTING PRICES
            # here create new product loader for store price value
            pricing_loaders = ItemLoader(item=IcsV1PricingItem(), selector=response)
            pricing_loaders.default_output_processor = TakeFirst()
            # xpath for getting price
            price = response.xpath("//div[@class='product-info-price']//span[@class='price']/text()").get('')
            # define minimum quentity
            qty = 1
            pricing_loaders.add_value('vendor_id', self.VENDOR_ID)
            pricing_loaders.add_value('sku', sku)
            pricing_loaders.add_value('hash_key', hash_key)
            pricing_loaders.add_value('currency', "USD")
            pricing_loaders.add_value('min_qty', qty)
            # check if price is available or not
            if price:
                # if price then remove doller sign from the price value
                price = price.replace("$", "").strip()
                pricing_loaders.add_value('price', price)
            # if price is not available then price string = 'Call for price'
            else:
                price_str = "Call For Price"
                pricing_loaders.add_value('price_string', price_str)
            yield pricing_loaders.load_item()
    #       here finish pricing table work
    # ----------------------------------------------------------------------------
            # # ASSET STORING
            # create item for store main image and other images and pdf and other documens
            item = IcsV1AssetItem()
            item['vendor_id'] = self.VENDOR_ID
            item['hash_key'] = hash_key
            item['sku'] = sku
            # for getting product image
            product_image= response.xpath('//script[contains(text(),"mage/gallery/gallery")]//text()').get('').strip()
            image_count = 1
            if product_image:
                image_data = json.loads(product_image)
                # for loop for getting all product images
                for ig in image_data.get('[data-gallery-role=gallery-placeholder]').get('mage/gallery/gallery').get('data'):
                    img_url = ig.get('full')
                    name = ig.get('caption')
                    type = ig.get('type')
                    if type.lower() == 'image' and "placeholder" not in img_url.lower():
                        image_item = item.copy()
                        if image_count == 1:
                            image_item['is_main_image'] = True
                        image_item['source'] = img_url
                        image_item['name'] = html.unescape(name).strip()
                        image_item['file_name'] = image_item['source'].split("?")[0].split("/")[-1]
                        image_item['type'] = 'image/product'
                        image_count +=1
            # for getting all documents
            document = response.xpath("//div[contains(@class,'attachment')]//ul//li")
            # image item copying
            image_item = item.copy()
            # for loop for getting all document
            for doc in document:

                source_doc = doc.xpath(".//a/@href").get('')
                source_name = re.sub(' +', ' ', html.unescape(' '.join(doc.xpath(".//text()").getall())).replace('\xa0','').strip())
                image_item['source'] = source_doc
                image_item['name'] = source_name

                source_fname = html.unescape(' '.join(doc.xpath(".//a//text()").getall()))
                image_item['file_name'] = image_item['source'].split("?")[0].split("/")[-1]
                if '.pdf' in source_fname.lower():
                    image_item['type'] = 'document/catalog'
                elif '.dwg' in source_fname.lower() or '.dxf' in source_fname.lower():
                    image_item['type'] = 'cad/2D'
                elif '.zip' in source_fname.lower():
                    image_item['type'] = 'cad/3D'

                yield image_item
            #     here asset table work is complate
            yield product_loader.load_item()
#             here i am yielding product loader
#


# for execute this spider
if __name__ == '__main__':
    # cammand line for running this file and giving start and end value
    execute("scrapy crawl mancom_data -a start=1 -a end=10000000".split())