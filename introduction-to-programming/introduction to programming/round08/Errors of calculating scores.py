def main():
    file_name=input('Enter the name of the score file: ')
    try:
        score_sheet=open(file_name,'r')
        names=[]
        scores=[]
        for line in score_sheet:
            ind_record=line.split(' ')
            #creating error
            if len(ind_record)!=2:
                error = line
                ind_record.count()
            names.append(ind_record[0])
            num_error=ind_record[1].rstrip('\n')
            scores.append(int(ind_record[1].rstrip('\n')))
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

        final_dict={}
        for z in range(len(names)):
            final_dict[names[z]]=scores[z]
        arraged=sorted(final_dict)
        print('Contestant score:')
        for p in range(len(arraged)):
            ordered=arraged[p]
            print(ordered,final_dict[ordered],sep=' ')
    except TypeError:
        print('There was an erroneous line in the file:')
        print(error)
    except ValueError:
        print('There was an erroneous score in the file:')
        print(num_error)
    except:
        print('There was an error in reading the file.')

main()
