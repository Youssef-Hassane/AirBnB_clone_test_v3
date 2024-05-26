#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    """ POST /api/v1/places_search
    """
    r = requests.post("http://0.0.0.0:5050/api/v1/places_search", data={}, headers={ 'Content-Type': "application/x-www-form-urlencoded" })
    print(r.status_code)