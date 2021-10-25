def func():
    def get_input(prompt):
        return int(input(prompt))

    a = get_input('a: ')
    b = get_input('b: ')

    if a > b:
        return func()

    sigma = 0

    while a <= b:
        if a > 0:
            sigma += a

        a += 1

    return sigma


print(
    func()
)
