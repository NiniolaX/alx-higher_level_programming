#!/usr/bin/python3
"""
This script:
    - takes in a URL,
    - sends a request to the URL,
    - displays the body of the response (decoded in utf-8),
    - managing HTTP error and exceptions appropriately.
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            page = response.read()
            print(page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
