#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    state_id = "nop"
    
    """ POST /api/v1/states/<state_id>/cities
    """
    r = requests.post("http://0.0.0.0:5050/api/v1/states/{}/cities/".format(state_id), data=json.dumps({ 'name': "NewCity" }), headers={ 'Content-Type': "application/json" })
    print(r.status_code)
    