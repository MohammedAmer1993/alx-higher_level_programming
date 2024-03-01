#!/bin/bash
# bash file to git the content legnth of a file

curl -si "$1" | grep Content-Length | sed 's/Content-Length: //g'