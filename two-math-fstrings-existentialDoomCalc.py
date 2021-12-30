def bmiCalc():
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    print(round(float(weight) / (float(height)**2)))

def existentialCrisisCalc():
    timeLeft = 90 - int(age) 
    day = str(int(timeLeft) * 365)
    week = str(int(timeLeft) * 52)
    month = str(int(timeLeft) * 12)
    print(f"You have {day} days, {week} weeks, and {month} months left to live.")

def billShareCalc():
    print("Please use decimal numbers for all inputs. Failure to do so will lead to immediate termination of employment.")
    bill = float(input("what is the bill amount?"))
    tip = 1 + float(input("What percent tip?"))/100
    print(tip)
    split = float(input("How many people will split the bill?"))
    share = round(bill * tip / split, 2)
    print(f"An even share of this bill including tip is ${share}.")
