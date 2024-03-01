#!/usr/bin/python3
"""
performing a get request using request
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url)
    if res.status_code == 200:
        resp = "Body response:\n\t- type: {}\n\t- content: {}"
        print(resp.format(
            type(res.text),
            res.text
        ))
