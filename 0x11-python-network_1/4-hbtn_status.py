#!/usr/bin/python3
""" module to fetch status """
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    data = response.text
    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
