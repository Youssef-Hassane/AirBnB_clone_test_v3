#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    """ Get 1 state_id and 1 city
    """
    r = requests.get("http://0.0.0.0:5050/api/v1/states")
    r_j = r.json()
    
    state_ids = []
    city_ids = []
    for state_j in r_j:
        rs = requests.get("http://0.0.0.0:5050/api/v1/states/{}/cities".format(state_j.get('id')))
        rs_j = rs.json()
        if len(rs_j) == 1: # Only Arizona
            state_ids.append(state_j.get('id'))
        else:
            for city_j in rs_j:
                rc = requests.get("http://0.0.0.0:5050/api/v1/cities/{}/places".format(city_j.get('id')))
                rc_j = rc.json()
                if len(rc_j) == 2: # Only City B
                    city_ids.append(city_j.get('id'))
            
    # Arizona OR City B

    """ POST /api/v1/places_search
    """
    r = requests.post("http://0.0.0.0:5050/api/v1/places_search", data=json.dumps({ 'states': state_ids, 'cities': city_ids }), headers={ 'Content-Type': "application/json" })
    r_j = r.json()
    print(len(r_j))
