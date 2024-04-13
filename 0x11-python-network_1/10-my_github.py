#!/usr/bin/python3
"""
This script:
    - takes in a Github credential (username and password), and
    - uses Github API to display the associated id
"""
import sys
import requests


def display_github_userid(user, passwd):
    """ Displays the id of a GitHub user using GitHub API"""
    url = 'https://api.github.com/user'
    headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
    response = requests.get(url, headers=headers, auth=(user, passwd))
    user_data = response.json()
    print(user_data.get('id'))


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    display_github_userid(username, password)
