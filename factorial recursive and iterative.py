#Lauren Looney CIS261  Recursive-and-Iterative-Factorials


def factorial_recursive(n):
    if n <= 1:
        #base case
        return 1 
    else:
        #recursive case
        return n * factorial_recursive(n-1)

print("Factorial results using recursive function ")


print(factorial_recursive(0))
print(factorial_recursive(5))
print(factorial_recursive(10))
print(factorial_recursive(25))
print(factorial_recursive(50))
print(factorial_recursive(100))


print("Factorial results using iterative function ")

def factorial_iterative(n):
        result = 1
        for i in range(n):
            result *= i + 1
        return result
print(factorial_iterative(0))
print(factorial_iterative(5))
print(factorial_iterative(10))
print(factorial_iterative(25))
print(factorial_iterative(50))
print(factorial_iterative(100))
