#!/usr/bin/python3
""" module to sent an email in a url throug post method"""
import urllib.request as req
import urllib.parse as par
import sys


if __name__ == "__main__":
    values = {"email": sys.argv[2]}
    url_parsed = par.urlencode(values).encode("utf-8")
    with req.urlopen(sys.argv[1], data=url_parsed) as mysite:
        d = mysite.read()
        print(d.decode('utf-8'))
