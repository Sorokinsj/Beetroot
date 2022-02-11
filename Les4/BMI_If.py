lower_bound = 18.5
upper_bound = 25
weight = 73
height = 1.76
BMI = weight/height**2
if BMI < lower_bound:
    print('Your BMI is less than normal')
elif BMI > upper_bound:
    print('Your BMI is greater than normal')
else:
    print('Your BMI is normal')