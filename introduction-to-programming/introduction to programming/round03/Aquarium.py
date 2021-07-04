#TIE-02106 Introduction to Programming
#Aquarium
#Mukesh Aryal,268456

def main():
    num_measurement=int(input("Enter the number of the measurements:"))
    if num_measurement<=0:
        print("Error: the number must be expressed as a positive integer.")
    else:
        initial_ph = float(input('Enter the measurement result ' + str(1) + ':'))
        sum_measurements=initial_ph #defining variable to calculate average later
        if num_measurement==1 and not((initial_ph < 6) or (initial_ph > 8)):
            print(("Conditions are suitable for zebra fishes."
                   "The average pH is "+str(format(initial_ph,'.2f'))+"."))
        elif (initial_ph < 6) or (initial_ph > 8):
            print("The conditions are not suitable for zebra fishes.")
        else:
            terminator_val=1 #variable to terminate loop if needed
            for x in range(2,num_measurement+1):
                if terminator_val<num_measurement+2:
                    result_x = float(
                        input('Enter the measurement result '+str(x)+':'))
                    sum_measurements+=result_x
                    change=result_x-initial_ph
                    if (change>1)or(change<-1)or(result_x<6)or(result_x>8):
                        print("The conditions are not suitable for zebra fishes.")
                        terminator_val=num_measurement+2
                    else:
                        initial_ph=result_x
                        if x == num_measurement:
                            average = sum_measurements / num_measurement
                            print((
                                  "Conditions are suitable for zebra fishes. The average pH"
                                  " is " + str(format(average, '.2f')) + "."))


main()





