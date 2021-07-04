# TIE-02106 Introduction to Programming
# Solution of task THE CENSOR
# MUKESH ARYAL, aryalm@student.tut.fi, student no: 268456

# The following program censors the blacklisted words of a message.
# The program first acquires the words to be censored and then
# the whole message which is later censored accordingly.

def main():
    print('Enter the blacklist. Quit by entering an empty row.')
    black_list=get_message()
    print('Enter text rows to the message. Quit by entering'
           ' an empty row.')
    whole_message=get_message()
    censored=censor_message(black_list,whole_message)
    print_censored(censored)

# This fuction gets the input from the user and then returns the
# message as a list.
def get_message():
    list_message = []
    while True:
        item=input()
        if item=='':
            break
        else:
            item_list=item.split()
            for words in item_list:
                list_message.append(words)
    return list_message

# This function checks for the word to be censored and returns
# a censored message in the form of list.
def censor_message(B_list,W_list):
    # 'x' and 'y' are random variables to denote index of the
    # element of the list.
    for x in range(len(W_list)):
        for y in range(len(B_list)):
            if W_list[x].lower()==B_list[y].lower():
                W_list[x]='###'
    return W_list

# This function prints the final censored message by converting
# list into an ordered text.
def print_censored(ready_list):
    print('Censored message:')
    output=''
    # 'x' is a random variable to denote index of the
    # element of the list.
    for x in range(len(ready_list)):
        if x!=len(ready_list)-1:
            output+=ready_list[x]+' '
        else:
            output+=ready_list[x]
    print(output)

main()



