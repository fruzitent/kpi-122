#include <sys/stat.h>

#include <iostream>
#include <random>

namespace aids {
    template<typename Iterator, typename Generator>
    static constexpr void generate(Iterator first, Iterator last, Generator gen) {
        for (; first != last; ++first) {
            *first = gen();
        }
    }
}  // namespace aids

template<typename T>
std::size_t get_index_of(const T* array, std::size_t size, T value) {
    for (std::size_t i = 0; i < size; ++i) {
        if (array[i] == value) {
            return i;
        }
    }
    throw std::runtime_error("Value not found\n");
}

static constexpr void print(const auto* array, std::size_t size) {
    for (std::size_t i = 0; i < size; ++i) {
        std::cout << array[i] << " ";
    }
    std::cout << "\n";
}

template<typename T>
std::size_t remove(T* array, std::size_t size, std::size_t index) {
    if (index < 0 && index >= size) {
        throw std::runtime_error("Index out of bounds\n");
    }

    --size;
    for (std::size_t i = index; i < size; i++) {
        array[i] = array[i + 1];
    }

    return size;
}

int main() try {
    static constexpr int rng_min = 0;
    static constexpr int rng_max = 10;

    std::random_device                 seed;
    std::mt19937                       gen(seed());
    std::uniform_int_distribution<int> dist(rng_min, rng_max);

    const auto rng = [&dist, &gen]() {
        return dist(gen);
    };

    static constexpr std::size_t array_size = 10;

    auto* array = new int[array_size];
    aids::generate(array, array + array_size, rng);
    print(array, array_size);

    std::FILE* file1 = std::tmpfile();
    if (std::fwrite(array, sizeof(int), array_size, file1) < array_size) {
        throw std::runtime_error("Could not write to file\n");
    }
    std::rewind(file1);
    delete[] array;

    static struct stat stat {};

    fstat(fileno(file1), &stat);
    static const auto file_size   = static_cast<std::size_t>(stat.st_size);
    static auto       buffer_size = file_size / sizeof(int);

    auto* buffer = new int[buffer_size];
    if (std::fread(buffer, sizeof(int), buffer_size, file1) < buffer_size) {
        throw std::runtime_error("Could not read from file\n");
    }

    // TODO: use smart pointers to avoid memory leaks or don't throw
    auto index  = get_index_of(buffer, buffer_size, 0);
    buffer_size = remove(buffer, buffer_size, index + 1);
    print(buffer, buffer_size);

    std::FILE* file2 = std::tmpfile();
    if (file2 == nullptr) {
        throw std::runtime_error("Could not open file\n");
    }

    if (std::fwrite(buffer, sizeof(int), buffer_size, file2) < buffer_size) {
        throw std::runtime_error("Could not write to file\n");
    }
    std::rewind(file2);
    delete[] buffer;

    if (std::fclose(file1) != 0) {
        throw std::runtime_error("Could not close file\n");
    }
    if (std::fclose(file2) != 0) {
        throw std::runtime_error("Could not close file\n");
    }

    return 0;
} catch (const std::exception& error) {
    std::cerr << "ERROR: " << error.what();
    return 1;
}
