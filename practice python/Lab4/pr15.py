'''15. Write a program to find power of any number using functions.'''
def power(num, pow):return print(f"{num}**{pow} = ", num**pow)
num=int(input("enter the number: "))
pow=int(input("enter the power: "))
power(num, pow)