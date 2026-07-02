from tkinter import *
import requests

def w():
    try:
        c=e.get()
        u=f"https://wttr.in/{c}?format=3"
        l.config(text=requests.get(u).text)
    except:
        l.config(text="Error")

r=Tk()
r.title("Weather App")

e=Entry(r)
e.pack()

Button(r,text="Get Weather",command=w).pack()

l=Label(r,text="")
l.pack()

r.mainloop()
