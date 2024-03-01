#!/bin/bash
# bash file to git the content legnth of a file
curl -sI "$1" | grep Content-Length | sed 's/Content-Length: //g'
