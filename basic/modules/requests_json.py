import json
import requests
import sys

limit = 10

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=" + str(limit) + "&term=" + sys.argv[1])
print(json.dumps(response.json(), indent = 2)) #json.dumps is just for pretty print

obj_res = response.json() #from server to json object
for result in obj_res["results"]: #there is a key called results
    print(result["trackName"])