import math
def compare_floats(val1,val2,EPSILON):
    if abs(val1-val2)<EPSILON:
        result=True
    else:
        result=False
    return result


