import requests
import json



#GET request
r = requests.get("http://iiapi-env2.eba-7fc5ti29.us-west-2.elasticbeanstalk.com/workstations/3")
print (r.content)

#Converts JSON document to a Python object, dictionary
myRecMsg=json.loads(r.content)
#print (type(myRecMsg))
#print  (myRecMsg["status"])
print(myRecMsg.get('status'))
print(('the id of my system is ')+ str(myRecMsg.get('id')))