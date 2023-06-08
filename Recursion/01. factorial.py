"""
    Understanding what recursion is through a factorial function
"""

def factorial(num: int) -> int:
    if num == 1:
        return 1
    return num * factorial(num - 1)


print(factorial(4))