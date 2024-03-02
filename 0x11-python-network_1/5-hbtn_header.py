#!/usr/bin/python3
""" module to send req, get X req id and print """
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    cont = response.headers.get("X-Request-Id")
    print(cont)
