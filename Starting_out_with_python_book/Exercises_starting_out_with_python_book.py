# my_value = 99
# my_value = 0
# print(my_value)

# string_value = input('How many hours did you work? ')
# hours = int(string_value)


#5/2  = 2.5 #give the answer in decimal
#5//2 = 2  #give answer in unit that is the fraction past is not printed and When the result is	negative,
# it	is	rounded	away from zero to the nearest integer.
# 5 & 2 = 1 #gives the reminder



# price = float(input('original price of the item? '))
# percentage_price = price * (20/100) #20% prcie of original cost
# sale_price= price - percentage_price
# print('the sale prcie is', sale_price)


# # Get a number of seconds from the user.
# total_seconds = float(input('Enter a number of seconds: '))
# # Get the number of hours.
# hours = total_seconds // 3600
# # Get the number of remaining minutes.
# minutes = (total_seconds // 60) % 60
# # Get the number of remaining seconds.
# seconds = total_seconds % 60
# # Display the results.
# print('Here is the time in hours, minutes, and seconds:')
# print('Hours:', hours)
# print('Minutes:', minutes)
# print('Seconds:', seconds)



#Breaking Long statements into Multiple Lines
# Python allows you to break a statement into multiple lines by using the line continuation
# character, which is a backslash (\) You simply type the backslash character at the point
# you want to break the statement, and then press the Enter key. (\n) is the escape characters

# Escape Character    Effect
# \n                  Causes output to be advanced to the next line.
# \t                  Causes output to skip over to the next horizontal tab position.
# \'                  Causes a single quote mark to be printed.
# \"                  Causes a double quote mark to be printed.
# \\                  Causes a backslash character to be printed.


# print('We sold', units_sold, \
# 'for a total of', sales_amount)

# print('One', end=' ')
# print('Two', end=' ')
# print('Three')

# print('Mon\tTues\tWed')
# print('Thur\tFri\tSat')

# print(format(12345.6789, '.2f'))
# Here is the meaning of its contents:
# •	The	.2 specifies the precision. It indicates that we want to round the number to two decimal places.
# •	The	f specifies that the data type of the number we are formatting is a floating-point
# number. (If you are formatting an integer, you cannot use f for the type. We discuss integer formatting momentarily.)

# inserting Comma separators
# If you want the number to be formatted with comma separators, you can insert a comma into the format specifier, as shown here:
# print(format(12345.6789, ',.2f'))
# print(format(123456789.456, ',.2f'))
# print(format(12345.6789, ',f'))

#### specifying a Minimum Field Width
#The following example prints a number in a field that is 12 spaces wide:
# print('The number is', format(12345.6789, '12,.2f'))

# num1 = 127.899
# num2 = 3465.148
# print('num is',format(num1,'7.2f'))  # 7 is the indentation and 2f is the number of fraction after decimal point
# print('num is',format(num2,'7,.2f'))
# print(format(0.5, '%'))

# # Get the item's original price.
# # Exponentiation: **
# # Multiplication *, division /, integer (whole number) // and remainder: * / // %
# # Addition and subtraction: + −
# original_price = float(input("Enter the item's original price: "))
# # Calculate the amount of the discount.
# discount = original_price * 0.2
# # Calculate the sale price.
# sale_price = original_price - discount
# # Display the sale price.
# print('The sale price is', sale_price)


# ########## (time_converter.py)
# # Get a number of seconds from the user.
# total_seconds = float(input('Enter a number of seconds: '))
# # Get the number of hours.
# hours = total_seconds // 3600
# # Get the number of remaining minutes.
# minutes = (total_seconds // 60) % 60
# # Get the number of remaining seconds.
# seconds = total_seconds % 60
# # Display the results.
# print('Here is the time in hours, minutes, and seconds:')
# print('Hours:', hours)
# print('Minutes:', minutes)
# print('Seconds:', seconds)


# ########### (future_value.py) P = F/(1 + r)**n
# # Get the desired future value.
# future_value = float(input('Enter the desired future value: '))
# # Get the annual interest rate.
# rate = float(input('Enter the annual interest rate: '))
# # Get the number of years that the money will appreciate.
# years = int(input('Enter the number of years the money will grow: '))
# # Calculate the amount needed to deposit.
# present_value = future_value / (1.0 + rate)**years
# # Display the amount needed to deposit.
# print('You will need to deposit this amount:', present_value)


#Escape Character   Effect
#   \n              Causes output to be advanced to the next line.
#   \t              Causes output to skip over to the next horizontal tab position.
#   \'              Causes a single quote mark to be printed.
#   \"              Causes a double quote mark to be printed.
#   \\              Causes a backslash character to be printed.


########  specifying an item separator
print('One', 'Two', 'Three')
print('One', 'Two', 'Three', sep='')
print('One', 'Two', 'Three', sep='*')
print('One', 'Two', 'Three', sep='˜˜˜')

########  escape Characters
print('One\nTwo\nThree')
print('Mon\tTues\tWed')
print('Thur\tFri\tSat')


