#include <iostream>

#define GET_INPUT(type, name)              \
    type name;                             \
    std::cout << "enter " << #name << ":"; \
    std::cin >> name

auto parabola(auto x, auto a, auto b, auto c) {
    return (a * pow(x, 2)) + (b * x) + c;
}

int main() {
    constexpr int a    = -3;
    constexpr int b    = 0;
    constexpr int c    = 5;
    constexpr int line = 3;
    GET_INPUT(float, pos_x);
    GET_INPUT(float, pos_y);
    const auto value = parabola(pos_x, a, b, c);

    std::cout << "point (" << pos_x << "; " << pos_y << ") is ";
    if (pos_x <= 0 && pos_y <= line && pos_y < value) {
        std::cout << "in definition area\n";
    } else {
        std::cout << "out of definition area\n";
    }

    return 0;
}
