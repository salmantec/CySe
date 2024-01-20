import requests
import sys

"""
OUTPUT of loop() function will be like below:

{"endpoints": ["v1"]"}
200
api
"""

def loop():
    for word in sys.stdin:
        # Here URL refers the actual ip / dns (like example.com)
        res = requests.get(f"URL/{word}")
        if res.status_code == 404:
            loop()
        else:
            data = res.json()
            print(data)
            print(res.status_code)
            print(word)


loop()


