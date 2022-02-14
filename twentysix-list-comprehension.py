#list comprehensions

list = [1,2,3]
new_list = [item + 1 for item in list] # operation to do FOR item IN list
print(new_list)

# also string comprehension
name = "jacob"
new_list = [operation for letter in name]

#
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers = [num**2 for num in numbers])
#
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num%2==0]
print(result)
#
with open("file1.txt") as fOne:
    contents1 = fOne.readlines()
with open("file2.txt") as fTwo:
    contents2 = fTwo.readlines()
result = [int(num) for num in contents1 if num in contents2]


print(result)


