# swap values between two variables.
import random


def variableSwap():
    a = input("a: ")
    b = input("b: ")
    swap = a
    a = b
    b = swap
    print("a: " + a)
    print("b: " + b)


# Create a password based on a mnemonic word or phrase
def passGen():
    mnemonic = input("What word do you want to use?")
    passArr = []
    passStr = ''
    for i in mnemonic:
        passArr.append(i)
        passArr.append(str(random.randrange(0,100)))
    for j in range(len(passArr)):
        passStr += passArr[j]
    print(passStr)
