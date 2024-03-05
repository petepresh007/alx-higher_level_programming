#!/bin/bash
# a script to print all HTTP method
curl -s -X OPTIONS -I "$1" | awk '/^Allow:/{gsub("Allow: ", ""); print}'
