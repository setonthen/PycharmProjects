# Johdatus ohjelmointiin
# Parasetamol

def main():

    weight=int(input("Patient's weight (kg): "))
    time_passed=int(input("How much time has passed from the previous dose (full hours): "))
    dose_taken=int(input("The total dose for the last 24 hours (mg): "))
    dose_needed=calculate_dose(weight,time_passed,dose_taken)
    print("The amount of Parasetamol to give to the patient: ",int(dose_needed))

def calculate_dose(w,t,d_t):
    if t>=6 and t!=24:
        required_dose=w*15*(t/6)
        total_dose=required_dose+d_t
        if total_dose>4000:
            take_it=4000-d_t
        else:
            take_it=required_dose
    elif t==24:
        second_limit=w*15
        if second_limit>4000:
            take_it=4000
        else:
            take_it=second_limit
    else:
        take_it=0
    return take_it

main()
