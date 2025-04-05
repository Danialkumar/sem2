#13. Write a program to check whether a number is even or odd using functions.
def odd_even(num):
  if num%2==0:print(f"{num}is enen")
  else:print(f"{num} is odd")
num=int(input("enter any number: "))
odd_even(num)
