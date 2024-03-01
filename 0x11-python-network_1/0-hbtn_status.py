#!/usr/bin/python3
"""
A pythion script to fetch data from the url below
https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status'
            ) as response:
        data_fetched = response.read()
        res = ("Body response:\n\t- type: {}\n\t- content: {}"
               "\n\t- utf8 content: {}")
        print(res.format(
            type(data_fetched),
            data_fetched,
            data_fetched.decode('utf-8')
        ))
