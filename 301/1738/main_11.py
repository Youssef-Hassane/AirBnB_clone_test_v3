#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    city_id = "nop"

    """ Get user
    """
    r = requests.get("http://0.0.0.0:5050/api/v1/users")
    r_j = r.json()
    user_id = r_j[0].get('id')

    
    """ POST /api/v1/cities/<city_id>/places
    """
    r = requests.post("http://0.0.0.0:5050/api/v1/cities/{}/places/".format(city_id), data=json.dumps({ 'user_id': user_id, 'name': "NewPlace", 'number_rooms': 4, 'number_bathrooms': 3, 'max_guest': 6, 'price_by_night': 100, 'latitude': 1.3, 'longitude': 2.3 }), headers={ 'Content-Type': "application/json" })
    print(r.status_code)