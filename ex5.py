# Firstly I initialize all the necessary variables 
total_marks = int()
total_students = int()
hd_students = int()
d_students = int()
c_students = int()
p_students = int()
n_students = int()

# I start a while loop
while True:
    # I take marks as inputs
    student_marks = input("enter the marks: ")
    # I state the break condition
    if student_marks.lower() == 'end':
        break
    # I turn the marks into an integer
    student_marks = int(student_marks)
    # I use if-elifs to make a the different comparisons. Inside, I increase all necessary variables
    if student_marks >= 80:
        hd_students += 1
        total_students +=1
    elif student_marks >= 70 and student_marks < 80:
        d_students += 1
        total_students +=1
        total_marks = total_marks + student_marks
    elif student_marks >= 60 and student_marks < 70:
        c_students += 1
        total_students +=1
        total_marks = total_marks + student_marks
    elif student_marks >= 50 and student_marks < 60:
        p_students += 1
        total_students +=1
        total_marks = total_marks + student_marks
    elif student_marks < 50:
        n_students += 1
        total_students +=1
        total_marks = total_marks + student_marks
    # I print all the reports asked for
    print(f"the total marks obtained is: {total_marks}")
    print(f"total students are: {total_students}")
    print('''
          number of students in hd: {} 
          number of students in d: {} 
          number of students in c: {}
          number of students in p: {}
          number of students in n: {}'''.format(hd_students, d_students, c_students, p_students, n_students))
    print()
    print("the percentage of students failing the unit is: %d%%" %(n_students / total_students * 100))
        
        
        
    
    