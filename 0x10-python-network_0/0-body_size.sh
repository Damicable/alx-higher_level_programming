#!/bin/bash
#Script that sends a request to a URL and display the body of response
curl -s "$1" | wc -c
