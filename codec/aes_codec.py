from Crypto.Cipher import AES
import hashlib
import base64
from utility import dataloader

assign = AES.block_size


def pad(s):
    return s + (assign - len(s) % assign) * chr(assign - len(s) % assign)


def unpad(s):
    return s[0:-ord(s[-1])]


def get_sha1prng_key(key):
    '''[summary]
    encrypt key with SHA1PRNG
    same as java AES crypto key generator SHA1PRNG
    Arguments:
        key {[string]} -- [key]

    Returns:
        [string] -- [hexstring]
    '''
    signature = hashlib.sha1(key.encode()).digest()
    signature = hashlib.sha1(signature).hexdigest()
    # res = ''.join(['%02x' % i for i in signature]).upper()[:32] # 28B2AEFDF7B48911FBC7AE225771C495
    return signature[:32]


# 手机号加解密
def encrypt(msg, aes_key=None):
    if not dataloader.loaded and not aes_key:
        dataloader.load()
        aes_key = dataloader.data_map['aes_key']
    aes_key = get_sha1prng_key(aes_key)
    aes = AES.new(bytes.fromhex(aes_key), AES.MODE_ECB)
    encrypt_aes = aes.encrypt(pad(msg))
    return ''.join(['%02x' % i for i in encrypt_aes]).upper()


def decrypt(msg, aes_key=None):
    if not dataloader.loaded and not aes_key:
        dataloader.load()
        aes_key = dataloader.data_map['aes_key']
    aes_key = get_sha1prng_key(aes_key)
    aes = AES.new(bytes.fromhex(aes_key), AES.MODE_ECB)
    decrypt_aes = aes.decrypt(bytes.fromhex(msg))
    return unpad(str(decrypt_aes, encoding='utf-8'))


# oreo 创建订单接口加解密
def encrypt_cbc(msg, key='24ReoosAdrdAplpe', iv='E-24-Reoo-Sritng'):
    aes = AES.new(key.encode(), AES.MODE_CBC, IV=iv.encode())
    msg = pad(msg)
    return base64.b64encode(aes.encrypt(msg))


def decrypt_cbc(msg, key=b'24ReoosAdrdAplpe', iv=b'E-24-Reoo-Sritng'):
    aes = AES.new(key, AES.MODE_CBC, IV=iv)
    return unpad(aes.decrypt(base64.b64decode(msg)).decode())


if __name__ == '__main__':
    enc = encrypt('13418400448')
    print(enc)
    phones = [
        '0A6E1318EBB2C39E202B55353D0487AD',
        # '4A63CDD067E055C45C492CDCEBBCA9F5',
        # 'f8721cdfddaf66719b8231eecc7d3ac1',
        '3231B7A0BC533B00618703E2BDEF5FB5',
        '0677c08ee0a02f7fce1c42dd67e219bf',
        # '5FE14DBD59EFEB10171A5ACDFA9CCB84',
        # '88ce4523fb35718593c10880cfc0c9ff',
        '0bf8dbd8a5a90360de5aa43d2eb3d7b7',
        '84421bcc1fe8c15656f372ea90cc935f',
        '440049f6412711cfbda72794495e39e9',
        'f423bc0c24a8c633156246f5a4610912',
        # '5148b95d83086f2d7c87accefe47a4de'
    ]
    for phone in phones:
        print(decrypt(phone))
