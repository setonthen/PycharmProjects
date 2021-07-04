def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    print("ROT13:")
    for x in range(len(msg)):
        print(row_encryption(msg[x]))

def read_message():
    text='s'
    row_list=[]
    while text!='':
        text=input()
        if text!='':
            row_list.append(text)
    return row_list

def encrypt(alphabet):
    REGULAR_CHARS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
                        "x", "y", "z"]

    ENCRYPTED_CHARS = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
                            "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                            "j", "k", "l", "m"]
    alphabet=change_alphabet(alphabet,REGULAR_CHARS,ENCRYPTED_CHARS)
    return alphabet

def change_alphabet(alpha,reg_char,encryp_char):
    try:
        for x in range(len(reg_char)):
            if alpha==reg_char[x].upper():
                order_no=x
                return encryp_char[order_no].upper()
        else:
            location = reg_char.index(alpha)
            return encryp_char[location]

    except ValueError:
        return alpha

def row_encryption(test_char):
    out_char=''
    for x in test_char:
        add_this=encrypt(x)
        out_char+=add_this
    return out_char

main()
