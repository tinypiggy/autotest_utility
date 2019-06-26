import hashlib


# P端接口签名生成方法
def param_sign(param_map, before_key, after_key, timestamp):
    # tail = '&timestamp={}&beforekey={}&afterkey={}'.format(timestamp, before_key, after_key)
    tail = 'timestamp=%d&beforeKey=%s&afterKey=%s' % (timestamp, before_key, after_key)
    key_set = sorted(param_map.keys())
    sign = ''
    seq = ''
    for key in key_set:
        if param_map[key]:
            sign += seq + key + '=' + param_map[key]
            seq = '&'
    sign += '&' + tail
    print(sign)
    m = hashlib.new('md5')
    m.update(sign.encode(encoding='utf-8'))
    sign = m.hexdigest().upper()
    return sign


if __name__ == '__main__':
    ss = '刘科哈哈'
    for s in ss:
        print(s)
    # ss = ss.encode('unicode')
    for s in ss:
        print(s)


