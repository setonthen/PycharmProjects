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

AREACODE=[]
for doorcode, areacode in DOORCODES.items():
    for items in areacode:
        AREACODE.append(items)

class Accesscard:

    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.
        :param id: card holders personal id (str)
        :param name: card holders name (str)

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME OR THE
        PARAMETERS!
        """
        self.id=id
        self.name=name
        file = open('accessinfo.txt', 'r')
        all_info = {}
        read_info(file, all_info)
        self.codes = sorted(all_info[id][self.name])
        # pass  # TODO: Implement the constructor




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
        redundants=[]
        for y in self.codes:
            if y in DOORCODES:
                for z in self.codes:
                    if z in DOORCODES[y]:
                        redundants.append(y)
        for x in range(len(redundants)):
            self.codes.remove(redundants[x])
        print(self.id+', '+self.name+', '+'access:',end=' ')
        for x in range(len(self.codes)):
            if x==len(self.codes)-1:
                print(self.codes[x])
            else:
                print(self.codes[x],end=', ')

        #pass # TODO: Implement the method



    def get_name(self):
        """
        :return: Returns the name of the accesscard holder.
        """
        return self.name
    #pass  # TODO: Implement the method


    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.
        :param new_access_code: The accesscode to be added in the card.
        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """
        if new_access_code not in self.codes:
            self.codes.append(new_access_code)
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
        if door in self.codes:
            return True
        else:
            return False
    #pass  # TODO: Implement the method


    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: The accesscard whose access rights are added to this card.
        :return:
        """

        pass  # TODO: Implement the method



def main():
    # TODO: Implement the reading of the inputfile and storing the information.
    file=open('accessinfo.txt','r')
    all_info ={}
    read_info(file,all_info)
    card_id=''
    name=''
    card=Accesscard(card_id,name)

    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        if command == "list" and len(strings) == 1:
            ordered=sorted(all_info)
            for x in range(len(ordered)):
                to_print=ordered[x]
                print(to_print,end=', ')
                for name,codes in all_info[to_print].items():
                    print(name+', access:',end=' ')
                    for y in range(len(codes)):
                        if y==len(codes)-1:
                            print(codes[y])
                        else:
                            print(codes[y],end=', ')


            #pass # TODO: Excecute the command list here

        elif command == "info" and len(strings) == 2:
            card_id = strings[1]
            name=get_name(card_id,all_info)
            card.info()

            #pass  # TODO: Excecute the command info here

        elif command == "access" and len(strings) == 3:
            card_id = strings[1]
            door_id = strings[2]
            if card_id in all_info:
                name = get_name(card_id, all_info)
                card = Accesscard(card_id, name)
                if door_id in DOORCODES:
                    if card.check_access(door_id)==True:
                        print('Card ' + card_id + '( ' + name + ' )' +
                              ' has access to door ' + door_id)
                    else:
                        print('Card ' + card_id + '( ' + name + ' )' +
                              ' has no access to door ' + door_id)
                else:
                    print('Error: unknown doorcode.')
            else:
                print('Error: unknown id.')

            #pass  # TODO: Excecute the command access here

        elif command == "add" and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]
            if card_id in all_info:
                name = get_name(card_id, all_info)
                card = Accesscard(card_id, name)
                if access_code in DOORCODES or access_code in AREACODE:
                    card.add_access(access_code)
                    card.info()
                else:
                    print('Error: unknown accesscode.')

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

def read_info(filename,list):
    name_area = {}
    for line in filename:
        ind_info=line.rstrip('\n')
        splitted = ind_info.split(';')
        if len(splitted) == 2:
            name_area[splitted[1]] = []
        else:
            codes=splitted[2].split(',')
            codes.sort()
            name_area[splitted[1]] =codes
        list[splitted[0]] = name_area
        name_area={}

def get_name(card_id,list):
    if card_id in list:
        for k, v in list[card_id].items():
            name = k
        return name
    else:
        print('Error: unknown id.')

main()
