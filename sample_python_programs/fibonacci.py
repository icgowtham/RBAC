def fib(n):
    """
    Calculates the n-th Fibonacci number iteratively
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
