# TIE-02106 Introduction to Programming
# Program Code of 'Coffee gallup'
# Mukesh Aryal, aryalm@student.tut.fi, student no: 268456

def main():
    print('Enter one response per line. End by entering an empty row.')
    consumers_response_list=get_responses()
    consumers_response_list=remove_non_coffee_drinkers(consumers_response_list)
    unsorted_list=[]+consumers_response_list
    consumers_response_list.sort()
    no_coffee_consumers = make_no_coffee_consumer_list(consumers_response_list)
    if no_coffee_consumers != consumers_response_list:
        print_response_statistics(consumers_response_list)
        print()
        print_coffee_abusers_info(consumers_response_list)
        print_over8_cups_responses(unsorted_list)

# This function collects individual response of coffee consumers
# and returns the values in the form of a list.
def get_responses():
    response_data_list=[]
    num_of_cups_per_day=0
    while num_of_cups_per_day!='':
        num_of_cups_per_day=input()
        if num_of_cups_per_day!='':
            response_data_list.append(int(num_of_cups_per_day))
    return response_data_list

# This function removes the response of non-coffee drinkers,
# prints the number of removed responses
# and returns a data list after removing non-coffee drinkers.
def remove_non_coffee_drinkers(data_sheet):
    non_drinkers = data_sheet.count(0)
    count=0
    for x in range(len(data_sheet)):
        try:
            data_sheet.remove(0)
            count+=1
        except ValueError:
            non_drinkers=count
    if count!=0:
            print('Removed '+str(non_drinkers)+' non-coffee-drinkers responses')
    print()
    return data_sheet

# This function makes a list of equal length with all elemets 0
def make_no_coffee_consumer_list(datasheet):
    no_consumers=[]+datasheet
    for x in range(len(datasheet)):
        no_consumers.insert(x,0)
    return no_consumers

# This function prints the graphical representation of input responses
# using '#' symbol and also prints the general statistics of
# coffee consumers.
def print_response_statistics(data_sheet):
    print('Information related to coffee drinkers: ')
    for x in range(min(data_sheet),max(data_sheet)+1):  # 'x' and 'y' are random
        print(format(x,'2'),end=' ')                                # variable used to address
        num_available=data_sheet.count(x)               # elements of list
        if num_available!=0:
            for y in range(num_available):
                print('#',end='')
            print()
        else:
            print()
    print()
    print('The greatest response:',max(data_sheet),
          'cups of coffee per day')
    finalized_data=find_most_common_response(data_sheet)
    print('The most common response:',finalized_data[0],'cups of coffee per day')
    print(finalized_data[3]+'% of the respondents drink '+
           finalized_data[1]+'-'+finalized_data[2]+' cups of coffee per day')



# This function finds the most common response, and its upper and lower limit
# it also calculates the percentage of responses within the range of
# limits of most common response.
def find_most_common_response(data_sheet):
    max_count=data_sheet.count(data_sheet[0])   # allocates the count of 1st element
    index=0                                     # as maximum and later changed accordingly
    for x in range(1,len(data_sheet)):
        num_of_repetition=data_sheet.count(data_sheet[x])
        if num_of_repetition>max_count:
            index=x
            max_count=num_of_repetition
    most_occuring=data_sheet[index]
    lower_limit=most_occuring-1
    upper_limit=most_occuring+1
    lower_limit_count=data_sheet.count(lower_limit)
    upper_limit_count=data_sheet.count(upper_limit)
    result_percentage=(((max_count+lower_limit_count+
                        upper_limit_count)/len(data_sheet)*100))
    result=[str(most_occuring),str(lower_limit),
            str(upper_limit),str(format(result_percentage,'.1f'))]
    return result

# This function prints the information on coffee abusers: more than 4 cups,
# in between 5-8 cups and over 8 cups.
def print_coffee_abusers_info(list):
    more_info = extra_info(list)
    if more_info[4] > 0:  # condition that checks if there are any responses
                          # more than 4 cups of coffee per day
        print('Information related to coffee abusers: ')
        more_info_list = extra_info(list)
        print(more_info_list[0]+'%'+' of the respondents drink '
                                    'more than 4 cups of coffee per day')
        print(more_info_list[2]+" respondents drink a little "
                                "too much coffee (5-8 cups per day)")
        print(more_info_list[3]+' respondents drink over double the recommendation')

# This function finds the number of responses above: 4 cups per day,
# in between 5-8 cups and over 8 cups
# it also calculates the percentage of people who drink
# more than 4 cups of coffee per day
# in the end, it returns the calculated value as a list.
def extra_info(list):
    count_4_moreCups=0
    count5_8Cups = 0
    count_over8Cups=0
    for x in range(len(list)):
        if list[x]>4:
            count_4_moreCups+=1
        if list[x]>4 and list[x]<9:
            count5_8Cups+=1
        if list[x]>8:
            count_over8Cups+=1

    moreThan4cups=(count_4_moreCups/len(list))*100
    additional_info=[str(format(moreThan4cups,'.1f')),count_over8Cups,
                     str(count5_8Cups),str(count_over8Cups),count_4_moreCups]
    return additional_info

# This function prints the last section of the program listing
# all the coffee abuser's responses above 8 cups of coffee per day.
def print_over8_cups_responses(list):
    more_info=extra_info(list)
    if more_info[1]>0:  # condition that checks if there are any responses
                        # over 8 cups of coffee per day.
        print('The responses over 8 cups of coffee per day: ')
        for x in range(len(list)):
            if list[x]>8:
                print(list[x])

main()