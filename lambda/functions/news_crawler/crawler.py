# pipeline test
import datetime
import json
import time
import uuid

import requests

from .db_access import DBAccessor

# from dateutil.relativedelta import relativedelta


# DEBUG = False
# if DEBUG:  # FIXME APIKEYがDEBUGの時しか読み込まれない, 本場では不要なため外出しする
#     from dotenv import load_dotenv
#     load_dotenv(verbose=True)

MAX_PAGE_SIZE = 100
MONTH_NUM = 12
PAGE_NUM = 1
PER_PAGE = 100
STOCKS = 300  # 検索対象にするstock数
URL_NEWS = 'https://newsapi.org'


class Crawler:
    # # NOTE ファクトリにできそう
    # access_token = os.environ['API_KEY']
    # headers = {'Authorization': 'Bearer '+access_token}

    def __init__(self):
        self.__db_accessor = DBAccessor()
        self.__target_date = self.__create_target_date()

    def __create_items(self, item):
        sk = str(uuid.uuid4())
        title = item.get('title')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')
        ttl = int(time.time()) + 86400

        items = {
            "pk": self.__target_date,
            "sk": sk,
            "title": title,
            "article_url": url,  # queryにおいて、ProjectionExpressionでurl属性が予約語として使用できない
            "urlToImage": urlToImage,
            "publishedAt": publishedAt,
            "ttl": ttl,
        }
        return items

    def __save_news(self, items: list[dict[str, str]]):

        for item in items:

            try:
                news = self.__create_items(item)
                self.__db_accessor.put_item(news)
            except Exception as e:
                print(e)
                return 500

        return 200

    def __get_news(self):
        # url = URL_NEWS + '/v2/everything?q=Apple&from='+self.__target_date+'&sortBy=popularity&apiKey=60790e1b53b94781be72b717110b48c1'

        url = URL_NEWS + '/v2/top-headlines?country=jp&sortBy=popularity&apiKey=60790e1b53b94781be72b717110b48c1'

        response = requests.get(url)  # , headers=Crowler.headers)
        # print(response.text)
        return response

    def __create_target_date(self):
        dt_now = datetime.datetime.now()
        target_each_year = dt_now.strftime('%Y')  # '2022'
        target_each_month = dt_now.strftime('%m')  # '06'
        target_each_day = dt_now.strftime('%d')  # '07'
        target_date = target_each_year + '-' + target_each_month + '-' + target_each_day
        return target_date

    def run(self):
        response = self.__get_news()
        self.__save_news(json.loads(response.text).get("articles"))
        return 200
