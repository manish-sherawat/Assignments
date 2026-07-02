f=open("topics.txt","w")
while 1:
    t=input("Topic: ")
    if t=="":
        break
    f.write(t+"\n")
f.close()
print("Done")




import csv

while 1:
    print("1.Add\n2.View\n3.Exit")
    c=input()

    if c=="1":
        d=[input("Name: "),input("Mobile: "),input("Email: ")]
        with open("address.csv","a",newline="") as f:
            csv.writer(f).writerow(d)

    elif c=="2":
        try:
            with open("address.csv") as f:
                for i in csv.reader(f):
                    print(i)
        except:
            print("No contacts")

    else:
        break
