from functools import cache


@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


if __name__ == '__main__':
    print(factorial(100))
