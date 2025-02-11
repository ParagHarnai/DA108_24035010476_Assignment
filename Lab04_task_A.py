maths_grade = 'Z'
physics_grade = 'Z'
chemistry_grade = 'Z'
overall_grade = 'Z'

student_name = ''
roll_no = 0
maths_marks = 0
physics_marks = 0
chemistry_marks = 0
avg_marks = 0.0

while not student_name:
    try:
        student_name = str(input("Enter Student Name: "))
    except Exception as err:
        print(f"Invalid student name, unexpected {err=} of {type(err)=} occurred.")
    else:
        if not(student_name.replace(" ", "").isalpha()):
            student_name = ''
            continue
        else:
            break

while not roll_no:
    try:
        roll_no = int(input(f"Enter Roll No. for {student_name}: "))
    except ValueError:
        print(f"Invalid {roll_no=}. Enter only numeric roll number, try again!")
    except Exception as err:
        print(f"Invalid roll number, unexpected {err=} of {type(err)=} occurred.")

while True:
    try:
        maths_marks = int(input(f"Enter marks (out of 100) in Maths, for {student_name}: "))
    except ValueError:
        print(f"Invalid {maths_marks=}. Enter only numbers for marks, try again!")
    except Exception as err:
        print(f"Invalid marks, unexpected {err=} of {type(err)=} occurred.")
    else:
        if maths_marks > 100:
            continue
        else:
            break
while True:
    try:
        physics_marks = int(input(f"Enter marks (out of 100) in Physics, for {student_name}: "))
    except ValueError:
        print(f"Invalid {physics_marks=}. Enter only numbers for marks, try again!")
    except Exception as err:
        print(f"Invalid marks, unexpected {err=} of {type(err)=} occurred.")
    else:
        if physics_marks > 100:
            continue
        else:
            break

while True:
    try:
        chemistry_marks = int(input(f"Enter marks (out of 100) in Chemistry, for {student_name}: "))
    except ValueError:
        print(f"Invalid {chemistry_marks=}. Enter only numbers for marks, try again!")
    except Exception as err:
        print(f"Invalid marks, unexpected {err=} of {type(err)=} occurred.")
    else:
        if chemistry_marks > 100:
            continue
        else:
            break

if maths_marks > 100:
    pass
elif maths_marks <= 100 and maths_marks >= 90:
    maths_grade = 'A'
elif maths_marks < 90 and maths_marks >= 80:
    maths_grade = 'B'
elif maths_marks < 80 and maths_marks >= 70:
    maths_grade = 'C'
elif maths_marks < 70 and maths_marks >= 60:
    maths_grade = 'D'
else:
    maths_grade = 'F'

if physics_marks > 100:
    pass
elif physics_marks <= 100 and physics_marks >= 90:
    physics_grade = 'A'
elif physics_marks < 90 and physics_marks >= 80:
    physics_grade = 'B'
elif physics_marks < 80 and physics_marks >= 70:
    physics_grade = 'C'
elif physics_marks < 70 and physics_marks >= 60:
    physics_grade = 'D'
else:
    physics_grade = 'F'

if chemistry_marks > 100:
    pass
elif chemistry_marks <= 100 and chemistry_marks >= 90:
    chemistry_grade = 'A'
elif chemistry_marks < 90 and chemistry_marks >= 80:
    chemistry_grade = 'B'
elif chemistry_marks < 80 and chemistry_marks >= 70:
    chemistry_grade = 'C'
elif chemistry_marks < 70 and chemistry_marks >= 60:
    chemistry_grade = 'D'
else:
    chemistry_grade = 'F'

avg_marks = (maths_marks+physics_marks+chemistry_marks)/3
if avg_marks > 100:
    overall_grade = 'Z'
elif avg_marks <= 100 and avg_marks >= 90:
    overall_grade = 'A'
elif avg_marks < 90 and avg_marks >= 80:
    overall_grade = 'B'
elif avg_marks < 80 and avg_marks >= 70:
    overall_grade = 'C'
elif avg_marks < 70 and avg_marks >= 60:
    overall_grade = 'D'
else:
    overall_grade = 'F'

print(f"Here is the grade card:\n")
print(f"Student Name:       {student_name:<50}")
print(f"Student Roll:       {roll_no:<10}")
print(f"Grade in Maths:     {maths_grade:<2}")
print(f"Grade in Physics:   {physics_grade:<2}")
print(f"Grade in Chemistry: {chemistry_grade:<2}")
print(f"Overall Grade:      {overall_grade:<2}")
print("Thank you!")