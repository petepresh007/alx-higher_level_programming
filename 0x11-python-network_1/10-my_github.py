#!/usr/bin/python3
"""
module to display github's user id
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    res = requests.get(
            "https://api.github.com/user", auth=(username, password)
            )
    if res.status_code == 200:
        data = res.json()
        print(data["id"])
    else:
        print("None")
