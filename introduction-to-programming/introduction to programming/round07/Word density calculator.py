def main():
    list=get_words()
    whole={}
    for x in range(len(list)):
        word_count=list.count(list[x])
        whole[list[x].lower()]=word_count
    for word,count in whole.items():
        print(word,':',count,'times',sep=' ')

def get_words():
    print('Enter rows of text for word counting. Empty row to quit.')
    word_list=[]
    while True:
        item=input().lower()
        if item=='':
            break
        else:
            item_list=item.split()
            word_list+=item_list
    sorted_list=sorted(word_list)
    return sorted_list

main()