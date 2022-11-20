print('Please enter weight in pounds:')
weight= float(input())
print('Please enter height in inches:')
height= float(input())

imperial_height= height * 0.0254
imperial_weight= weight * 0.453592

bmi= imperial_weight/(imperial_height**2)
new_bmi= round(bmi,10)

print('BMI is:',new_bmi)