#!/usr/bin/bash
# the size of the webpage
curl -w '%{size_download}\n' -o /dev/null -s http://example.com

