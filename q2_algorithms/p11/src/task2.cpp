#include <cmath>
#include <iostream>

double get_rightmost_unset_bit(int n) {
    if ((n & (n + 1)) == 0) {
        return -1;
    }
    return n == 0 ? 1 : std::log2(~n & -~n) + 1;
}

int main() {
    constexpr auto num = 11;  // 0b1011
    const auto     pos = get_rightmost_unset_bit(num);
    std::cout << "pos 0: " << sizeof(num) - pos << "\n";
    return 0;
}
