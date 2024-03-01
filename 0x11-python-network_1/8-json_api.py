#!/usr/bin/python3
"""
a module with a function that searches
for name
"""
import sys
import requests


def search(searchparams):
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": searchparams}

    res = requests.get(url, data=data)
    try:
        res_data = res.json()
        if res_data:
            print(f"[{res_data['id']}] {res_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        search(sys.argv[1])
    else:
        search("")
