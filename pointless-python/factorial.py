def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return n*factorial(n-1)

def test_factorial(n: int, expected: int):
    result = factorial(n)
    print(f"Calculating the Factorial of {str(n)}")
    print(f"Expected = {expected}")
    print(f"Result = {result}")
    print(f"The Same = {expected == result}")

#Factorial of 20:
test_factorial(20, 2_432_902_008_176_640_000)