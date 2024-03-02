#!/usr/bin/python3
""" take url, send req, show return """
import requests
import sys

if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
        req.raise_for_status()
        print(req.text)
    except requests.exceptions.RequestException as e:
        print(f"Error code: {e.response.status_code}")
