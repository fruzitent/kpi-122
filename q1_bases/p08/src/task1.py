from random import randint


def get_input(prompt):
    return int(input(prompt))


def print_matrix(matrix):
    arr = [''.join(['{:4}'.format(item) for item in row]) for row in matrix]
    print('\n'.join(arr))


def main():
    n = get_input('n: ')
    m = get_input('m: ')
    a = get_input('a: ')
    b = get_input('b: ')

    print('\n')

    matrix = [[randint(a, b) for _ in range(m)] for _ in range(n)]
    print_matrix(matrix)

    print('\n')

    result = [sum(row) for row in matrix]

    print(result)


if __name__ == '__main__':
    main()
