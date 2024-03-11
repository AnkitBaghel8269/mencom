import os.path

import pymysql
import scrapy
from scrapy.cmdline import execute
from scrapy.utils.response import open_in_browser
import hashlib
cookies = {
    'searchReport-log': '0',
    'visid_incap_699049': 'zKJhDY1aSh2g64NGGrjLan50DWUAAAAAQUIPAAAAAACBV9fFX1csizKXQ6289b9p',
    'incap_ses_715_699049': 'BLMRLTHhO3sKxD8CtDHsCYB0DWUAAAAAuPmXhcc8eguE54hI29hjKA==',
    '_clck': '18x5iry|2|ff8|0|1360',
    '_lfa': 'LF1.1.79c4f9c4f6b9af20.1695380606418',
    '_ga': 'GA1.1.1773664088.1695380606',
    'PHPSESSID': 'b8fc930db3d33ff3cb7d10d9ba49dc25',
    'form_key': 'K9GMUnPpymzayswC',
    'mage-cache-storage': '{}',
    'mage-cache-storage-section-invalidation': '{}',
    'mage-cache-sessid': 'true',
    'mage-messages': '',
    'form_key': 'K9GMUnPpymzayswC',
    'recently_viewed_product': '{}',
    'recently_viewed_product_previous': '{}',
    'recently_compared_product': '{}',
    'recently_compared_product_previous': '{}',
    'product_data_storage': '{}',
    'incap_ses_883_699049': 'DG4MCuCqWjpcPbhV4AtBDJ50DWUAAAAAOtc+GFN6Wy46SkOy8W9uww==',
    'aw_popup_viewed_page': '%5B%220f598c7907dd95da4956d0bacc76c47ebb35a2c7db661f473fae1ce97aa2540f%22%2C%22c01c48e3378f659b45a8135d13ecdfc8c3d29484d0b21592fdacd5b84d41b13c%22%2C%220f88851e395f52198092c87571f9e2ed5c6133ddfbb858fa3de704bed2a19c2e%22%2C%2280413d881bb6f7ed75d595794af71e7c95d11f9f2639256636b3029f67009c92%22%2C%22ea68962f02ad60a2f0074df56c737574a392ddcc543ce87792e351135df60c06%22%2C%22f3b32dd7465624a317e85d9b1760c0f2d8e1cce44fc77da22110abd730b2d152%22%5D',
    'incap_ses_1548_699049': '7K3hVb0GB10RjeHEVZp7Fbt3DWUAAAAApZngxoEuuZ8zJqBsbnM2/w==',
    '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2OTUzODA2MDYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1lbmNvbS5jb20vc29sZW5vaWQtdmFsdmUtY29ubmVjdG9ycy5odG1sIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjk1MzgxNDkyLCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5tZW5jb20uY29tL3NvbGVub2lkLXZhbHZlLWNvbm5lY3RvcnMuaHRtbCJ9fQ==',
    '_clsk': 'mzimkz|1695381492967|14|1|z.clarity.ms/collect',
    'private_content_version': '9de18729a2723e2677ce27378d104190',
    '_ga_P9JBZMY5X5': 'GS1.1.1695380606.1.1.1695381494.59.0.0',
    'section_data_ids': '{%22customer%22:1695381497%2C%22compare-products%22:1695381497%2C%22last-ordered-items%22:1695381497%2C%22cart%22:1695381497%2C%22directory-data%22:1695381497%2C%22captcha%22:1695381497%2C%22instant-purchase%22:1695381497%2C%22loggedAsCustomer%22:1695381497%2C%22persistent%22:1695381497%2C%22review%22:1695381497%2C%22wishlist%22:1695381497%2C%22faq%22:1695381497%2C%22gtm%22:1695381498%2C%22mst-gtm-addtocart%22:1695381498%2C%22recently_viewed_product%22:1695381497%2C%22recently_compared_product%22:1695381497%2C%22product_data_storage%22:1695381497%2C%22paypal-billing-agreement%22:1695381497}',
}

