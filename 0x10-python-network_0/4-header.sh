#!/bin/bash
# takes URL GET request & displays response
curl -sH 'X-School-User-Id: 98' -X GET "$1"
