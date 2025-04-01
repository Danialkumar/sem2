n=int (input ("enter a number "))
if n>2:
  for i in range(2, int(n**0.5) +1):
    if n%i==0:print("given number is not prime")
    else:print("given number is prime")
else:print("number is neither prime nor composite")