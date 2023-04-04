#!/bin/bash
# Bash script that takes in a URL, sends a request and display size
# The size must be displayed in bytes
# You have to use curl
curl -s "$1" | wc -c
