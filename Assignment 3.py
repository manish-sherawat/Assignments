## Student Result with Grade Using Conditional Statements

name = input("Enter student name: ")
cls = input("Enter class: ")

m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

if percentage >= 60:
    grade = "A"
elif percentage >= 50:
    grade = "B"
elif percentage >= 40:
    grade = "C"
elif percentage >= 33:
    grade = "D"
else:
    grade = "Fail"

print("\nResult")
print("Name:", name)
print("Class:", cls)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)


Output---

Result
Name: Manish Sherawat
Class: 12th
Total Marks: 168
Percentage: 33.6 %
Grade: D


-----------------------------------------------------------------------------------------------------------------------

## Multiplication Table (Number Between 2 and 50)


num = int(input("Enter a number between 2 and 50: "))

if num < 2 or num > 50:
    print("Please enter a number between 2 and 50.")
else:
    print("\nTable of", num)

    for i in range(1, 11):
        print(num, "x", i, "=", num * i)


Output ---

Table of 39
39 x 1 = 39
39 x 2 = 78
39 x 3 = 117
39 x 4 = 156
39 x 5 = 195
39 x 6 = 234
39 x 7 = 273
39 x 8 = 312
39 x 9 = 351
39 x 10 = 390

--------------------------------------------------------------------------------------------------------------------------
## Palindrome Number Program

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse Number:", reverse)

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


Output ---

Reverse Number: 321
Not a Palindrome Number



