#!/usr/bin/python3
"""
This script
- takes in a URL and an email address,
- sends a POST request to the URL with an email as parameter, and
- displays the body of the response.
"""
import sys
import requests


def post_email(url, email):
    """Posts an email to a URL and displays the body of the response."""
    response = requests.post(url, data={'email': email})
    print(response.text)


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
