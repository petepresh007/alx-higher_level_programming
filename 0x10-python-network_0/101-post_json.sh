#!/bin/bas
# sending a json post request
curl -s -X POST -H "Content-Type: application/json" -d "$2" "$1"
