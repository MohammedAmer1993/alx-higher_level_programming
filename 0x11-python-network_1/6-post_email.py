#!/usr/bin/python3
""" take url, send post with an email, show body with the email"""
import requests
import sys

if __name__ == "__main__":
    val = {"email": sys.argv[2]}
    res = requests.post(sys.argv[1], data=val)
    print(res.text)
