#JSON encoding
#Converts an object, usually a dictionary and outputs a JSON document as a string
#The entity that wants to transmit some data needs to encode it first as a JSON document

import json


wsID=5
alarmMsg="Workstation in error"

alarm={"wsID":wsID, "alarmMessage":alarmMsg, "time":"13:45:12"}

print ("Type of variable:")
print (str(type(alarm)))

print ("Dictionary item:")
print (alarm["alarmMessage"])

#JSON dumps takes an object, in this case a dictionary a creates a JSON document as a string
jsonsString= json.dumps(alarm)
print ("Json string")
print (jsonsString)

#Notice that we can send a JSON document easily through web services
print (str(type(jsonsString)))