import datetime
import json
import os

import boto3
from boto3.dynamodb.conditions import Key
from dateutil.relativedelta import relativedelta


def get_database():
    endpoint = os.environ.get('DB_ENDPOINT')
    if endpoint:
        print("db endpoint enabled: ", endpoint)
        return boto3.resource('dynamodb', endpoint_url=endpoint)
    else:
        print("db endpoint disabled")
        return boto3.resource('dynamodb')


class DBAccessor:

    # NOTE ファクトリにできそう
    dynamodb = get_database()
    TABLE_NAME = os.environ.get('DB_TABLE_NAME')
    # FIXME table name:  pythagorasになる
    print("table name: ", TABLE_NAME)
    table = dynamodb.Table(TABLE_NAME)

    def __init__(self, pk):
        self.__pk = pk

    def get_items(self):

        try:
            response = DBAccessor.table.query(
                KeyConditionExpression=Key('pk').eq(self.__pk)
            )
        except Exception as e:
            print("e = ", e)
            return 500

        items = response['Items']  # [0]

        return items


def lambda_handler(event, __):
    print("event = ", event)
    status_code = 200
    message = 'Success'

    body = {
        'message': message,
    }

    # access_token = API_KEY
    # headers = {'Authorization': 'Bearer '+access_token}

    dt_now = datetime.datetime.now()
    # dt_prev_year = str((dt_now - relativedelta(months=1)).year)
    # dt_prev_month = str((dt_now - relativedelta(months=1)).month)
    # dt_next_year = str((dt_now + relativedelta(months=1)).year)
    # dt_next_month = str((dt_now + relativedelta(months=1)).month)

    target_year = str(dt_now.year)  # '2021'
    target_month = str(dt_now.month).zfill(2)  # '03'
    target_day = str(dt_now.day).zfill(2)  # '04'
    print(target_year, target_month, target_day)

    pk = target_year + '-' + target_month + '-' + target_day

    db_accessor = DBAccessor(pk)
    articles = db_accessor.get_items()
    print(articles)

    return {'statusCode': status_code,
            'body': json.dumps(body),
            'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}}


if __name__ == "__main__":
    lambda_handler(None, None)

# 実行方法
# chalice local
