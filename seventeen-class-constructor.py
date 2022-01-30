import random
import tkinter.messagebox
from tkinter import *

def name_gen():
    return "bobo"

def num(limit):
    return random.randint(1,limit)

group = []

class Entity:
    def __init__(self):
        self.name = name_gen()
        self.number = num(100)
        self.vector = [10,15]
        self.location = [num(1000), num(1000)]
        print(f"{self.number} {self.name} {self.location}")

def create_group(size):
    global group
    for each in range(size):
        print(f"initialized {each}")
        each = Entity()
        group.append(each)
    #print(f"group {group}")
create_group(10)
#Tk(screenName=None, baseName=None, className='Tk', usTk=1)

window = tkinter.Tk()
window.title("Window Title")
canvas = tkinter.Canvas(window, width=1000, height=1000)

for each in group:
    canvas.create_oval(each.location[0], each.location[1], each.location[0]+each.number, each.location[1]+each.number, fill='green')

for each in group:
    each.location[0] = each.location[0] + each.vector[0]
    each.location[1] = each.location[1] + each.vector[1] 

    canvas.pack()
    window.mainloop()
