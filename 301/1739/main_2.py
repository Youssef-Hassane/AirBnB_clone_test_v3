#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    """ GET /api/v1/places/<place_id>/amenities
    """
    r = requests.get("http://0.0.0.0:5050/api/v1/places/{}/amenities".format("doesn_t_exist"))
    print(r.status_code)
