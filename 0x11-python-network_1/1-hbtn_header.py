#!/usr/bin/python3
""" fetch url and send request and get the value of var in header """
import urllib.request as req
import sys


if __name__ == "__main__":
    with req.urlopen(sys.argv[1]) as mysite:
        x = mysite.getheader("X-Request-Id")
        print(x)
