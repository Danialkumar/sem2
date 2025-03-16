num=[]
num_div=[]
for i in range(51):num.append(i)
for k in range(len(num)):
  if num[k]%3==0:num_div.append(num[k])
print("number divsible by 3 are: ", num_div)
