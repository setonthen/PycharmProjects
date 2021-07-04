#JSON decoding
#This code exemplifies how to parse and process a JSON document
#Parsing is usually done at the Server (Back end side)

import json

#Communication phase
jsonAsString='{"wsID": "55", "location":"A51","pallets":[{"pID":55,"part":"cylinder"},{"pID":33,"part":"spring"}]}'

#Converting to a python object, dictionary
#parsing
myRecMsg=json.loads(jsonAsString)

#Access to one attribute of the dictionary
print ("Workstation ID: " + myRecMsg["wsID"])


myPallets=myRecMsg["pallets"]
# Each value in x will hava data with the next format: {"pID":55,"part":"spring"}
for x in myPallets:
    print (str(x["pID"]) + " has part: "+ x["part"])



print ("Type of variable: " + str(type(myPallets)))

print ("Type of variable: " + str(type(myRecMsg)))