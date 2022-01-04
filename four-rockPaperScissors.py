import random

wins = 0
losses = 0
rock =''' 
    _____
  -' ____)
-'  (_____)
    (_____)
    (____)
--._(__)'''

paper =''' 
    _____
  -' ____)__
-'      _____)
        ______)
       _____)
--.______)'''

scissors =''' 
    _____
  -' ____)___
-'       _____)
        ______)
    (____)
--._(__)'''

listA = [rock, paper, scissors]
userC = int(input("please enter 1 for rock, 2 for paper, or 3 for scissors")) - 1
compC = random.randint(0,2)


print(f"""Player chooses:
{listA[userC]}
""")
print(f"""Computer chooses:
{listA[compC]}
""")

if userC == compC:
    print("Draw!")
elif userC == 0:
    if compC == 1:
        print("Paper covers rock!")
        losses += 1
    else:
        print("Rock breaks scissors!")
        wins += 1
elif userC == 1:
    if compC == 2: 
        print("Scissors cut paper!")
        losses += 1 
    else: 
        print("Paper covers rock")
        wins += 1 
else: 
    if compC == 0: 
        print("Rock breaks scissors!")
        losses += 1 
    else: 
        print("Scissors cut paper!") 
        wins += 1 

print(f"W:{wins}, L:{losses}") 

