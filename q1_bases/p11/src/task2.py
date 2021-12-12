INPUT_PATH: str = '../assets/task2_input.txt'
OUTPUT_PATH: str = '../assets/task2_output.txt'

def main():
    vowels = 'aeiou'

    def capitalize_consonants(char):
        if char.lower() not in vowels and char.islower():
            return char.capitalize()

        return char

    with open(INPUT_PATH, 'r') as f:
        file1 = f.read().split('\n')

        for l_index, line in enumerate(file1[::2]):
            new_line = [''.join(capitalize_consonants(char)) for char in line]
            file1[l_index * 2] = ''.join(new_line)

    with open(OUTPUT_PATH, 'w') as f:
        f.write('\n'.join(file1))


if __name__ == '__main__':
    main()
