

# mean of total of list (rounded)
numbers = input("Input a list of numbers ").split()
for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])

total = 0
counter = 0

for h in student_heights:
    total += h
    counter += 1

average = total/counter 
print(round(average)) 


# Highest int in list
numbers = input("Input a list of student scores ").split()
for n in range(0, len(numbers)):
  numbers[n] = int(numbers[n])
print(numbers)

for i in range(len(numbers)):
    if numbers[i-1] > numbers[i]:
        swap = numbers[i-1]
        numbers[i-1] = numbers[i]
        numbers[i] = swap
print(f"The highest score in the class is: {numbers[-1]}")


# Add all the even numbers between 0 and 100.
# "There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions."
# (no range function)
count = 0
total = 0
def recur():
    global count, total
    count += 1
    if count % 2 == 0:
        total += count
    if count == 100:
        return
    recur()
recur()
print(total)

# fizzbuzz
i = 1
while i <= 100:
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
    i += 1


