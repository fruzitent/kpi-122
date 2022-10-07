#include <iostream>
#include <random>

#include "src/matrix.hpp"

bool is_even(auto value) {
    return value % 2 == 0;
}

int main() {
    std::random_device                 seed;
    std::mt19937                       gen(seed());
    std::uniform_int_distribution<int> dist(0, 100);

    auto prng = [&dist, &gen]() {
        return dist(gen);
    };

    Matrix<int> matrix(5, 5);
    matrix.fill(prng);
    std::cout << matrix;

    auto rid = 1;
    auto rwp = matrix.row_product(rid, is_even);
    std::cout << "Row #" << rid << " product: " << rwp.view << "\n";

    auto cid = 1;
    auto clp = matrix.col_product(cid, is_even);
    std::cout << "Col #" << cid << " product: " << clp.view << "\n";

    return 0;
}
