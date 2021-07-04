# TIE-02106 Introduction to Programming
# Solution of task Access control system
# Ujjwal Aryal, ujjwal.aryal@student.tut.fi
# student no: 268447


DOORCODES = {'TC114': ['TIE'], 'TC203': ['TIE'], 'TC210': ['TIE', 'TST'],
             'TD201': ['TST'], 'TE111': [], 'TE113': [], 'TE115': [],
             'TE117': [], 'TE102': ['TIE'], 'TD203': ['TST'], 'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'], 'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'], 'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'], 'TB104': ['OPET'], 'TB205': ['G'],
             'SM111': [], 'SM112': [], 'SM113': [], 'SM114': [],
             'S1': ['OPET'], 'S2': ['OPET'], 'S3': ['OPET'], 'S4': ['OPET'],
             'K1705': ['OPET'], 'SB100': ['G'], 'SB202': ['G'],
             'SM220': ['ELT'], 'SM221': ['ELT'], 'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'], 'TB': ['G'], 'SA': ['G'], 'KA': ['G']}


class Accesscard:
    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.
        :param id: card holders personal id (str)
        :param name: card holders name (str)

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME OR THE
        PARAMETERS!
        """
        pass
        self.__id = id
        self.__name = name
        self.__access = []

    def info(self):
        """
        The method has no return value. It prints the information related to
        the access card in the format:
        id, name, access: a1,a2,...,aN
        for example:
        777, Thelma Teacher, access: OPET, TE113, TIE
        Note that the space characters after the commas and semicolon need to
        be as specified in the task description or the test fails.
        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE PRINTOUT FORMAT!
        """

        # CREATING  A LIST OF ACCESS IN PRINTABLE FORM and printing the result

        access_list = []
        for datas in sorted(self.__access):
            if datas in DOORCODES:
                door_name = DOORCODES[datas]
                num = 0
                for keys in door_name:
                    if keys in self.__access:
                        num += 1
                if num == 0:
                    access_list.append(datas)
            else:
                access_list.append(datas)

        self.__access = access_list

        print(self.__id + ",", self.__name + ", access: ",end="")

        if len(self.__access) != 0:
            number = 1
            for items in sorted(self.__access):
                if len(self.__access) == number:
                    print(items)
                    number = 0
                else:
                    print(items+", ",end="")
                    number += 1
        else:
            print()

    def get_name(self):
        """
        :return: Returns the name of the accesscard holder.
        """
    pass

    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.
        :param new_access_code: The accesscode to be added in the card.
        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """
        # this method checks if the new access code is already in the current access
        # list, to be an access code all the characters has to be in Upper case
        # Acess code can be of a single door or for the whole department hence
        # the vaues of the DOORCOEES dic also needs to be checked

        if new_access_code not in self.__access:
            if new_access_code.isupper():
                if new_access_code in DOORCODES:
                    self.__access.append(new_access_code)
                else:
                    number = 0
                    for elements in DOORCODES:
                        DOORCODES_values = DOORCODES[elements]
                        if new_access_code in DOORCODES_values:
                            self.__access.append(new_access_code)
                            number += 1
                            break
                    if number == 0:
                        print("Error: unknown accesscode.")
            else:
                print("Error: unknown accesscode.")


    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.
        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """
        door_allowed = DOORCODES[door]
        if door in self.__access:
            return True
        else:
            for elements in door_allowed:
                if elements in self.__access:
                    return True
                else:
                    return False


    def access(self,door):

        # this method checks if the given id has access to the given door
        # and prints the information in return whether or not the given id has
        #access to the given door
        allowed = []
        for items in self.__access:
            for names in DOORCODES:
                DOORCODES_values = DOORCODES[names]
                if items in DOORCODES_values:
                    allowed.append(names)
        for name_door in self.__access:
            allowed.append(name_door)

        if door in DOORCODES:
            if door in allowed:
                print("Card",self.__id,"(",self.__name\
                      ,")","has access to door",door)
            else:
                print("Card",self.__id,"(",self.__name\
                      ,")","has no access to door",door)
        else:
            print("Error: unknown doorcode.")


    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: The accesscard whose access rights are added to this card.
        :return:
        """
        to_add = card.__access
        for elements in to_add:
            if elements in self.__access:
                continue
            else:
                self.__access.append(elements)




def main():
    # reading the inputfile and storing the information in suitable data structure.
    try:
        registry = open("accessinfo.txt", "r")
        id_list = {}
        for datas in registry:
            id, name, access = datas.rstrip("\n").split(";")
            id_list[id] = Accesscard(id, name)
            if len(access) == 0:
                continue
            else:
                access_list = access.split(",")
                for valuess in access_list:
                    id_list[id].add_access(valuess)

        # making sure that the same id doesnot exist more than once

        for items in id_list:
            counter = 0
            for elements in id_list:
                if items == elements:
                    counter += 1
                if counter > 1:
                    raiseerror = int("LOL")
        registry.close()

        while True:
                line = input("command> ")

                if line == "":
                    break

                strings = line.split()
                command = strings[0]

                if command == "list" and len(strings) == 1:
                    pass
                    for ids in sorted(id_list):
                        id_list[ids].info()

                elif command == "info" and len(strings) == 2:
                    card_id = strings[1]
                    pass
                    if card_id in id_list:
                        id_list[card_id].info()
                    else:
                        print("Error: unknown id.")

                elif command == "access" and len(strings) == 3:
                    card_id = strings[1]
                    door_id = strings[2]
                    pass
                    if card_id in id_list:
                        id_list[card_id].access(door_id)
                    else:
                        print("Error: unknown id.")

                elif command == "add" and len(strings) == 3:
                    card_id = strings[1]
                    access_code = strings[2]
                    pass
                    if card_id in id_list:
                        id_list[card_id].add_access(access_code)
                    else:
                        print("Error: unknown id.")

                elif command == "merge" and len(strings) == 3:
                    card_id_to = strings[1]
                    card_id_from = strings[2]
                    pass
                    if card_id_to in id_list:
                        id_list[card_id_to].merge(id_list[card_id_from])
                    else:
                        print("Error: unknown id.")

                elif command == "quit":
                    print("Bye!")
                    return
                else:
                    print("Error: unknown command.")

    except:
        print("Error: file cannot be read.")


main()
