#!/usr/bin/python3
""" module to send the req and show the return code"""
import urllib.error as er
import urllib.request as req
import sys

if __name__ == "__main__":
    try:
        with req.urlopen(sys.argv[1]) as mysite:
            data = mysite.read()
            print(data.decode("utf-8"))
    except er.URLError as e:
        print(f"Error code: {e.code}")
    except er.HTTPError as e:
        print(f"Error code: {e.code}")
