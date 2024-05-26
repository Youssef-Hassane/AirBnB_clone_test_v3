#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    """ Get one user
    """
    r = requests.get("http://0.0.0.0:5050/api/v1/users")
    r_j = r.json()
    user_id = r_j[0].get('id')

    """ DELETE /api/v1/users/<user_id>
    """
    r = requests.delete("http://0.0.0.0:5050/api/v1/users/{}".format(user_id))
    print(r.status_code)
    
    """ Verify if the deleted user is not present anymore
    """
    r = requests.get("http://0.0.0.0:5050/api/v1/users")
    r_j = r.json()
    for user_j in r_j:
        if user_j.get('id') == user_id:
            print("user is not deleted")
        else:
            print("OK")
