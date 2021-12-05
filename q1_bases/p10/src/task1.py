from functools import reduce


def get_score():
    value = input('enter your points: ')

    arr = [float(i) for i in value.split()]
    sigma = reduce(lambda a, b: a + b, arr)

    if 0 <= sigma <= 100:
        return sigma

    print(f'your score must be in range from 0 to 100, current sum: {sigma}')
    return get_score()


def get_ects(value):
    if 95 <= value <= 100:
        return 'a'

    elif 85 <= value < 95:
        return 'b'

    elif 75 <= value < 85:
        return 'c'

    elif 65 <= value < 75:
        return 'd'

    elif 60 <= value < 64:
        return 'e'

    elif 30 <= value < 60:
        return 'fx'

    else:
        return 'f'


if __name__ == '__main__':
    score = get_score()
    char = get_ects(score)
    print(char)
