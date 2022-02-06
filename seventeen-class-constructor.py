import random
import tkinter
import time



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
def create_window():
    window = tkinter.Tk()
    window.title("Window Title")
    window.geometry(f'1000x1000')
    return window

def create_canvas(window):
    canvas = tkinter.Canvas(window, width=1000, height=1000)
    canvas.pack(fill="both", expand=True)
    return canvas

def animation(window, canvas, group):
    for each in group:
        ball = canvas.create_oval(each.location[0], each.location[1], each.location[0]+each.number, each.location[1]+each.number, fill='green', outline= "Green", width=each.number)
        print(each)
    while True:
        window.update()
        time.sleep(.1)
    

animwindow = create_window()
animcanvas = create_canvas(animwindow)
animation(animwindow,animcanvas,group)
