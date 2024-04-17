def apply_callback(callback, lst):
    return list(map(callback, lst))


def mult(x):
    return x * 2


numbers = [1, 2, 3, 4, 5]

result = apply_callback(mult, numbers)
print(result)
