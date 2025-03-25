l=[]
n=int(input("number of elements you want in the list: "))
for i in range(n):
  alpha=input("enter your alphabet")
  l.append(alpha)
print(l)
l1=l[0:n//2]
l2=l[n//2: ]
print(f"list after spliting are: {l1} & {l2}")