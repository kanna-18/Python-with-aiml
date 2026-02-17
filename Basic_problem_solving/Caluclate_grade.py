marks = float(input("Enter marks: "))
if (marks>= 90):
    grade = "A"
elif (marks >= 80):
    grade = "B"
elif (marks >= 70):
    grade = "C"
elif (marks >= 60):
    grade = "D"
elif (marks >= 50):
    grade = "E"
elif (marks >= 35):
    grade = "P"
else:
    grade = "F"
print("The grade =",grade)
