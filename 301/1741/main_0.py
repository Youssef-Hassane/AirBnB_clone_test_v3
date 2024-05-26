#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    """ verify http response header Access-Control-Allow-Origin
    """
    r = requests.get("http://0.0.0.0:5050/api/v1/states")
    print(r.headers.get("Access-Control-Allow-Origin") is None)
