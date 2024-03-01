#!/usr/bin/python3
"""
a script to post email to an endpoint
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = {"email": email}
    res = requests.post(url, data=value)
    if res.status_code == 201:
        print(res.text)
