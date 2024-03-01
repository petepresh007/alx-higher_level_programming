#!/usr/bin/python3
"""
get the data stored in a header attr X-Request-Id
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_requested_id = response.headers.get('X-Request-Id')
        print(x_requested_id)
