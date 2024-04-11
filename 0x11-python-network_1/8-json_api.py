#!/usr/bin/python3
"""
This script:
    - takes in a letter and sends a POST request to a URL
    - displays the id and name if the response body is properly JSON formatted
"""
import sys
import requests


def post_json(q):
    """
    POSTs a letter to a URL and displays the associated name and id.
    """
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': q})
    try:
        data = response.json()
    except ValueError:
        print('Not a valid json')
    else:
        if not data:
            print('No result')
        else:
            print(f"[{data.get('id')}] {data.get('name')}")


if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    post_json(q)
