#!/usr/bin/env python
# -*- coding: utf-8 -*-
def say_hello():
    import requests
    print(requests.get("http://www.baidu.com").status)
    print('hello','123')

if __name__ == '__main__':
    say_hello()