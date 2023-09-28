#!/bin/bash
#Script that sends a request to a URL and displays only status code
curl -s -o /dev/null -w "%{http_code}" "$1"
