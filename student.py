
# Student Marks Management System
# Updated Version

name = input("Enter student name: ")

mark1 = float(input("Enter marks in Subject 1: "))
mark2 = float(input("Enter marks in Subject 2: "))
mark3 = float(input("Enter marks in Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

# Pass if marks are at least 35 in each subject
if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    result = "PASS"
else:
    result = "FAIL"

print("\n----- Student Mark Details -----")
print("Student Name:", name)
print("Subject 1:", mark1)
print("Subject 2:", mark2)
print("Subject 3:", mark3)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Result:", result)
