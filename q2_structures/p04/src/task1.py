INPUT_PATH = "../assets/input.txt"
OUTPUT_PATH = "../assets/output.txt"
VOWELS = "aAeEiIoOuU"


def is_more_vowels(string: str) -> bool:
    counter: int = sum(letter in VOWELS for letter in string)
    return counter > len(string) - counter


def main() -> None:
    with open(INPUT_PATH, "r") as file_input:
        words: list[str] = file_input.read().split(" ")

    with open(OUTPUT_PATH, "w") as file_output:
        text: str = " ".join([word for word in words if is_more_vowels(word)])
        file_output.write(text)
        print(text)


if __name__ == "__main__":
    main()
