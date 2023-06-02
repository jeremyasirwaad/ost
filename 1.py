vov = ['a','e','i','o','u']

data = "helloo"

value = 0

for i in data:
    if(i in vov):
        value = value + 1


def deltobin(deci):
    num = deci
    value = ""
    while num >= 1:
        rem = num % 2
        value = value + str(rem)
        num = num // 2

    print(value)



def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_n_primes(n):
    count = 0
    number = 2
    while count < n:
        if is_prime(number):
            print(number, end=" ")
            count += 1
        number += 1

print_n_primes(10)
        

from itertools import permutations

num = ["10", "20", "30"]

print(list(permutations(num)))


# import mysql.connector

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="students"
# )

# class lessage(Exception):
#     pass

# class overage(Exception):
#     pass

# def checage(age):
#     if(age < 10):
#         raise lessage();
#     elif(age > 99):
#         raise overage()
#     else:
#         print("oaky")

# try:
#     checage(100)
# except lessage:
#     print("Less age")
# except overage:
#     print("over ag

# from tkinter import *

# app = Tk()
# app.title("Jeremy's Ex1")
# app.geometry("300x400")
# a = Label(app,text="Hello World")
# btn = Button(app,text="Click to close", command=app.destroy)

# menubar = Menu(app)

# file = Menu(menubar, tearoff=0)
# file.add_cascade(label="Files",command= None)
# file.add_command(label="Edit",command= None)
# file.add_command(label="Clear",command= None)
# file.add_command(label="Exit",command= None)


# btn.pack()
# a.pack()
# app.config(menu=menubar)
# app.mainloop()

# importing only those functions
# which are needed
from tkinter import *

# creating tkinter window
root = Tk()

# Creating Menubar
menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# display Menu
root.config(menu = menubar)
mainloop()


