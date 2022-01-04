
import random	 

def fiftyFifty():
    test_seed = int(input("Create a seed number: "))
    random.seed(test_seed)
    if random.randint(0,1) == 0:
        print('Tails')
    else: 
        print('Heads')

def randoFromList():
    test_seed = int(input("Create a seed number: "))
    random.seed(test_seed)
    names_string = input("List data, separated by a comma. ")
    names = names_string.split(", ")
    index = random.randint(0, len(names)-1)
    print(f"This: {names[index]} has been selected.")

def targetMatriceXY():
    row1 = ["⬜️","⬜️","⬜️"]
    row2 = ["⬜️","⬜️","⬜️"]
    row3 = ["⬜️","⬜️","⬜️"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Matrix coordinates 'YX' format")
    x = int(position[0]) -1
    y = int(position[1]) -1
    map[y][x] = 'X'
    print(f"{row1}\n{row2}\n{row3}")
