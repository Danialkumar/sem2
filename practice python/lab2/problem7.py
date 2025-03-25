pass_='123'
a=False
while a==False:
  pass_up=input("enter your old password: ")
  if pass_==pass_up:
    pass_new=input("enter new password: ")
    pass_=pass_new
    a= True
  else:
    print("password not verifed")
print("new password is: ", pass_)




