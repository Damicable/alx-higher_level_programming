#!/bin/bash
# Script that displays all HTTP methods the server will accept in URL
curl -sI "$1" | grep "Allow" | cud -d " " -f 2-
