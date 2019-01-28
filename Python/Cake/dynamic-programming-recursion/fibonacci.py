# https://www.interviewcake.com/question/python/nth-fibonacci?course=fc1&section=dynamic-programming-recursion
# Write a function fib() that takes an integer nn and returns the nth Fibonacci ↴ number.


def fib(n, memo):
    if n < 2:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n - 1, memo) +  fib(n - 2, memo)

    return memo[n]


print(fib(4, {}))


def fib_bottom_up(num):
    if num < 2:
        return num

    num_sum = 0
    for n in range(2, num):
        num_sum = (n-1) + (n-2)

    return num_sum


print(fib_bottom_up(4))