headers = {
    'authority': 'www.mencom.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'searchReport-log=0; visid_incap_699049=zKJhDY1aSh2g64NGGrjLan50DWUAAAAAQUIPAAAAAACBV9fFX1csizKXQ6289b9p; incap_ses_715_699049=BLMRLTHhO3sKxD8CtDHsCYB0DWUAAAAAuPmXhcc8eguE54hI29hjKA==; _clck=18x5iry|2|ff8|0|1360; _lfa=LF1.1.79c4f9c4f6b9af20.1695380606418; _ga=GA1.1.1773664088.1695380606; PHPSESSID=b8fc930db3d33ff3cb7d10d9ba49dc25; form_key=K9GMUnPpymzayswC; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; form_key=K9GMUnPpymzayswC; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; incap_ses_883_699049=DG4MCuCqWjpcPbhV4AtBDJ50DWUAAAAAOtc+GFN6Wy46SkOy8W9uww==; aw_popup_viewed_page=%5B%220f598c7907dd95da4956d0bacc76c47ebb35a2c7db661f473fae1ce97aa2540f%22%2C%22c01c48e3378f659b45a8135d13ecdfc8c3d29484d0b21592fdacd5b84d41b13c%22%2C%220f88851e395f52198092c87571f9e2ed5c6133ddfbb858fa3de704bed2a19c2e%22%2C%2280413d881bb6f7ed75d595794af71e7c95d11f9f2639256636b3029f67009c92%22%2C%22ea68962f02ad60a2f0074df56c737574a392ddcc543ce87792e351135df60c06%22%2C%22f3b32dd7465624a317e85d9b1760c0f2d8e1cce44fc77da22110abd730b2d152%22%5D; incap_ses_1548_699049=7K3hVb0GB10RjeHEVZp7Fbt3DWUAAAAApZngxoEuuZ8zJqBsbnM2/w==; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2OTUzODA2MDYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1lbmNvbS5jb20vc29sZW5vaWQtdmFsdmUtY29ubmVjdG9ycy5odG1sIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjk1MzgxNDkyLCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5tZW5jb20uY29tL3NvbGVub2lkLXZhbHZlLWNvbm5lY3RvcnMuaHRtbCJ9fQ==; _clsk=mzimkz|1695381492967|14|1|z.clarity.ms/collect; private_content_version=9de18729a2723e2677ce27378d104190; _ga_P9JBZMY5X5=GS1.1.1695380606.1.1.1695381494.59.0.0; section_data_ids={%22customer%22:1695381497%2C%22compare-products%22:1695381497%2C%22last-ordered-items%22:1695381497%2C%22cart%22:1695381497%2C%22directory-data%22:1695381497%2C%22captcha%22:1695381497%2C%22instant-purchase%22:1695381497%2C%22loggedAsCustomer%22:1695381497%2C%22persistent%22:1695381497%2C%22review%22:1695381497%2C%22wishlist%22:1695381497%2C%22faq%22:1695381497%2C%22gtm%22:1695381498%2C%22mst-gtm-addtocart%22:1695381498%2C%22recently_viewed_product%22:1695381497%2C%22recently_compared_product%22:1695381497%2C%22product_data_storage%22:1695381497%2C%22paypal-billing-agreement%22:1695381497}',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

from ics_v1_mencom import db_config as db
class DownloadAssestSpider(scrapy.Spider):
    name = 'download_assest'
    assets_save = 'E:/Work/Actowiz/pages/ics/assets/'

    def __init__(self,start="",end="", name=None, vendor_id="ACT-B7-002", **kwargs):
        super().__init__(name, **kwargs)
        if not vendor_id:
            exit(-1)
        self.start = start
        self.end = end
        self.VENDOR_ID = vendor_id
        self.assets_save += vendor_id + "/"
        if not os.path.exists(self.assets_save):
            os.makedirs(self.assets_save)

        self.con = pymysql.connect(host=db.db_host, user=db.db_user, password=db.db_password, db=db.db_name)
        self.cursor = self.con.cursor()

    def start_requests(self):
        select_query = [
            f"select id, source, file_name, is_main_image, name, type from {db.asset_table} where",
            f"vendor_id = '{self.VENDOR_ID}'",
            f"and status = 'pending'",
            f"and id between {self.start} and {self.end}"
        ]

        self.cursor.execute(" ".join(select_query))

        for data in self.cursor.fetchall():
            if not data[1].strip():
                continue
            # print(data)
            yield scrapy.Request(
                url=data[1],
                headers=headers,
                cookies=cookies,
                cb_kwargs={
                    "id": data[0],
                    "file_name": data[2],
                    "main": data[3],
                    "name": "" if not data[4] else data[4],
                    "type": "" if not data[5] else data[5],
                },
                dont_filter=True
            )

    def parse(self, response, **kwargs):

        id = kwargs['id']

        if 'play.google.com' in response.url:
            print("invalid document url")
            update = f'update {db.asset_table} set status="invalid" where Id={id}'
            self.cursor.execute(update)
            self.con.commit()
            self.logger.info(f'{db.asset_table} Inserted...')
            self.con.commit()
            return None

        if self.VENDOR_ID == "ACT-B1-008" and ('.php' in response.url or '.asp' in response.url):
            if 'Content-Disposition' not in response.headers:
                if 'already_processed' not in kwargs:
                    kwargs['already_processed'] = True
                    yield scrapy.FormRequest.from_response(response, cb_kwargs=kwargs)
                    return None

        file_name = kwargs['file_name']
        if response.url.endswith(".exe"):
            file_name = response.url.split("/")[-1]
        if not file_name or file_name.endswith(".php") or file_name.endswith(".asp"):
            file_name = response.headers['content-disposition'].decode("utf-8").split("=")[-1].strip('"')

        file_type = kwargs['type']
        if not file_type:
            file_type = None
            if kwargs['main']:
                file_type = "image/product"
            elif ".zip" in file_name:
                file_type = "other"
            elif file_name.split(".")[-1].lower() in ['dxf', 'dwg', 'slddrw']:
                file_type = "cad/2D"
            elif file_name.split(".")[-1].lower() in ['step', 'iges', 'igs', 'sldprt', 'ipt', 'x_t', 'eprt', '.step']:
                file_type = "cad/3D"
            elif file_name.split(".")[-1].lower() in ['cert', 'crt']:
                file_type = "document/cert"

            if 'software' in kwargs['name'].lower():
                file_type = "other"

            if not file_type:
                if 'manual' in kwargs['name'].lower():
                    file_type = "document/manual"
                elif 'spec' in kwargs['name'].lower():
                    file_type = "document/spec"
                elif 'catalog' in kwargs['name'].lower():
                    file_type = "document/catalog"

            if not file_type and '.pdf' in file_name.lower():
                file_type = "document"

            if not file_type and file_name.split(".")[-1].lower() in ['png', 'jpg']:
                file_type = "image/product"

            if not file_type:
                file_type = "other"

        sha256 = hashlib.sha256(response.body).hexdigest()


        if 'Content-Length' in response.headers:
            length = response.headers['Content-Length'].decode("utf-8")
        else:
            length = response.body.__sizeof__()

        content_type = response.headers['Content-Type'].decode("utf-8")
        if ";" in content_type:
            content_type = content_type.split(";")[0].strip()

        item = dict()
        item['download_path'] = self.assets_save + str(sha256)
        item['media_type'] = content_type
        item['length'] = length
        item['type'] = file_type
        item['sha256'] = sha256
        item['file_name'] = file_name
        item['status'] = "Done"

        open(item['download_path'], "wb").write(response.body)

        try:
            field_list = []
            for field in item.items():
                field_list.append(f'{field[0]}="{field[1]}"')

            update = f'update {db.asset_table} set {", ".join(field_list)} where Id={id}'
            self.cursor.execute(update)

            self.con.commit()
            self.logger.info(f'{db.asset_table} Inserted...')
            self.con.commit()

        except Exception as e:
            self.logger.error(e)


if __name__ == '__main__':
    execute("scrapy crawl download_assest -a  start=1 -a end=370000000".split())
