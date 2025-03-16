lst=["num",2,45,67,"float",67,55,"int",80,90]
num=[]
sum=0
for i in range(len(lst)):
  if isinstance(lst[i],int):num.append(lst[i])
for j in range(len(num)):sum=sum+num[j]
print(num,"\n"f"sum of the number is:{sum} & average of the numbers is: ",sum/len(num))
