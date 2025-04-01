#to calculate roots of quadratic equation
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
c=int(input("enter the value of c: "))

print(f"Quadratic equation is {a}*x**2+{b}x+{c}")
D=b**2-4*a*c
if D>0:
  print("roots are real")
  print("first root is ")