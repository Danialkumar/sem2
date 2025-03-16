#sum of seires 1+ 2/2! +3/3!+ ......n 

import math
sum=0
n= int(input("enter the number upto which you want sum for "))
for i in range(1, n+1):sum=sum+ i/math.factorial(i)
print("sum of the series is = ",sum)