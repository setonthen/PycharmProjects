def main():
    player_name,points=seperate_elements()
    rev_name,rev_scores=summed_list(player_name,points)
    to_print(rev_scores,rev_name)

def seperate_elements():
    file_name = input('Enter the name of the score file: ')
    score_sheet = open(file_name, 'r')
    names=[]
    scores=[]
    for line in score_sheet:
        ind_record=line.split(' ')
        names.append(ind_record[0])
        scores.append(int(ind_record[1].rstrip('\n')))
    score_sheet.close()
    return names, scores

def summed_list(names,scores):
    x = 0
    y = 0
    while x != len(names):
        while y != len(names):
            if names[x] == names[y] and x != y:
                scores[x] += scores[y]
                y += 1
            else:
                y += 1
        x += 1
        y = x
    scores.reverse()
    names.reverse()
    return names,scores

def to_print(scores,names):
    final_dict={}
    for z in range(len(names)):
        final_dict[names[z]]=scores[z]
    arraged=sorted(final_dict)
    print('Contestant score:')
    for p in range(len(arraged)):
        ordered=arraged[p]
        print(ordered,final_dict[ordered],sep=' ')

main()

