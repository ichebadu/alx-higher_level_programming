#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first arg
# displays the body of the response using curl

You have to use curl
curl -sX DELETE "$1"
