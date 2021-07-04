def count_abbas(text):
    count=0
    x=0
    while x<len(text)-3:
        if text[x]=='a':
            if text[x+1]=='b':
                if text[x+2]=='b':
                    if text[x+3]=='a':
                        count+=1
                        x+=1
                    else:
                        x+=1
                else:
                    x+=1
            else:
                x+=1
        else:
            x+=1
    return count

