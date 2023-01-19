#include <cstring>
#include <iostream>

void filter(char* string, bool (*predicate)(char)) {
    char* original = string;

    while (*original != '\0') {
        if (predicate(*original)) {
            *string = *original;
            ++string;
        }
        ++original;
    }

    *string = '\0';
}

bool is_alpha(char symbol) {
    return std::isalpha(symbol) != 0;
}

void parse(char* string, char** buffer, std::size_t* capacity, std::size_t size) {
    char* token = nullptr;
    char* rest  = string;

    while ((token = strtok_r(rest, " ", &rest)) != nullptr) {
        filter(token, is_alpha);
        if (std::strlen(token) % 2 == 0) {
            if (*capacity == size) {
                throw std::overflow_error("Buffer overflow\n");
            }
            buffer[(*capacity)++] = token;
        }
    }
}

int main(int argc, char** argv) try {
    if (argc < 2) {
        throw std::invalid_argument("Not enough arguments\n");
    }

    std::size_t capacity = 0;
    std::size_t size     = 256;
    char**      buffer   = new char*[size];

    parse(argv[1], buffer, &capacity, size);

    for (std::size_t i = 0; i < capacity; ++i) {
        std::cout << buffer[i] << " ";
    }

    delete[] buffer;
    return 0;
} catch (const std::exception& error) {
    std::cerr << "ERROR: " << error.what();
    return 1;
}
