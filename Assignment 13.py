class Temperature:
    def __init__(self,c):
        self.c=c

    def to_fahrenheit(self):
        return self.c*9/5+32

    def to_kelvin(self):
        return self.c+273.15

t=Temperature(float(input("Celsius: ")))
print(t.to_fahrenheit())
print(t.to_kelvin())

###################################
class Interest:
    def __init__(self,p,r,t):
        self.p,self.r,self.t=p,r,t

    def si(self):
        return self.p*self.r*self.t/100

    def ci(self):
        return self.p*(1+self.r/100)**self.t-self.p

i=Interest(10000,5,2)
print(i.si())
print(i.ci())

######################################

class CoffeeMachine:
    def __init__(self,w,c,m):
        self.w,self.c,self.m=w,c,m

    def make_latte(self):
        if self.w>=200 and self.c>=20 and self.m>=150:
            self.w-=200
            self.c-=20
            self.m-=150
            print("Latte Ready")
        else:
            print("Not enough resources")

x=CoffeeMachine(300,100,200)
x.make_latte()


######################################

class Vehicle:
    def __init__(self,n,s):
        self.n=n
        self.s=s

    def display(self):
        print(self.n,self.s)

class Bus(Vehicle):
    def __init__(self,n,s,c):
        super().__init__(n,s)
        self.c=c

    def reservation(self):
        print("Seats:",self.c)

b=Bus("Volvo",120,40)
b.display()
b.reservation()
