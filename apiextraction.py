'''Data Retrival form duckduckgo API
using basic json and request packages
'''


import requests
import json

#try to take single word input from user
query = raw_input("Enter The Word to search")

#Mapping the input string with the API
duckduckgoapi = "http://duckduckgo.com/?q="
duckduckgoapi = duckduckgoapi + query
duckduckgoapi = duckduckgoapi + "&t=he&ia=web&format=json"

#Printing The API String to show user how the data would Look like
print duckduckgoapi

#Making String Connect to Webserver
req = requests.get(duckduckgoapi)

if (req.status_code == 200):
    print ("Connection Established SuccessFully");
    req.text
    data = json.loads(req.text)
    
    #Printing the data That were required in a specific format as Link and One line Description
    for a in data["Results"]:
        dict=a
        print dict["Text"]
        print dict["FirstURL"]

    for a in data["RelatedTopics"]:
        dict=a
        print dict["Text"]
        print dict["FirstURL"]



