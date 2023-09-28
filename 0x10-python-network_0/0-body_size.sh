#!/bin/bash
# sends a request to url, and displays e size of the body of the responsecurl -s "${1}" | wc -c
