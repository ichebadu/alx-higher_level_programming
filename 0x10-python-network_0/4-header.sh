#!/bin/bash
# Bash script thatget get URL header variable X-School-User-Id must be sent with the value 98
curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
