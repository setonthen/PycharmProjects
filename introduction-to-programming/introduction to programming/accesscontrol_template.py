# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to programming
# Task: accesscontrol, program code template

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

    def __init__(self, id, name,areas):
        """
        Constructor, creates a new object that has no access rights.
        :param id: card holders personal id (str)
        :param name: card holders name (str)

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME OR THE
        PARAMETERS!
        """
        self.__id= id
        self.__name=name
        self.__areas=areas


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
        print(self.__id,end=', ')
        print(self.__name,end=', ')
        print('access:',end=' ')
        for x in self.__areas:
            if x==self.__areas[-1]:
                print(x)
            else:
                print(x,end=', ')

    def get_name(self):
        """
        :return: Returns the name of the accesscard holder.
        """

    pass  # TODO: Implement the method


    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.
        :param new_access_code: The accesscode to be added in the card.
        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

    pass  # TODO: Implement the method


    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.
        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

    pass  # TODO: Implement the method


    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: The accesscard whose access rights are added to this card.
        :return:
        """

        pass  # TODO: Implement the method



def main():
    # TODO: Implement the reading of the inputfile and storing the information.
    dict={}
    file= open('accessinfo.txt','r')
    for line in file:
        x=line.rstrip('\n')
        list=x.split(';')
        codes=list[2].split(',')
        s_codes=sorted(codes)
        dict[list[0]]=Accesscard(list[0],list[1],s_codes)
    file.close()
    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        if command == "list" and len(strings) == 1:
            for ids in dict.keys():
                dict[ids].info()
        elif command == "info" and len(strings) == 2:
            card_id = strings[1]
            try:
                dict[card_id].info()
            except:
                print('Error: unknown id.')

        elif command == "access" and len(strings) == 3:
            card_id = strings[1]
            door_id = strings[2]
            pass  # TODO: Excecute the command access here

        elif command == "add" and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]
            pass  # TODO: Excecute the command add here

        elif command == "merge" and len(strings) == 3:
            card_id_to = strings[1]
            card_id_from = strings[2]
            pass  # TODO: Excecute the command merge here

        elif command == "quit":
            print("Bye!")
            return
        else:
            print("Error: unknown command.")


main()
