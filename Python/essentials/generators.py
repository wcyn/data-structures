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
print([i for i in factors_gen(100)])