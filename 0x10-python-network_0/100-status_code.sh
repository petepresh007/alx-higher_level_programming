#!/bin/bash
# print status codes
curl -s -o /dev/null -w "%{http_code}" "$1"
