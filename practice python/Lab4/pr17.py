'''17. Write a program to check whether a number is
 palindrome or not using functions.'''
word=input("enter the word you want to check palindrome of: ")
def pallindrome(word):
  if word==word[::-1]:print(f"{word} is pallindrome.")
  else:print(f"{word} is not a pallindrome.")
pallindrome(word)
