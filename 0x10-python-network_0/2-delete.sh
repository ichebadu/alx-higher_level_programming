#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first arg
curl -sX DELETE "$1"
