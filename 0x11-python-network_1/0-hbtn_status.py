#!/usr/bin/python3
""" module to fetch a url """
import urllib.request as req

if __name__ == "__main__":
    with req.urlopen("https://alx-intranet.hbtn.io/status") as mysite:
        data = mysite.read()
        print("body response:")
        print(f"    - type: {type(data)}")
        print(f"    - content: {data}")
        print(f"    - utf-8 content: {data.decode('utf-8')}")
