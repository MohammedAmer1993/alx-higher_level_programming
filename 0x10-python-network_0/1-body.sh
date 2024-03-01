#!/bin/bash
#this script shows body only if return was 200 ok
curl -sI "$1" | grep "200 OK" && curl "$1" 