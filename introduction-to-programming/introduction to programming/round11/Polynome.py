# TIE-02106 Introduction to Programming
# Solution of task 'Polynome', C-task
# MUKESH ARYAL, aryalm@student.tut.fi, student no: 268456

class Polynome:
    def __init__(self,factor,exponent):
        self.factor=factor
        self.exponent=exponent

    def make_polynomial(self):
        if self.factor.count(0) == len(self.factor):
            print('0')
        else:
            for p in range(len(self.factor)):
                if p==len(self.factor)-1 and self.factor[p]!=0:
                    print(str(self.factor[p])+'x^'+str(self.exponent[p]))
                elif p!=len(self.factor)-1 and self.factor[p]!=0:
                    print(str(self.factor[p]) + 'x^' + str(self.exponent[p]),end=' + ')


    def addition(self,to_add):
        result_fac,result_exp=process_addition(self.factor,self.exponent,
                            to_add.factor,to_add.exponent)
        resultant=Polynome(result_fac,result_exp)
        print('The simplified result:')
        resultant.make_polynomial()

    def substraction(self,to_deduct):
        result_fac, result_exp = process_substration(self.factor, self.exponent,
                                to_deduct.factor,to_deduct.exponent)
        resultant = Polynome(result_fac, result_exp)
        print('The simplified result:')
        resultant.make_polynomial()

    def multiplication(self,to_multiply):
        result_fac, result_exp = process_multiplication(self.factor, self.exponent,
                                to_multiply.factor,to_multiply.exponent)
        resultant = Polynome(result_fac, result_exp)
        print('The simplified result:')
        resultant.make_polynomial()



def main():
    file_name = input('Enter file name: ')
    try:
        file = open(file_name, 'r')
        all_polymials=make_ind_polynome(file)
        polynome_dict=assign_memory_location(all_polymials)
        command=input('>')
        while command!= 'quit':
            try:
                splitted = command.split(' ')
                location_1, operator, location_2 = int(splitted[0]), \
                                                   splitted[1], int(splitted[2])
                if location_1>len(polynome_dict) or location_2>len(polynome_dict):
                    print('Error: the given memory location does not exist.')
                else:
                    if operator == '+':
                        print_polynomials(location_1, location_2, polynome_dict)
                        polynome_dict[location_1].addition(polynome_dict[location_2])

                    elif operator == '-':
                        print_polynomials(location_1, location_2, polynome_dict)
                        polynome_dict[location_1].substraction(
                            polynome_dict[location_2])

                    elif operator == '*':
                        print_polynomials(location_1, location_2, polynome_dict)
                        polynome_dict[location_1].multiplication(
                            polynome_dict[location_2])
                    else:
                        print('Error: unknown operator.')
            except:
                print('Error: entry format is memory_location operation memory_location.')
            command=input('>')

        if command == 'quit':
            print('Bye bye!')

    except FileNotFoundError:
        print('Error in reading the file.')



def process_addition(list1_fac, list1_exp, list2_fac, list2_exp):
    index = 0
    new_fac = []
    new_exp = []
    flag1 = False
    flag2 = False
    while index != len(list1_exp):
        for x in range(len(list2_exp)):
            if list1_exp[index] == list2_exp[x]:
                flag1 = True
                if flag1 == True:
                    result = list1_fac[index] + list2_fac[x]
                    new_fac.append(result)
        if flag1 == False:
            new_fac.append(list1_fac[index])
        new_exp.append(list1_exp[index])
        index += 1

    for y in range(len(list2_exp)):
        for z in range(len(list1_exp)):
            if list1_exp[z] == list2_exp[y]:
                flag2 = True
        if flag2 == False:
            new_exp.append(list2_exp[y])
            new_fac.append(list2_fac[y])
        flag2=False
    final_fac, final_exp = arrage_elements(new_fac, new_exp)
    return final_fac, final_exp

def process_substration(list1_fac, list1_exp, list2_fac, list2_exp):
    index = 0
    new_fac = []
    new_exp = []
    flag1 = False
    flag2 = False
    while index != len(list1_exp):
        for x in range(len(list2_exp)):
            if list1_exp[index] == list2_exp[x]:
                flag1 = True
                if flag1 == True:
                    result = list1_fac[index] - list2_fac[x]
                    new_fac.append(result)
        if flag1 == False:
            new_fac.append(-list1_fac[index])
        new_exp.append(list1_exp[index])
        index += 1

    for y in range(len(list2_exp)):
        for z in range(len(list1_exp)):
            if list1_exp[z] == list2_exp[y]:
                flag2 = True
        if flag2 == False:
            new_exp.append(list2_exp[y])
            new_fac.append(-list2_fac[y])
        flag2=False
    final_fac, final_exp = arrage_elements(new_fac, new_exp)
    return final_fac, final_exp

def process_multiplication(list1_fac, list1_exp, list2_fac, list2_exp):
    new_fac = []
    new_exp = []
    index = 0
    if len(list1_exp) == 1:
        for x in range(len(list2_fac)):
            factor = list1_fac[0] * list2_fac[x]
            exponent = list1_exp[0] + list2_exp[x]
            new_fac.append(factor)
            new_exp.append(exponent)
    else:
        while index != len(list1_exp):
            for x in range(len(list2_fac)):
                factor = list1_fac[index] * list2_fac[x]
                exponent = list1_exp[index] + list2_exp[x]
                new_fac.append(factor)
                new_exp.append(exponent)
            index += 1


    final_fac, final_exp = arrage_elements(new_fac, new_exp)
    return final_fac, final_exp

def arrage_elements(list1, list2):
    terms = {}
    arr_list1 = []
    for x in range(len(list2)):
        terms[list2[x]] = list1[x]
    arr_list2 = sorted(terms, reverse=True)
    for x in range(len(arr_list2)):
        arr_list1.append(terms[arr_list2[x]])
    return arr_list1, arr_list2

def make_ind_polynome(file):
    factors = []
    exponents = []
    polynomials = []
    for line in file:
        only_num = line.rstrip('\n')
        ind_term = only_num.split(';')
        for x in ind_term:
            digit_term = x.split(' ')
            factors.append(int(digit_term[0]))
            exponents.append(int(digit_term[1]))
        ordered_fac, ordered_exp = arrage_elements(factors, exponents)
        polynome = Polynome(ordered_fac, ordered_exp)
        polynomials.append(polynome)
        factors = []
        exponents = []
    return polynomials

def assign_memory_location(polynomials):
    memory = {}
    for location in range(len(polynomials)):
        memory[location] = polynomials[location]
    return memory

def print_polynomials(loc_1, loc_2, dict):
    print('Memory location ' + str(loc_1) + ':', end=' ')
    dict[loc_1].make_polynomial()
    print('Memory location ' + str(loc_2) + ':', end=' ')
    dict[loc_2].make_polynomial()


main()
