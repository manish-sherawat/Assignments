# 1. Maximum of three numbers
def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Maximum:", maximum(10, 25, 15))


# 2. Distinct elements from a list
def distinct_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

print("Distinct List:", distinct_list([1, 2, 2, 3, 4, 4, 5]))


# 3. Multiply all numbers in a list
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

print("Product:", multiply_list([2, 3, 4, 5]))


# 4. Factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("Factorial:", factorial(5))


# 5. Reverse a string
def reverse_string(text):
    return text[::-1]

print("Reversed String:", reverse_string("Python"))


# 6. Check whether a number falls within range 10 and 50
def check_range(num):
    if 10 <= num <= 50:
        print("Number is within range.")
    else:
        print("Number is outside the range.")

check_range(35)


# 7. Print even numbers from a list
def print_even(lst):
    print("Even Numbers:")
    for num in lst:
        if num % 2 == 0:
            print(num)

print_even([1, 2, 3, 4, 5, 6, 7, 8])


# 8. Check whether a number is prime
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print("Is Prime:", is_prime(13))


# 9. Count upper and lower case letters
def count_case(text):
    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    print("Uppercase Letters:", upper)
    print("Lowercase Letters:", lower)

count_case("Hello Python")


Output ---


Maximum: 25
Distinct List: [1, 2, 3, 4, 5]
Product: 120
Factorial: 120
Reversed String: nohtyP
Number is within range.
Even Numbers:
2
4
6
8
Is Prime: True
Uppercase Letters: 2
Lowercase Letters: 9
