# https://www.interviewcake.com/question/python/nth-fibonacci?course=fc1&section=dynamic-programming-recursion
# Write a function fib() that takes an integer nn and returns the nth Fibonacci ↴ number.
import unittest

def fib(n, memo):
    if n < 2:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n - 1, memo) +  fib(n - 2, memo)

    return memo[n]


print(fib(4, {}))


# def fib_bottom_up_incorrect(num):
#     if num < 2:
#         return num

#     num_sum = 0
#     for n in range(2, num):
#         num_sum = (n-1) + (n-2)

#     return num_sum

# Compute the nth Fibonacci number
def fib_bottom_up(num):
    # Edge cases:
    if n < 0:
        raise ValueError('Index was negative. No such thing as a '
                         'negative index in a series.')
    elif n in [0, 1]:
        return n

    # We'll be building the fibonacci series from the bottom up
    # so we'll need to track the previous 2 numbers at each step
    prev_prev = 0  # 0th fibonacci
    prev = 1       # 1st fibonacci

    for _ in xrange(n - 1):
        # Iteration 1: current = 2nd fibonacci
        # Iteration 2: current = 3rd fibonacci
        # Iteration 3: current = 4th fibonacci
        # To get nth fibonacci ... do n-1 iterations.
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return current

print(fib_bottom_up(4))

# Bonus
# If you're good with matrix multiplication you can bring the time cost
# down even further, to O(lg(n))O(lg(n)). Can you figure out how?

# Tests

class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2)