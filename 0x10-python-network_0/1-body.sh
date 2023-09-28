#!/bin/bash
#Script that takes in a URL, sends a GET request and display body of response if status code is 200 using 'curl'
curl -sL "$1"
