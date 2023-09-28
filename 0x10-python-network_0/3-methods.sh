#!/bin/bash
# Script that displays all HTTP methods the server will accept in URL
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
