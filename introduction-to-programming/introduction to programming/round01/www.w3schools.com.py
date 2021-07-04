# Unpack a Collection/List: If you have a collection of values in a list, tuple etc.
# Python allows you extract the values into variables. This is called unpacking.

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# for loop

# for i in range (5): # i is the variable and 5 is the number of time to loop
#   print(i)

# for i in range (2):
#   print('a')
#   print('b')
# for i in range (2):
#   print('c')
#   for i in range (3):
#     print('d')
# print('End of loop')



#Global and Local Variable : Variables that are created outside of a function (as in all of the examples above)
# are known as global variables. If you create a variable with the same name inside a function, this variable will be local,
# and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.
# x = "awesome"
#
# def myfunc():
#   x = 'fantastic'
#   print("Python is " + x)
#
# myfunc()
#
# print('python is ' + x)


# # Variables to hold the prices of each item, the subtotal,
# # and the total.
# item1 = 0.0
# item2 = 0.0
# item3 = 0.0
# item4 = 0.0
# item5 = 0.0
# subtotal = 0.0
# tax = 0.0
# total = 0.0
#
# # Constant for the sales tax rate.
# TAX_RATE = 0.07
#
# # Get the price of each item.
# item1 = float(input("Enter the price of item #1: "))
# item2 = float(input("Enter the price of item #2: "))
# item3 = float(input("Enter the price of item #3: "))
# item4 = float(input("Enter the price of item #4: "))
# item5 = float(input("Enter the price of item #5: "))
#
# # Calculate the subtotal.
# subtotal = item1 + item2 + item3 + item4 + item5
#
# # Calculate the sales tax.
# tax = subtotal * TAX_RATE
#
# # Calculate the total.
# total = subtotal + tax
#
# # Print the values.
# print("Subtotal: ", format(subtotal, '.2f'))
# print("Sales Tax: ", format(tax, '.2f'))
# print("Total: ", format(total, '.2f'))


# # Variables to hold the distances.
# distance6Hours = 0.0
# distance10Hours = 0.0
# distance15Hours = 0.0
#
# # Constant for the speed.
# SPEED = 70

# # Calculate the distance the car will travel in
# # 6, 10, and 15 hours.
# distance6Hours = SPEED * 6
# distance10Hours = SPEED * 10
# distance15Hours = SPEED * 15
#
# # Print the results.
# print("The car will travel the following distances:")
# print(distance6Hours, "miles in 6 hours.",format(distance6Hours,'.2f'))
# print(distance10Hours, "miles in 10 hours.")
# print(distance15Hours, "miles in 15 hours.")


# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

### Create a variable outside of a function, and use it inside the function

# x = "awesome"
# def myfunc():
#   print("Python is " + x)
#
# myfunc()

#####Example
# x = "awesome"
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
# myfunc()
# print("Python is " + x)


###EXample of global variable
# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

# def myfunc():
#   global x
#   x = "fantastic"
#
# myfunc()
#
# print("Python is " + x)

txt = " Hello World "
x = txt.strip()
