#!/usr/bin/python3
""" module to fetch a url """
import urllib.request as req

if __name__ == "__main__":
    with req.urlopen("https://alx-intranet.hbtn.io/status") as mysite:
        data = mysite.read()
        print("Body response:")
        print(f"\t- type: {type(data)}")
        print(f"\t- content: {data}")
        s = data.decode('utf-8')
        print(f"\t- utf8 content: {s}")
