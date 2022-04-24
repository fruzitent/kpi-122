#include <iostream>

auto calculate(auto x) {
    return (pow(x, 2) / 2) + (2.5 * x);
}

double get_value(auto t) {
    if (t < 5) {
        return (3 * t) - 15;
    }
    if (t == 5) {
        return pow(t, 2) - 3;
    }
    return t + 10;
}

int main() {
    constexpr int   from = 2;
    constexpr int   to   = 7;
    constexpr float step = 0.5;

    for (int i = 0; i < (to - from) / step; i++) {
        const auto t = from + i * step;
        const auto x = get_value(t);
        const auto y = calculate(x);
        std::cout << i << " | (" << t << "; " << y << ")\n";
    }

    return 0;
}
