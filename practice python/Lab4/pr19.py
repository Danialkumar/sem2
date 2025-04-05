#19.Write a program to generate nth Fibonacci term using functions.
def fibonacci(n):
    if n <= 0:
        return "Invalid input. Enter a positive number."
    elif n == 1:return 0
    elif n == 2:return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):a, b = b, a + b
        return b
num = int(input("Enter the value of n: "))
result = fibonacci(num)
print(f"The {num}th Fibonacci term is: {result}")
