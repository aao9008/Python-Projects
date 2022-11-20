print('Please enter weight in kilograms:')
weight= float(input())
print('Please enter height in meters:')
height= float(input())

bmi= weight/(height**2)
new_bmi= round(bmi,2)

if (new_bmi > 30.0):
    status= "obese"
elif (new_bmi < 29.9 and new_bmi > 25.0):
    status= "Overweight"
elif (new_bmi < 24.9 and new_bmi > 18.5):
    status= "Normal"
elif (new_bmi < 18.5):
    status= "Underweight"

print('BMI is: ', new_bmi,", Status is ", status, sep='')