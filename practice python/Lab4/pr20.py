'''20. Write a program to print numbers divisible by 11 between 200 and 500 using the `filter`
and `lambda` functions.'''
divisible_by_11 = list(filter(lambda x: x % 11 == 0, range(200, 501)))
print("Numbers divisible by 11 between 200 and 500:")
print(divisible_by_11)
