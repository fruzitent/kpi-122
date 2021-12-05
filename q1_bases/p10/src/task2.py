from random import randint


def get_matrix(a, b, x, y):
    return [[randint(a, b) for j in range(x)] for i in range(y)]


def print_matrix(matrix):
    value = [' '.join(['{:4}'.format(item) for item in row]) for row in matrix]
    print('\n'.join(value))


def main():
    matrix = get_matrix(-1e3, 1e3, 4, 4)
    print_matrix(matrix)

    sigma = 0

    for row_index, row in enumerate(matrix):
        for column_index, column in enumerate(row):
            if column_index < row_index:
                sigma += column

    print(f'sum of elements under main diagonal: {sigma}')


if __name__ == '__main__':
    main()
