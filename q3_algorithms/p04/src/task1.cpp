#include <functional>
#include <iostream>
#include <random>

#include "src/matrix.hpp"

bool is_even(auto value) {
    return value % 2 == 0;
}

bool is_odd(auto value) {
    return value % 2 != 0;
}

int main() {
    std::random_device                 seed;
    std::mt19937                       gen(seed());
    std::uniform_int_distribution<int> dist(-100, 100);

    auto rng = [&dist, &gen]() {
        return dist(gen);
    };

    Matrix<int> matrix(5, 5);
    matrix.fill(rng);
    std::cout << matrix << "\n";

    {
        auto row_id = 1;
        auto row    = matrix.row(row_id);
        std::cout << "row #" << row_id << ": " << *row;

        auto row_filtered = row->filter(is_odd);
        std::cout << "filter: " << *row_filtered;

        auto row_product = row_filtered->reduce(std::multiplies(), 1);
        std::cout << "product: " << row_product << "\n";
    }

    std::cout << "\n";

    {
        auto col_id = 1;
        auto col    = matrix.col(col_id);
        std::cout << "col #" << col_id << ": " << *col;

        auto col_filtered = col->filter(is_even);
        std::cout << "filter: " << *col_filtered;

        auto col_product = col_filtered->reduce(std::multiplies(), 1);
        std::cout << "product: " << col_product << "\n";
    }

    return 0;
}
