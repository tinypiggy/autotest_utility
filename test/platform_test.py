import requests
import time
import json
from codec import param_sign
from utility.dataloader import load, loaded, data_map


def call_platform(platform_name, url, param_map):
    timestamp = int(time.time())
    if not loaded:
        load()
    before_key = data_map['before_key']
    after_key = data_map['after_key']
    sign = param_sign.param_sign(param_map, before_key, after_key, timestamp)
    create_order_url = data_map['test_domain']
    if url.startswith('/'):
        create_order_url += url
    else:
        create_order_url += '/' + url
    create_order_url += '/%s/%s/%d' % (platform_name, sign, timestamp)
    print(create_order_url)
    print(json.dumps(param_map))
    headers = {'content-type': 'application/json'}
    res = requests.post(create_order_url, data=json.dumps(param_map), headers=headers)
    return res.content.decode('utf-8')

# 1. 黑名单  2. 优惠次数限制  3. 打印机状态
# 折扣油站和普通油站


if __name__ == '__main__':
    # oreo/ejiayou_open_api/orders/v1
    # param_map = {}
    # param_map['stationId'] = '12'
    # param_map['oilgunCode'] = '1'
    # param_map['totalAmount'] = '7.05'
    # param_map['phoneNumber'] = '17500001001'
    # param_map['hadInvoice'] = 'true'
    # param_map['invoiceHead'] = 'test'
    # param_map['invoiceNumber'] = 'sign123456'
    # # param_map['plateNumber'] = '粤A12345'
    # print(call_platform('dcd', 'oreo/ejiayou_open_api/orders/v1', param_map))

    # /oreo/ejiayou_open_api/orders/v1/payments
    param_map = {}
    param_map['outOrderSign'] = '20190515'
    param_map['payAmount'] = '4.15'
    orderSign = '1000000054976941'
    url = '/oreo/ejiayou_open_api/orders/v1/payments/' + orderSign
    print(call_platform('dcd', url, param_map))
