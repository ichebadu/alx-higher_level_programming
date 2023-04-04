#!/usr/bin/python3
"""
This script accepts a URL as input, sends a request to the URL, 
and then displays the body of the response, decoded in UTF-8.
"""

import sys
from urllib import request, error

def fetch_web_page(url):
try:
with request.urlopen(url) as res:
return res.read().decode('UTF-8')
except error.HTTPError as er:
return 'Error code: {}'.format(er.code)

if name == "main":
url = sys.argv[1]
web_page = fetch_web_page(url)
print(web_page)
