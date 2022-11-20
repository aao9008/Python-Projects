""""
print('Please enter the number of students:')
number_of_students = int(input())

print('Enter the students grades (in separate lines):')
grade_sum = 0

for i in range(number_of_students):
    current_grade = int(input())
    grade_sum += current_grade
average = grade_sum / number_of_students

print('The class average is',average)
"""
print("Enter grades in separate lines, to end input, type 'done':")
grade_sum = 0
student_count = 0
seen_done = False

while (seen_done == False):
    curr_input = input()
    if (curr_input == 'done'):
        seen_done = True
    else:
        curr_grade= int(curr_input)
        grade_sum += curr_grade
        student_count += 1
average = grade_sum / student_count

print('The class average is',average)
