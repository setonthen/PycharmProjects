def calculate_angle(angle1, angle2=90):
    if angle2==90:
        angle3=90-angle1
        print(angle3)
        return angle3
    else:
        angle3=180-(angle1+angle2)
        print(angle3)
        return angle3
