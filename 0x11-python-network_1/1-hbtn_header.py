#!/usr/bin/python3
""" sends a request to the given URL and displays the value of the
X-Request-Id variable found in the response header
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        headers = dict(res.headers)
        x_request_id = headers.get("X-Request-Id")
        print(x_request_id)
