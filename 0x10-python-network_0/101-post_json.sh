#!/bin/bash
#Script that sends a JSON POST request to a URL as first argument
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
