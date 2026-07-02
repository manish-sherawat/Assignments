def kap(n):
    while n!="6174":
        a="".join(sorted(n))
        d=a[::-1]
        n=str(int(d)-int(a)).zfill(4)
        print(d,"-",a,"=",n)

kap(input("Enter 4-digit number: "))
