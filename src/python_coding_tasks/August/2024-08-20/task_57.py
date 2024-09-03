# Grade calculator
# write a program that calculates the grade based on the score

score = int(input("Enter the subject score"))
grade = "F"

if 90 <= score <= 100:
    grade = "A"
    print("Grade is: ",grade)
elif 80 <= score <= 89:
    grade = "B"
    print("Grade is: ",grade)
elif 70 <= score <= 79:
    grade = "C"
    print("Grade is: ",grade)
elif 60 <= score <= 69:
    grade = "D"
    print("Grade is: ", grade)
elif score > 100:
    print("You are a superman!!")
else:
    grade = "F"
    print("Grade is: ",grade)
