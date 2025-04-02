#21. Write a program  to print sqares of all numbers iin the list from 1to 20 using the map and lambda function
numbers=list(range(1,21))
sqares=list(map(lambda x:x**2, numbers))
print(sqares)
