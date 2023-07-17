#Lauren Looney CIS261  Recursive-and-Iterative-Factorials


def factorial_recursive(n):
    if n <= 1:
        #base case
        return 1 
    else:
        #recursive case
        return n * factorial_recursive(n-1)



print(factorial_recursive(5))
print(factorial_recursive(6))
print(factorial_recursive(7))
print(factorial_recursive(8))
print(factorial_recursive(9))

 

def factorial_iterative(n):
        result = 1
        for i in range(n):
            result *= i + 1
        return result
print(factorial_iterative(5))
print(factorial_iterative(6))
print(factorial_iterative(7))
print(factorial_iterative(8))
print(factorial_iterative(9))
