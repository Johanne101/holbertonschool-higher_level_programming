#!/bin/bash
# sends URL request & displays status code response
curl -s -o "$1" /dev/null -w "%{http_code}"
