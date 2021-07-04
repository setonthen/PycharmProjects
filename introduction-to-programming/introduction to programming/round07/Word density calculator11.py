def black_list():
    black_list = ""
    print("Enter rows of text for word counting. Empty row to quit.")
    words = input("")
    if words != "":
        black_list += words.lower()

    while words != "":
        words = input()
        if words != "":
            black_list += " "
            black_list += words.lower()
    black_list=sorted(black_list.split())

    d = {x:black_list.count(x) for x in black_list}
    for k,v in sorted(d.items()):
        print(k,':',v,'times')

black_list()