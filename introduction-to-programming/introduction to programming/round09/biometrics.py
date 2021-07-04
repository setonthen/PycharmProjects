# Introduction to Programming K2017
# Mukesh Aryal, Student_no: 268456, Science and Engineering
# Email: mukesh.aryal@student.tut.fi
# Biometric-Recoginition
###############################################################################
# read_biometric_registry(filename)                                                     
# =========================================
# Function reads the biometric information from the file whose name is in
# the parameter filename. The read information will be parsed and saved in 
# the data structure that is in the variable called result. The coder has
# to define the data structure by him/herself.
# After successfully reading the file and saving its contents in the data
# structure, the function returns the result. If there's an error, None is
# returned.
#         
# PLEASE NOTE:
# (a) Implement all parts of the code that say TODO.
# (b) The data structure returned by the function must be something that
#     that nests lists and/or dicts. That is the wole point of this project:
#     to use nested data structures.
###############################################################################

import math
def read_biometric_registry(filename):

    result = []

    handled_passports = []

    try:
        with open(filename, "r") as file_object:
            for row in file_object:
                row = row.rstrip("\n")

                fields = row.split(";")

                if len(fields) != 8:
                    print("Error: there is a wrong number of fields in the file:")
                    print("'", row, "'", sep="")
                    return None

                for ind in range(3, 8):
                    fields[ind] = float(fields[ind])
                    if not (0 <= fields[ind]<= 3.0):
                        print("Error: there is a erroneous value in the file:")
                        print("'", row, "'", sep="")
                        return None

                name = fields[0] + ", " + fields[1]
                passport = fields[2]

                biometric = fields[3:]

                if passport in handled_passports:
                    print("Error: passport number", passport, "found multiple times.")
                    return None

                else:
                    handled_passports.append(passport)
                    final_record = (name,passport,biometric)
                    result.append(final_record)

        return result

    except FileNotFoundError:
        print("Error: file", filename, "could not be opened.")

    except ValueError:
        print("Error: there's a non-numeric value on row:")
        print("'", row, "'", sep="")

    return None


def execute_match(registry):
    match_founds = []
    for elements in registry:

        values = elements[2]



        counter = 0
        another_counter = 0

        for ag_elements in registry:

            counter += 1



            ag_values = ag_elements[2]
            if values != ag_values and ag_elements not in match_founds:

                # number of first "for" loop

                num_1 = float(values[0])
                num_2 = float(values[1])
                num_3 = float(values[2])
                num_4 = float(values[3])
                num_5 = float(values[4])

                # numbers of second "for" loop

                ag_num_1 = float(ag_values[0])
                ag_num_2 = float(ag_values[1])
                ag_num_3 = float(ag_values[2])
                ag_num_4 = float(ag_values[3])
                ag_num_5 = float(ag_values[4])

                # calculating if it is less than 0,1

                result = math.sqrt(
                    (num_1-ag_num_1)** 2 + (num_2-ag_num_2)** 2 + \
                    (num_3-ag_num_3)** 2 + (num_4-ag_num_4)** 2 + \
                    (num_5-ag_num_5)** 2
                )

                if result < 0.1 and elements not in match_founds:

                    another_counter += 1

                    match_founds.append(elements)

                    name = elements[0]
                    pass_num = elements[1]
                    numbers = elements[2]

                    print('Probably the same person:')
                    print(
                        name + ";" + pass_num + ";" + str(
                            format(numbers[0], ".2f")) + ";" + str(
                            format(numbers[1], ".2f")) + \
                        ";" + str(format(numbers[2], ".2f")) + ";" + str(
                            format(numbers[3], ".2f")) + ";" + str(
                            format(numbers[4], ".2f")))


                if result < 0.1:

                    match_founds.append(ag_elements)

                    ag_name = ag_elements[0]
                    ag_pass_num = ag_elements[1]
                    ag_numbers = ag_elements[2]

                    print(
                        ag_name + ";" + ag_pass_num + ";" + str(
                            format(ag_numbers[0], ".2f")) + ";" + str(
                            format(ag_numbers[1], ".2f")) + \
                        ";" + str(format(ag_numbers[2], ".2f")) + ";" + str(
                            format(ag_numbers[3], ".2f")) + ";" + str(
                            format(ag_numbers[4], ".2f")))


            if  another_counter == 1 and counter == len(registry):
                another_counter = 0
                counter = 0
                print()


    if len(match_founds) == 0:
        print("No matching persons were found.")


def execute_search(registry):
    # TODO

    num_1,num_2,num_3,num_4,num_5 = error_in_search()

    suspects = []
    for elements in registry:
        values = elements[2]
        result = float(math.sqrt(
            (num_1-values[0])**2 + (num_2-values[1])**2 +\
            (num_3-values[2])**2 + (num_4-values[3])**2 + \
            (num_5-values[4])**2))

        name = elements[0]
        pass_num = elements[1]
        printing = name+";"+pass_num+";"+str(format(values[0],".2f"))+";"\
            +str(format(values[1],".2f"))+";"+str(format(values[2],".2f"))\
                   +";"+str(format(values[3],".2f"))+";"+str(format(values[4],".2f"))

        if result <  0.1:
            suspects.append(printing)

    if len(suspects) > 0:
        print("Suspects found:")
        for elements in suspects:
            print(elements)
        print()
    else:
        print("No suspects were found.")
        print()
###############################################################################
# command_line_user_interface
# Very simple user interface. It might be good to add some helper functions.
#
###############################################################################
def command_line_user_interface(registry):
    while True:
        command = input("command [search/match/<enter>] ")
        if command == "":
            return False
        elif command == "match":
            execute_match(registry)

        elif command == "search":
            execute_search(registry)
        else:
            print("Error: unknown command '", command,
                  "': try again.", sep="")




###############################################################################

# main()                                                                      #
# ======                                                                      #
# Main program for the project. You're not supposed to edit this.
#

###############################################################################
def main():
    registry_file = input("Enter the name of the registry file: ")

    biometric_registry = read_biometric_registry(registry_file)
    if biometric_registry is not None:
        command_line_user_interface(biometric_registry)

def error_in_search():

    while True:
        numbers = input("enter 5 measurement points separated by semicolon: ")

        try:
            number = numbers.split(";")

            while len(number) != 5:
                print("Error: wrong number of measurements. Try again.")

                numbers = input("enter 5 measurement points separated by semicolon: ")
                number = numbers.split(";")



            num_1 = float(number[0])
            num_2 = float(number[1])
            num_3 = float(number[2])
            num_4 = float(number[3])
            num_5 = float(number[4])

            return num_1, num_2, num_3, num_4, num_5

        except ValueError:
            print("Error: enter floats only. Try again.")
main()