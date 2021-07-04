def main(text):
    count=0
    max_count=0
    index=0
    x=0
    while x!=len(text)-1:
        if text[x]<text[x+1]:
            count+=1
            if max_count<count:
                max_count=count
                index=x
            x+=1
        else:
            count=0
            x+=1
    start=index-(max_count-1)
    end=start+max_count
    char=''
    for z in range(start,end+1):
        char+=text[z]
    return char

main(input())

