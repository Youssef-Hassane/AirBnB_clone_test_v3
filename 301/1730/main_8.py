#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    """ POST /api/v1/states
    """
    r = requests.post("http://0.0.0.0:5050/api/v1/states/", data=json.dumps({ 'fake_name': "NewState" }), headers={ 'Content-Type': "application/json" })
    print(r.status_code)
