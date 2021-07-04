def main():
    official_score=calculate_score(5)
    print('The official competition score is',official_score,'seconds.',sep=' ')

def calculate_score(times):
    time_list=[]
    for x in range(1,times+1):
        score=float(input("Enter the time for performance "+str(x)+': '))
        time_list.append(score)
    time_list.remove(min(time_list))
    time_list.remove(max(time_list))
    total=0.0
    for val in time_list:
        total+=val
    result=format(total/len(time_list),'.2f')

    return result
main()
