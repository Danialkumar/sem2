lst=[1,2,4,6,-1,1,-20,-57]
neg_count=0
pos_count=0
for i in range(len(lst)):
  if lst[i]<0:neg_count+=1
  else:pos_count+=1
print(f"number of positive integer is {pos_count} & negative integer is {neg_count} ")



