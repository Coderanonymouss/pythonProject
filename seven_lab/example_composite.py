def g(x):
    return x * 2


def f(x):
    return x + 1


def composite_function(x):
    return f(g(x))


result = composite_function(3)
print(result)
