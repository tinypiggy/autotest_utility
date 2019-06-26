from codec.aes_codec import *
from concurrent.futures import ThreadPoolExecutor
import time
import json
import requests


def task(param):
    start = time.time()
    res = requests.post(param['url'], data=param['body'], headers=param['header'])
    last = time.time() - start
    m = json.loads(decrypt_cbc(res.content))
    if m['code'] == 500:
        print(param['url'])
    return {"last": last, "content": decrypt_cbc(res.content)}


if __name__ == '__main__':
    input_param = {
        "userCouponId": "",
        "productType": "1",
        "orderSum": "200",
        "filterSource": "20",
        "originalCost": "200",
        "payType": "1",
        "createOrderCarType": "1",
        "invoiceNumber": "22123333444",
        "stationId": "12",
        "oilId": "2",
        "invoiceHead": "深圳市警视通实业有限公司",
        "orderType": "1",
        "oilgunId": "2039",
        "hadInvoice": "true",
        "freeOrderActivity": "1"
    }
    headers = {'Content-Type': 'application/text'}
    params = []
    with open('../resources/params.txt') as f:
        for line in f.readlines():
            session_key = line.strip()
            data_body = encrypt_cbc(json.dumps(input_param)).decode()
            v2_url = "http://dev.ejiayou.com/oreo/rs/order/create/v2/" + session_key + "/121212121"
            param = {
                'body': data_body,
                'header': headers,
                'url': v2_url
            }
            params.append(param)

    executors = ThreadPoolExecutor(max_workers=1)
    max_last = 0
    min_last = 100
    sum_last = 0
    count = 0
    fail = 0
    for data in executors.map(task, params):
        print(data['content'])
        if json.loads(data['content'])['code'] != '200':
            fail += 1
        count += 1
        if data['last'] < min_last:
            min_last = data['last']
        if data['last'] > max_last:
            max_last = data['last']
        sum_last += data['last']

    print("最短响应时间: {}".format(min_last))
    print("最大响应时间: {}".format(max_last))
    print("平均响应时间: {}".format(sum_last/count))
    print("成功率: {}%".format(int(fail * 100/count)))

    # print(json.dumps(input_param))
    # print(encrypt_cbc(json.dumps(input_param)))
    # print(encrypt_cbc('abcd').decode())
    # v1_url = "http://dev.ejiayou.com/oreo/rs/order/create/v2/db3acba13d5a45d09cfc1f3ea4c73288/12312321"
    # res = requests.post(v1_url, data=encrypt_cbc(json.dumps(input_param)).decode(), headers=headers)
    # print(decrypt_cbc(res.content))
