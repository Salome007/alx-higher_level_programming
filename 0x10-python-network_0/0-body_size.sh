#!/bin/bash
# Sends a request to url nd display the size of the body of the response
curl -s "${1}" | wc -c
