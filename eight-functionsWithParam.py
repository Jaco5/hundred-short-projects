# calculate area and divide by portion, then round up.
import math
def paint_calc(height, width, cover):
    cans = math.ceil(height * width / coverage)
    print(f"You'll need {cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


#Prime checker

def prime_checker(number):
    if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        print("It's a prime number.")
    else: 
        print("It's not a prime number.")



n = int(input("Check this number: "))
prime_checker(number=n)

