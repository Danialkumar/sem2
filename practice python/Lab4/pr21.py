'''21. Write a program to print the squares of all numbers in the list from 1 to 20 using the
`map` and `lambda` functions.'''
numbers = list(range(1, 21))
squares = list(map(lambda x: x**2, numbers))
print("Squares of numbers from 1 to 20:")
print(squares)
