#!/bin/bash
# sends URL request & displays status code response
curl -so "$1" /dev/null -w "%{http_code}"
