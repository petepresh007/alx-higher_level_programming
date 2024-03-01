#!/usr/bin/python3
"""
a module to print the content of headers
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    if 'X-Request-Id' in res.headers:
        print(res.headers['X-Request-Id'])
