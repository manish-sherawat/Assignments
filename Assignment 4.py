# 1) List operations

numbers = [12, 45, 67, 23, 89, 34, 56, 78, 90, 11, 22, 33, 44, 55, 66]

# Total sum
total_sum = sum(numbers)

# Arithmetic mean (average)
average = total_sum / len(numbers)

# Largest and smallest values
largest = max(numbers)
smallest = min(numbers)

# Count even and odd numbers
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("List:", numbers)
print("Total Sum =", total_sum)
print("Average =", average)
print("Largest Number =", largest)
print("Smallest Number =", smallest)
print("Even Numbers Count =", even_count)
print("Odd Numbers Count =", odd_count)


# 2) Access number 5 from a list of lists

data = [10, 11, 102, [1, 2], [3, 4, 5], [6, 7]]

print("\nNumber 5 =", data[4][2])


# 3) Check if a value exists in a list

inventory = ["Laptop", "Mouse", "Monitor", "Keyboard"]
target = "Tablet"

if target in inventory:
    print(f"\n{target} is available in inventory.")
else:
    print(f"\n{target} is NOT available in inventory.")


# 4) Delete every instance of a specific value from a list

my_list = [5, 20, 15, 20, 25, 50, 20]
item_to_remove = 20

new_list = [item for item in my_list if item != item_to_remove]

print("\nOriginal List:", my_list)
print("Updated List:", new_list)


# 5) Create a dictionary from two lists

keys = ["name", "age", "city"]
values = ["ABC", 25, "Jaipur"]

my_dict = dict(zip(keys, values))

print("\nDictionary:", my_dict)


# 6) Retrieve a value from a nested dictionary

person = {
    "name": "ABC",
    "address": {
        "city": "Jaipur",
        "state": "Rajasthan"
    }
}




Output - -

List: [12, 45, 67, 23, 89, 34, 56, 78, 90, 11, 22, 33, 44, 55, 66]
Total Sum = 725
Average = 48.333333333333336
Largest Number = 90
Smallest Number = 11
Even Numbers Count = 8
Odd Numbers Count = 7

Number 5 = 5

Tablet is NOT available in inventory.

Original List: [5, 20, 15, 20, 25, 50, 20]
Updated List: [5, 15, 25, 50]

Dictionary: {'name': 'ABC', 'age': 25, 'city': 'Jaipur'}

City = Jaipur
city = person["address"]["city"]

print("\nCity =", city)
