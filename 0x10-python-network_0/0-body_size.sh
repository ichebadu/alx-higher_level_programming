#!/bin/bash
# Bash script that takes in a URL, sends a request and display size
# The size must be displayed in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
