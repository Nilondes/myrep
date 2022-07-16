import requests

import json

import sys

for line in sys.stdin:
    line = line.rstrip()

    url = 'http://numbersapi.com/' + line + '/math?json=true'

    res = requests.get(url)
    answer = json.loads(res.text)

    if answer["found"]:
        print("Interesting")
    else:
        print("Boring")



