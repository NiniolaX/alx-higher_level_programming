#!/usr/bin/python3
"""
This script:
    - takes in a URL,
    - sends a request to the URL,
    - displays the body of the response, and
    - prints the HTTP status code, if >= 400.
"""
import sys
import requests


def get_url_with_status_code(url):
    """ Sends a request to a given URL and prints response body.
    Prints HTTP status code if error occurs.
    """
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == '__main__':
    url = sys.argv[1]
    get_url_with_status_code(url)
