#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    """ Fetch reviews
    """
    r = requests.get("http://0.0.0.0:5050/api/v1/places/{}/reviews".format("nop"))
    print(r.status_code)
