#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    review_id = "nop"

    """ PUT /api/v1/reviews/<review_id>
    """
    r = requests.put("http://0.0.0.0:5050/api/v1/reviews/{}".format(review_id), data=json.dumps({ 'text': "NewTextReview" }), headers={ 'Content-Type': "application/json" })
    print(r.status_code)
