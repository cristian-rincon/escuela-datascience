def my_gen():
    a = [i for i in range(1, 201)]

    for i in a:
        if i % 2 == 0:
            yield i


my_first_gen = my_gen()

[print(next(my_first_gen)) for _ in range(100)]
