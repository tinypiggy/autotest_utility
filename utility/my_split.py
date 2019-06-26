import base64
import socket
import errno


def my_split(s, seq):
    length = len(s)
    i = 0
    n = ''
    result = []
    while i < length:
        if s[i] == seq[0]:
            if len(seq) > length - i:
                n += s[i:]
                i = length
            else:
                if s[i: i+len(seq)] == seq:
                    i += len(seq)
                    result.append(n)
                    n = ''
                else:
                    i += 1
                    n += s[i]
        else:
            n += s[i]
            i += 1
    if n != '':
        result.append(n)
    return result


def tes(*args, **kwargs):
    print('{} -- {}'.format(args, kwargs))


if __name__ == '__main__':
    print('start')
    s = 'aaa&&&ccc&&&'
    print(my_split(s, '&&&'))
    print(base64.b64encode(b'ab\x00cd'))
    for i in range(65536):
        try:
            sock = socket.create_connection(('127.0.0.1', '10001'))
            print("connected from {} to {}".format(sock.getsockname(), sock.getpeername()))
            # time.sleep(1)
        except socket.error as e:
            print('range no: {}'.format(i))
            if e.errno != errno.ECONNREFUSED:
                print("erron: {}, ECONNREFUSED: {} ".format(e.errno, errno.ECONNREFUSED))
                break

