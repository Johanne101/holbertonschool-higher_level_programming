#!/bin/bash
# Takes URL, sends POST request & displays response
curl -d "email=test@gmail.com&subject=I will always be here for PLD" -sX POST "$1"
