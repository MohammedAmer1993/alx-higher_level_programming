#!/bin/bash
# bash file to git the content legnth of a file

curl -si gazza.tech | grep Content-Length | sed 's/Content-Length: //g'