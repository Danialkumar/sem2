'''18. Write a program to find factorial of any number using functions.'''
import math
num=int(input("enter the number you want factorial of: "))
def fact(num):print(f"{num}! = ", math.factorial(num))
fact(num)