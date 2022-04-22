#!/bin/bash
# Takes URL & displays all HTTP methods
curl -sI "$1" | grep -i Allow | sed 's/.*: //p'
