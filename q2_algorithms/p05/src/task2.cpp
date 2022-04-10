#include <iostream>

auto calculate(auto a, auto b, auto c, auto d) {
    auto left  = cos(a) / (sin(c) * pow(a, b));
    auto right = 2 * log(d);
    return left + right;
}

int main() {
    constexpr auto a = 1.11;
    constexpr auto b = -2.22;
    constexpr auto c = 3.33;
    constexpr auto d = 4.44;  // TODO(p05): -4.44?

    const auto result = calculate(a, b, c, d);
    std::cout << "result: " << result << "\n";

    return 0;
}
