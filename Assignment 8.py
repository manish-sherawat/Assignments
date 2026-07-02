from tkinter import *
import csv

def save():
    with open("address.csv","a",newline="") as f:
        csv.writer(f).writerow([n.get(),e.get(),m.get()])
    print("Saved")

r=Tk()

Label(r,text="Name").grid(row=0,column=0)
Label(r,text="Email").grid(row=1,column=0)
Label(r,text="Mobile").grid(row=2,column=0)

n=Entry(r)
e=Entry(r)
m=Entry(r)

n.grid(row=0,column=1)
e.grid(row=1,column=1)
m.grid(row=2,column=1)

Button(r,text="Save",command=save).grid(row=3,column=1)

r.mainloop()
