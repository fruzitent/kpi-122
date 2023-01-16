#include <iostream>

struct multiplies {
    template<typename T>
    constexpr T operator()(T lhs, T rhs) const {
        return lhs * rhs;
    }
};

static constexpr void fill(auto* array, std::size_t size) {
    for (std::size_t i = 0; i < size; ++i) {
        std::cout << "Enter #" << i << ": ";
        std::cin >> array[i];
    }
}

template<typename T>
static constexpr std::size_t filter(T* array, std::size_t size, bool (*predicate)(T)) {
    T* pos   = array;
    T* first = array;
    T* last  = array + size;

    for (; first != last; ++first) {
        if (predicate(*first)) {
            *pos++ = *first;
        }
    }

    return static_cast<std::size_t>(pos - array);
}

template<typename T>
T* get_matrix_col(T* matrix, std::size_t cols, std::size_t rows, std::size_t index) {
    T* col = new T[rows] {};

    for (std::size_t i = 0; i < rows; ++i) {
        col[i] = matrix[i * cols + index];
    }

    return col;
}

template<typename T>
T* get_matrix_row(T* matrix, std::size_t cols, std::size_t index) {
    T* row = new T[cols] {};

    for (std::size_t i = 0; i < cols; ++i) {
        row[i] = matrix[index * cols + i];
    }

    return row;
}

static constexpr bool is_even(auto value) {
    return value % 2 == 0;
}

static constexpr bool is_odd(auto value) {
    return value % 2 != 0;
}

template<typename T>
static constexpr T reduce(T* array, std::size_t size, auto reducer, T initial) {
    T result = initial;
    for (std::size_t i = 0; i < size; ++i) {
        result = reducer(result, array[i]);
    }
    return result;
}

void print(auto* arr, std::size_t size) {
    for (std::size_t i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << "\n";
}

int main() try {
    static constexpr std::size_t cols = 3;
    static constexpr std::size_t rows = 3;

    std::size_t size   = cols * rows;
    auto*       matrix = new int[size] {};
    fill(matrix, size);

    {
        static constexpr std::size_t row_id = 1;
        std::cout << "[row #" << row_id << "]\n";

        auto* row = get_matrix_row(matrix, cols, row_id);
        std::cout << "Original: ";
        print(row, cols);

        auto width = filter(row, cols, is_odd);
        std::cout << "Odd: ";
        print(row, width);

        auto product = reduce(row, width, multiplies(), 1);
        std::cout << "Prduct: " << product << "\n";
        delete[] row;
    }

    {
        static constexpr std::size_t col_id = 1;
        std::cout << "[col #" << col_id << "]\n";

        auto* col = get_matrix_col(matrix, cols, rows, col_id);
        std::cout << "Original: ";
        print(col, rows);

        auto width = filter(col, cols, is_even);
        std::cout << "Even: ";
        print(col, width);

        auto product = reduce(col, width, multiplies(), 1);
        std::cout << "Prduct: " << product << "\n";
        delete[] col;
    }

    delete[] matrix;
    return 0;
} catch (const std::exception& error) {
    std::cerr << "ERROR: " << error.what();
    return 1;
}
