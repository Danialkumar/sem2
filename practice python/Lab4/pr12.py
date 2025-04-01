def max(a,b,c):
  if a>b & b>c:print(f"first number {a} is greatest")
  elif b>a & b>c:print(f"second number {b} is greatest")
  else:print(f"third number {c} is greatest")
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
max(a,b,c)