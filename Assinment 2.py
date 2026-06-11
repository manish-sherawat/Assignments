## Student Result Program

name = input("Enter student name: ")
cls = input("Enter class: ")
                                                                                          
m1 = int(input("Enter marks of subject 1: "))                                                                
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\nResult")
print("Name:", name)
print("Class:", cls)
print("Total Marks:", total)
print("Percentage:", percentage, "%")


Output ----

Result
Name: Manish
Class: 12th
Total Marks: 402
Percentage: 80.4 %

---------------------------------------------------------------------------------------------------------

## String Concatenation and Methods Program

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s3 = s1 + s2

print("Concatenated String:", s3)

print("lower():", s3.lower())
print("upper():", s3.upper())
print("title():", s3.title())
print("swapcase():", s3.swapcase())
print("capitalize():", s3.capitalize())
print("casefold():", s3.casefold())
print("center():", s3.center(30))
print("count('a'):", s3.count('a'))
print("endswith('a'):", s3.endswith('a'))
print("find('a'):", s3.find('a'))
print("isalnum():", s3.isalnum())
print("isdigit():", s3.isdigit())
print("isnumeric():", s3.isnumeric())
print("isspace():", s3.isspace())
print("replace():", s3.replace('a', '@'))


Output ---

Concatenated String: 5575
lower(): 5575
upper(): 5575
title(): 5575
swapcase(): 5575
capitalize(): 5575
casefold(): 5575
center():              5575             
count('a'): 0
endswith('a'): False
find('a'): -1
isalnum(): True
isdigit(): True
isnumeric(): True
isspace(): False
replace(): 5575


--------------------------------------------------------------------------------------------------------------


## Assignment Operators Program

a = 10

print("Initial value:", a)

a += 5
print("After += :", a)

a -= 2
print("After -= :", a)

a *= 3
print("After *= :", a)

a /= 2
print("After /= :", a)

a %= 4
print("After %= :", a)

a **= 2
print("After **= :", a)

a //= 2
print("After //= :", a)


Output  ---

Initial value: 10
After += : 15
After -= : 13
After *= : 39
After /= : 19.5
After %= : 3.5
After **= : 12.25
After //= : 6.0

