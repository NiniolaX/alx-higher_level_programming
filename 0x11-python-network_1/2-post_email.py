#!/usr/bin/python3
"""
This script:
    - takes in a URL and an email,
    - sends a POST request to the passed URL with the email as parameter, and
    - displays the body of the response decoded in utf-8.
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    # Extract url and email from script arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Build request object
    data = {'email': email}
    req = urllib.request.Request(url, data)

    # Send POST request to server
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page)
