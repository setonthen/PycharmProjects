# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: viesti, program code template

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    print("The same, shouting:")
    for x in range(len(msg)):
        print(msg[x].upper())

def read_message():
    text='s'
    row_list=[]
    while text!='':
        text=input()
        if text!='':
            row_list.append(text)
    return row_list
main()
