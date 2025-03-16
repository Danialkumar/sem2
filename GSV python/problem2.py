#taking length of tri, square , and rect and give area

#square
a=int(input("enter the value of the side of the square"))
print("area of the square = ",a*a)
print("perimeter of the square is ", 4*a)

#traiangle
print("which type of triangle you want to calculate your area for ")
beta =int(input("enter the value of the first  side of the scalene triangle"))
gama=int(input("enter the value of the second side of the scalene triangle"))
delta=int(input("enter the value of the third side of the scalene triangle"))
s=1/2*(beta +gama +delta )
area=(s(s-delta)(s-beta )(s-gama))**1/2
perimeter=delta +beta +gama
print("area of the scalene triangle is = ", area )
print("perimeter of the scalene triangle is = ",perimeter )


    



c=int(input("enter the value of the length of the rectangle"))
d=int(input("enter the value of the width of the rectangle"))

print("area of the rectangle= ",c*d)
print("perimeter of the rectangle= ",2(c+d))


