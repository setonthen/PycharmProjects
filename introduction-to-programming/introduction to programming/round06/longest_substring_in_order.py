def longest_substring_in_order(text):
    count = 0
    max_count = 0
    index = 0
    x = 0
    char = ''
    if len(text)==1:
        char+=text[0]
    elif len(text)==0:
        char
    else:
        while x != len(text) - 1:
            if text[x] < text[x + 1]:
                count += 1
                if max_count < count:
                    max_count = count
                    index = x
                x += 1
            else:
                count = 0
                x += 1
        if max_count==0:
            start=0
            char+=text[0]
        else:
            start = index - (max_count - 1)
            end = start + max_count
        for z in range(start, end + 1):
            char += text[z]
    return char
