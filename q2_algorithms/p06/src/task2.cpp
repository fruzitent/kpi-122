#include <iostream>

#define GET_INPUT(type, name)              \
    type name;                             \
    std::cout << "enter " << #name << ":"; \
    std::cin >> name

bool is_something(auto x, auto y, auto z) {
    return x && !y && !(x && !z);
}

int main() {
    GET_INPUT(float, x);
    GET_INPUT(float, y);
    GET_INPUT(float, z);
    const auto result = is_something(x, y, z);
    std::cout << std::boolalpha << result << "\n";
    return 0;
}
