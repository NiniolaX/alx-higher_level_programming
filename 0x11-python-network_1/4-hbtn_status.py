#!/usr/bin/python3
"""
This script fetches a URL using Python requests package.
"""


import requests
def fetchUrl(url):
    """ Fetches a given URL """
    r = requests.get(url)
    print(f"Body response:\n\t- type: {type(r.text)}\n\t- content: {r.text}")

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    fetchUrl(url)
