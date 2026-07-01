import math

# Rectangle Class
class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


r = Rectangle(8, 4)
print("Rectangle")
print("Area =", r.area())
print("Perimeter =", r.perimeter())


# Circle Class
class Circle:
    def __init__(self, r):
        self.radius = r

    def diameter(self):
        return 2 * self.radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius


c = Circle(5)
print("\nCircle")
print("Diameter =", c.diameter())
print("Area =", c.area())
print("Circumference =", c.circumference())


# Product Class
class Product:
    def __init__(self, n, p, q):
        self.name = n
        self.price = p
        self.quantity = q

    def total_value(self):
        return self.price * self.quantity


p = Product("Pen", 20, 15)
print("\nProduct")
print("Name =", p.name)
print("Total Value =", p.total_value())


# Bank Account Class
class BankAccount:
    def __init__(self, bal):
        self.balance = bal

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Withdrawn")
        else:
            print("Not enough balance")


a = BankAccount(1000)
a.deposit(500)
a.withdraw(300)
print("Balance =", a.balance)


# User Class
class User:
    def __init__(self, u, p):
        self.username = u
        self.password = p

    def check_password(self, x):
        if x == self.password:
            return True
        else:
            return False


u = User("student", "abc123")
print("\nUser")
print(u.check_password("abc123"))
print(u.check_password("hello"))





Output--

Rectangle
Area = 32
Perimeter = 24

Circle
Diameter = 10
Area = 78.53981633974483
Circumference = 31.41592653589793

Product
Name = Pen
Total Value = 300
Amount Withdrawn
Balance = 1200

User
True
False
