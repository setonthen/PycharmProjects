def read_biometric_registry(filename):
    result = {}# initialize your data structure here

    handled_passports = []

    try:
        with open(filename, "r") as file_object:
            for row in file_object:
                row = row.rstrip()

                fields = row.split(";")

                if len(fields) != 8:
                    print("Error: there is a wrong number of fields in the file:")
                    print("'", row, "'", sep="")
                    return None

                for ind in range(3, 8):
                    fields[ind] = float(fields[ind])
                    if not (0 <= fields[ind] <= 3.0):
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
                    record=

                #TODO:
                #save the read information in the result data structure

        #erturn result

    except FileNotFoundError:
        print("Error: file", filename, "could not be opened.")

    except ValueError:
        print("Error: there's a non-numeric value on row:")
        print("'", row, "'", sep="")

    return None
read_biometric_registry('test1.dat')