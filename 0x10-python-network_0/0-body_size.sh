#!/bin/bash
# Takes request size of the URL body & displays response
curl -s "$1" | wc -c
