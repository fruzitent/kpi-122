#include <iostream>

#define GET_INPUT(type, name)              \
    type name;                             \
    std::cout << "enter " << #name << ":"; \
    std::cin >> name

auto calculate(auto a, auto b, auto c, auto d) {
    auto numerator   = sinh(b) / log(abs(c + d));
    auto denominator = pow(tan(a), 1 / c);
    return (6 + numerator) / denominator;
}

int main() {
    GET_INPUT(float, a);
    GET_INPUT(float, b);
    GET_INPUT(float, c);
    GET_INPUT(float, d);
    const auto result = calculate(a, b, c, d);
    std::cout << "result: " << result << "\n";
    printf_s(
        "a: %.2f, "
        "b: %.2f, "
        "c: %.2f, "
        "d: %.2f\n",
        a,
        b,
        c,
        d
    );
    return 0;
}
