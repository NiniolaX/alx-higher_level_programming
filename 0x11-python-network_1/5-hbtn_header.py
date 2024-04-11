#!/usr/bin/python3
"""
This script,
- takes in a URL,
- sends a request to the URL, and
- displays the value of the variable 'X-Request-Id' in the response id.
"""


import requests
import sys

def get_x_request_id(url):
    """
    Sends a request to a given URL and displays the value of its X-Request_Id.
    """
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))

if __name__ == '__main__':
    url = sys.argv[1]
    get_x_request_id(url)
