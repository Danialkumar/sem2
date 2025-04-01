# f(x)= ax**2+bx+c
#let f(x)=5x**2+6*x-8 , d=-2
x=int(input("enter the value of x"))
if x!=-2:
  val=5*x**2+6*x-8
  print(f"value of f(x) at x={x} is ", val)
else:
  print(f"value of f(x) at x={x} is ", 0)