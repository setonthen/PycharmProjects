myList=[]

print ("Printing list content:")
for p in myList:
    print (p)

print ("Adding elements to the list")

myList.append("element 1")
myList.append("element 2")

print ("Printing list content:")
for p in myList:
    print (p)

someString=myList.pop(0)
print ("Printing element content")
print (someString)

print ("Printing list content:")
for p in myList:
    print (p)