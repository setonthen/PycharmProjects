# TIE-02106 Introduction to Programming
# Solution of task THE CENSOR
# MUKESH ARYAL, aryalm@student.tut.fi, student no: 268456

# The following program censors the blacklisted words of a message.
# The program first acquires the words to be censored and then
# the whole message; which afterwards is censored accordingly.

def main():
    print('Enter the blacklist. Quit by entering an empty row.')
    black_list=get_black_list()
    print('Enter text rows to the message. Quit by entering'
          ' an empty row.')
    whole_list=get_whole_message()
    print('Censored message:')
    process(whole_list,black_list)

# This function gets the input for the black list from the user
# and then returns the message as a list.
def get_black_list():
    list_message = []
    while True:
        item = input()
        if item == '':
            break
        else:
            item_list = item.split()
            for words in item_list:
                list_message.append(words)
    return list_message

# This function gets the input for the whole message from the user
# and then returns the message as a list.
def get_whole_message():
    list_message = []
    while True:
        item = input()
        if item == '':
            break
        else:
            list_message.append(item)
    return list_message

# This function processes the main input which comprises
# 3 sub functions.
def process(W_list,B_list):
    for x in range(len(W_list)):
        separated=W_list[x].split()
        censor_unwanted(B_list,separated)
        final_printout(separated)

# This function censors the unwanted words from the main
# message.
# 'a' and 'b' are variables to indicate the index of the
# element of the list.
def censor_unwanted(black_list,separated):
    for a in range(len(black_list)):
        for b in range(len(separated)):
            if black_list[a].lower() == separated[b].lower():
                separated[b] = '###'

# This function prints the final censored list.
def final_printout(distinct):
    for x in range(len(distinct)):
        if x == len(distinct) - 1:
            print(distinct[x])
        else:
            print(distinct[x], end=' ')

main()

