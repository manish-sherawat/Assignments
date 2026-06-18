# Python Assignment

# 1) Repeat a tuple three times using * operator
t = (1, 2, 3)
result = t * 3
print("Repeated Tuple:", result)

# 2) Join three tuples using + operator
t1 = (1, 2)
t2 = (3, 4)
t3 = (5, 6)

new_tuple = t1 + t2 + t3
print("Joined Tuple:", new_tuple)

# 3) Check whether an element exists in a tuple
t = (10, 20, 30, 40)
element = 30

if element in t:
    print(element, "exists in the tuple")
else:
    print(element, "does not exist in the tuple")

# 4) Find total, highest and lowest value without sum(), max(), min()
nums = (12, 45, 7, 89, 23)

total = 0
highest = nums[0]
lowest = nums[0]

for n in nums:
    total += n

    if n > highest:
        highest = n

    if n < lowest:
        lowest = n

print("Total =", total)
print("Highest =", highest)
print("Lowest =", lowest)

# 5) Filter tuple values greater than 10
n = (3, 14, 7, 22, 9, 41, 18, 5)

filtered = ()

for i in n:
    if i > 10:
        filtered += (i,)

print("Filtered Tuple:", filtered)

# 6) Count elements in a set without len()
s = {"cat", "dog", "bird", "fish"}

count = 0

for item in s:
    count += 1

print("Number of elements:", count)

# 7) Combine two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

combined = set1 | set2
print("Combined Set:", combined)

# 8) Find common elements in two sets
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

common = s1 & s2
print("Common Elements:", common)

# 9) Find elements in either set but not both
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

result = s1 ^ s2
print("Elements in either set but not both:", result)



Output ---

Repeated Tuple: (1, 2, 3, 1, 2, 3, 1, 2, 3)
Joined Tuple: (1, 2, 3, 4, 5, 6)
30 exists in the tuple
Total = 176
Highest = 89
Lowest = 7
Filtered Tuple: (14, 22, 41, 18)
Number of elements: 4
Combined Set: {1, 2, 3, 4, 5}
Common Elements: {3, 4}
Elements in either set but not both: {1, 2, 5, 6}
