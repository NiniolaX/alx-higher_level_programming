#!/bin/bash
# Script takes a URL, sends a GET request and displays the body of response
curl -X GET -L "$1"