#include <iostream>
#include <vector>

void print(auto range) {
    for (auto item : range) {
        std::cout << item << " ";
    }
    std::cout << "\n";
}

void print(auto* arr, std::size_t size) {
    for (auto i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << "\n";
}

template<typename T>
void merge(
    T*          arr0,
    std::size_t size0,
    T*          arr1,
    std::size_t size1,
    T*          arr2,
    bool        strict = false
) {
    if (strict && size0 != size1) {
        throw std::invalid_argument("size0 != size1");
    }

    auto it0 = 0;
    auto it1 = 0;
    auto it2 = 0;

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

template<typename T>
std::vector<T>
merge(std::vector<T> vec0, std::vector<T> vec1, bool strict = false) {
    if (strict && vec0.size() != vec1.size()) {
        throw std::invalid_argument("size0 != size1");
    }

    auto it0 = vec0.begin();
    auto it1 = vec1.begin();

    std::vector<T> res {};

    while (it0 != vec0.end() && it1 != vec1.end()) {
        res.push_back(*it0++);
        res.push_back(*it1++);
    }

    while (it0 != vec0.end()) {
        res.push_back(*it0++);
    }

    while (it1 != vec1.end()) {
        res.push_back(*it1++);
    }

    return res;
}

void carray() {
    std::size_t size0 = 5;
    std::size_t size1 = 10;
    std::size_t size2 = size0 + size1;

    auto* arr0 = new int[size0] {1, 3, 5, 7, 9};
    auto* arr1 = new int[size1] {2, 4, 6, 8, 10, 11, 12, 13, 14, 15};
    auto* arr2 = new int[size2] {};

    merge(arr0, size0, arr1, size1, arr2);
    print(arr2, size2);

    delete[] arr0;
    delete[] arr1;
    delete[] arr2;
}

void stl_vector() {
    std::vector<int> vec0 {1, 3, 5, 7, 9};
    std::vector<int> vec1 {2, 4, 6, 8, 10, 11, 12, 13, 14, 15};

    auto vec2 = merge(vec0, vec1);
    print(vec2);

    vec0.clear();
    vec1.clear();
    vec2.clear();
}

int main() {
    carray();
    stl_vector();
    return 0;
}
