#include <iostream>

#define GET_INPUT(type, name)              \
    type name;                             \
    std::cout << "enter " << #name << ":"; \
    std::cin >> name

double get_sum(const double k) {
    const double value = 1 / k;
    return value == 1 ? value : value + get_sum(k - 1);
}

int main() {
    GET_INPUT(int, k);
    if (k <= 0) {
        throw std::invalid_argument("value must be greater than zero");
    }
    const auto res = get_sum(k);
    std::cout << "res: " << res << "\n";
    return 0;
}
