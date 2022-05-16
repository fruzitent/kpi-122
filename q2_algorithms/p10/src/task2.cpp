#include <iostream>
#include <random>

#define GET_INPUT(type, name)              \
    type name;                             \
    std::cout << "enter " << #name << ":"; \
    std::cin >> name

int main() {
    constexpr int from         = 1;
    constexpr int to           = 10;
    constexpr int max_attempts = 3;
    bool          is_succeeded = false;

    std::random_device                  seed;
    std::mt19937                        gen(seed());
    const std::uniform_int_distribution dist(from, to);

    for (int i = 0; i < max_attempts; i++) {
        GET_INPUT(int, guess);
        if (dist(gen) == guess) {
            std::cout << "correct answer\n";
            is_succeeded = true;
            break;
        }
        std::cout << "incorrect answer, try again\n";
    }

    if (!is_succeeded) {
        throw std::invalid_argument("ran out of attempts");
    }

    return 0;
}
