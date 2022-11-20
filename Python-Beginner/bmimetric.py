print('Please enter weight in kilograms:')
weight= float(input())
print('Please enter height in meters:')
height= float(input())

bmi= weight/(height**2)
new_bmi= round(bmi,10)

print('BMI is:',new_bmi)