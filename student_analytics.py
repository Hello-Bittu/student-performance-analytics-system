# Student Performance Analytics System
print("=== Student Performance Analytics Sysytem ===")

name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))
hindi = int(input("Enter Hindi marks: "))
computer = int(input("Enter Computer marks: "))

total = maths + science + english + hindi + computer

percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 70:
    grade = "D"
else:
    grade = "F"

if maths < 33 or science < 33 or english < 33 or hindi < 33 or computer < 33:
    result = "FAIL"
else:
    result = "PASS"

print("\n==== REPORT CARD ===")

print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage,"%")
print("Grade:", grade)
print("Result:",result)

