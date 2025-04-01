'''
9. Write a code to take a sentence as input, then:
1. Convert it to uppercase using .upper().
2. Find the total number of characters using len().
3. Replace all occurrences of the word "Python" with "Programming" using .replace().'''

str_1=input("enter any string: ")
print("upper string is: ",str_1.upper())
print("length of the string is: ", len(str_1))
print("updated string is: ",str_1.replace("python", "programming"))