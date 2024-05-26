#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    """ GET /api/v1/cities/<city_id>
    """
    city_id = "nop"
    r = requests.get("http://0.0.0.0:5050/api/v1/cities/{}".format(city_id))
    print(r.status_code)
