#!/bin/bash
# Takes in a URL, sends a request to it and displays size of response body
url=$1
curl -s -o /dev/null -w '%{size_download}\n' "$url"
