def live(x, y):
    return x + y
print(live(2, 3))

def is_even(n):
    return n % 2 == 0
print(is_even(4))
print(is_even(5))

def max_of_three(a, b, c):
    return max(a, b, c)
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m
print(max_of_three(10, 20, 15))
print(max_of_three(70, 210, 15))


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res
print(factorial(5))


def calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: Division by zero"
        return a / b
print(calc(10, 5, '+'))
print(calc(10, 5, '-'))
print(calc(10, 5, '*'))
print(calc(10, 5, '/'))
