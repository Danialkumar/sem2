#14. Write a program to check whether a number is prime, Armstrong using functions.
num=int(input("enter the number to check prime or not: "))
def prime(num):
  if num>2:
    for i in range(2,int(num**0.5)+1):
      if num %i==0:print(f"{num} is not prime")
      else:print(f"{num} is prime")
  else:print(f"{num} is neither prime nor composite: ")
prime(num)
