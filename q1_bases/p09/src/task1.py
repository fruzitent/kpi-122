from string import ascii_letters


def get_number_count(string):
    counter = 0

    for word in string.split():

        for letter in word:
            if not letter.isdigit():
                break
        else:
            counter += 1

    return counter


def get_ascii_words(string):
    result = []

    for word in string.split():

        for letter in word:
            if letter not in ascii_letters:
                break
        else:
            result.append(word)

    return result


def delete_even_words(string):
    result = []

    for index, word in enumerate(string.split()):
        if index % 2 == 0:
            result.append(word)

    return result


if __name__ == "__main__":
    value = str(input("Enter string: "))

    result_A = get_number_count(value)
    result_B = get_ascii_words(value)
    result_C = delete_even_words(value)

    print(result_A, result_B, result_C, sep="\n")
