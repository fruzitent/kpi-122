#include <iostream>

auto calculate(auto x) {
    return pow(x, 3) + 1.755 * pow(cos(x), 2);
}

double get_value(auto t) {
    if (t == 2) {
        return 1 / t;
    }
    if (t <= 3) {
        return pow(t, 2);
    }
    return 1 / cos(t);
}

int main() {
    constexpr int   from = 1;
    constexpr int   to   = 6;
    constexpr float step = 0.5;

    for (int i = 0; i < (to - from) / step; i++) {
        const auto t = from + i * step;
        const auto x = get_value(t);
        const auto y = calculate(x);
        std::cout << i << " | (" << t << "; " << y << ")\n";
    }

    return 0;
}
