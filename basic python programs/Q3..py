#PYTHON PROGRAM FOR FACTORIAL OF A GIVEN NUMBER RECURSIVE?

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = 5
result = factorial(n)
print("Factorial of", n, "is", result)


# or
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print("Factorial of 5 is", result)
