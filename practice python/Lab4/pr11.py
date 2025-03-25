#11. Write a program to find diameter, circumference and area of circle using functions.
import math
def cic(r):
  print("the diameter of the circle is : ", 2*r)
  print("the circumference of the circle is : ",2*math.pi*r )
  print("the area of the circle is : ",math.pi*r*r )
r=int(input("enter the value of radius: "))
cic(r)