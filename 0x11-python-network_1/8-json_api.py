#!/usr/bin/python3
"""Script that takes in a letter, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = {'q': sys.argv[1]}
    else:
        letter = {'q': ''}
    r = requests.post('http://0.0.0.0:5000/search_user', data=letter)
    try:
        content = r.json()
        if not content:
            print("No result")
        else:
            print("[{}] {}".format(content['id'], content['name']))
    except ValueError:
        print("Not a valid JSON")
