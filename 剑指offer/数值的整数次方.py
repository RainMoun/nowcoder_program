def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    result = power(a, n >> 1)
    result *= result
    if n % 2 == 1:
        result *= a
    return result


def my_pow(a, n):
    if a == 0 and n < 0:
        return -1
    n_abs = n if n >= 0 else (0 - n)
    result = power(a, n_abs)
    if n < 0:
        return 1.0/result
    else:
        return result


print(my_pow(3, -5))

