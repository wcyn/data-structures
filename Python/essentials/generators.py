import math
# A function to return factors of a given number
def factors(num):
    results = []
    for i in range(1, num + 1):
        if num % i == 0:
            results.append(i)
    return results

print(factors(100))

# A function to return a generator for factors of a given number
def factors_gen(num):
    for i in range(1, num + 1):
        if num % i == 0:
            yield i

print(factors_gen(100))
print("Factors gen: ", [i for i in factors_gen(100)])

# Efficient gen with multiple yields
def efficient_factors_gen(num):
    k = 1
    while k * k < num:
        if num % k == 0:
            yield k
            yield num // k  # Yield its partener multiple as well
        k += 1
    if k * k == num:
        yield k

print(factors_gen(100))
print("Efficient factors gen: ", [i for i in efficient_factors_gen(100)])

# A fibonacci series generator
def fibonacci_series(num):
    previous_num = 0
    current_num = 1
    pos = 0
    while num > pos:
        yield previous_num
        prev_and_curr =  previous_num + current_num
        previous_num = current_num
        current_num = prev_and_curr
        pos += 1

print("Fibonacci Series: ", [i for i in fibonacci_series(10)])