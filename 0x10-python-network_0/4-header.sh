#!/bin/bash
# sends a get result to add headers
curl -s -X GET -H "X-School-User-Id:98" "$1"
