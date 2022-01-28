import random

def encryption(text, seed, mode):
    encryptedStr = ""
    switch = True
    seedA = int(seed[0])
    seedB = int(seed[1])
    offset = -26
    if mode == 'd':
        seedA = -seedA
        seedB = -seedB
        offset = -offset
    for ch in text:
        if ch.isalpha():
            if switch:
                new_ch = ord(ch) + seedA
                switch = False
            else:
                new_ch = ord(ch) + seedB
                switch = True
            if new_ch > ord('z') or new_ch < ord('a'):
                new_ch += offset
            ch = chr(new_ch)
        encryptedStr += ch
    print(encryptedStr)
    init()

def init():
    text = input("Message text: ")
    if len(text) == 0: init()
    seed = input("Enter double digit seed: ")
    if len(seed) != 2: seed = str(random.randint(10,99)); print("Invalid seed. " + str(seed) + " used instead.")
    mode = input("""Options:
'e' - encrypt mode
'd' - decrypt mode

>""")
    if mode != 'e' and mode != 'd': print("Must enter a mode. Resetting."); init()
    else: encryption(text, seed, mode)

init()
