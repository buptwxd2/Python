"""
函数的嵌套
"""

def factorial(n):
    # check on input
    if not isinstance(n, int):
        raise Exception("input must be an integer")
    if n < 0:
        raise Exception("input must be greater or eqaul to 0")

    def inner_factorial(n):
        if n == 1:
            return 1

        return n * inner_factorial(n-1)

    return inner_factorial(n)

print(factorial(10))
