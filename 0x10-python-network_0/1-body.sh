#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL
# Display only body of a 200 status code response. You have to use curl
curl -sL "$1"
