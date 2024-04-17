def squares_generator(n):
    for i in range(1, n + 1):
        yield i ** 2


# 1-ден n-ға дейінгі сандардың квадраттарын қайта қайтару
for square in squares_generator(5):
    print(square)

