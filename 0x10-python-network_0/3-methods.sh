#!/bin/bash
# a script to print all HTTP method
curl -s -X OPTIONS -I "$1" | grep -i allow
