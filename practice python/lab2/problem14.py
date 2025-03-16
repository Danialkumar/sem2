digit=0
alpha=0
str=input("enter any string")
for i in str:
  if i.isdigit():
    digit=digit+1
  elif i.isalpha:
    alpha=alpha+1
print("number of letter is: ", alpha)
print("number of digits is: ", digit)