#include <iostream>

void fill(auto* array, std::size_t size) {
    for (std::size_t i = 0; i < size; ++i) {
        std::cout << "Enter #" << i << ": ";
        std::cin >> array[i];
    }
}

template<typename T>
void merge(T* arr0, std::size_t size0, T* arr1, std::size_t size1, T* arr2, bool strict = false) {
    if (strict && size0 != size1) {
        throw std::invalid_argument("size0 != size1");
    }

    std::size_t it0 = 0;
    std::size_t it1 = 0;
    std::size_t it2 = 0;

    while (it0 < size0 && it1 < size1) {
        arr2[it2++] = arr0[it0++];
        arr2[it2++] = arr1[it1++];
    }

    while (it0 < size0) {
        arr2[it2++] = arr0[it0++];
    }

    while (it1 < size1) {
        arr2[it2++] = arr1[it1++];
    }
}

void print(auto* arr, std::size_t size) {
    for (std::size_t i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << "\n";
}

int main() try {
    static constexpr std::size_t size0 = 5;
    static constexpr std::size_t size1 = 10;
    static constexpr std::size_t size2 = size0 + size1;

    auto* arr0 = new int[size0] {};
    auto* arr1 = new int[size1] {};
    fill(arr0, size0);
    fill(arr1, size1);

    auto* arr2 = new int[size2] {};
    merge(arr0, size0, arr1, size1, arr2);
    print(arr2, size2);

    delete[] arr0;
    delete[] arr1;
    delete[] arr2;
    return 0;
} catch (const std::exception& error) {
    std::cerr << "ERROR: " << error.what();
    return 1;
}
