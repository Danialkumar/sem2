'''6. Write a program to delete 3rd character of the string "Hello World". Also delete 2nd
last character of the same string.'''
string="hello world"
print(string.replace(string(2)," "))
print(string.replace(string(-2)," "))

print("updated string is :", string)