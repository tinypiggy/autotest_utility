from codec import aes_codec


base_url = "https://dev.ejiayou.com/v1/phpUtils/encrypt.do?content="


def phone_decode(_input, _out):
    with open(_out, 'a+') as w:
        w.seek(0, 0)
        with open(_input) as r:
            for line in r.readlines():
                w.write(aes_codec.decrypt(line.strip()) + '\n')


if __name__ == '__main__':
    phone_decode('../resources/phone.txt', '../resources/res.txt')
