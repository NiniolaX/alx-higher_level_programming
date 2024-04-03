#!/bin/bash
# Takes in URL, sends GET request to it and displays response body
curl -s -H "X-School-User-Id: 89" "$1"
