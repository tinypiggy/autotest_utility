#!/usr/bin/env python3
# -*- coding:utf-8 -*-


data_map = {}
loaded = False


def load():
    with open('../resources/ejiayou.properties') as f:
        while True:
            line = f.readline()
            if line.strip():
                if line[0] != '#':
                    key, value = line.split('=')
                    data_map[key.strip()] = value.strip()
                    # print(key)
            elif line.endswith('\r') or line.endswith('\n') or line.endswith('\r\n'):
                continue
            else:
                break
    loaded = True


if __name__ == '__main__':
    load()