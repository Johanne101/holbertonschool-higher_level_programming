#!/bin/bash
# sends URL request & displays status code response
curl -so /dev/null -w "%{http_code}" "$1"
