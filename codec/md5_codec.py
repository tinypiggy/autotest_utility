import hashlib

# 斑马加密
param = {
    "ak": "1235",
    "finalFee": "",
    "isPay": "true",
    "openId": "0352599927039743",
    "orderId": "590141509324795904",
    "paySno": "6681a745da62486f9edb9d7eb0f0afd8",
    "t": "1560238513",
    "totalFee": "86.59",
    "tradeNo": "20190611113834894008202649611",
    # "sign": '919500919993E5F5ACBBC3B33C895B1E'
}


def zebra_encode(param_map, after_key='19961A8B6534B94871421B16600FE15F'):
    key_set = sorted(param_map.keys())
    sign = ''
    seq = ''
    for key in key_set:
        if param_map[key]:
            sign += seq + key + '=' + param_map[key]
            seq = '&'
    sign += after_key
    # sign = sign.upper()
    print(sign)
    m = hashlib.new('md5')
    m.update(sign.encode(encoding='utf-8'))
    sign = m.hexdigest().upper()
    return sign


if __name__ == '__main__':
    sign = zebra_encode(param)
    print(sign)
