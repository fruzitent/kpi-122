#include <iostream>
#include <string>
#include <vector>

#define GET_INPUT(type, name)              \
    type name;                             \
    std::cout << "enter " << #name << ":"; \
    std::cin >> name

std::string get_romanized(auto number) {
    if (number < 0 || number > 4000) {
        throw std::invalid_argument("out of range value");
    }

    std::vector<std::string> ones = {
        "",
        "I",
        "II",
        "III",
        "IV",
        "V",
        "VI",
        "VII",
        "VIII",
        "IX",
    };
    std::vector<std::string> tens = {
        "",
        "X",
        "XX",
        "XXX",
        "XL",
        "L",
        "LX",
        "LXX",
        "LXXX",
        "XC",
    };
    std::vector<std::string> hundreds = {
        "",
        "C",
        "CC",
        "CCC",
        "CD",
        "D",
        "DC",
        "DCC",
        "DCCC",
        "CM",
    };
    std::vector<std::string> thousands = {
        "",
        "M",
        "MM",
        "MMM",
        "MMMM",
    };

    auto one      = ones[std::floor(number % 10)];
    auto ten      = tens[std::floor(number / 10 % 10)];
    auto hundred  = hundreds[std::floor(number / 100 % 10)];
    auto thousand = thousands[std::floor(number / 1000)];

    return thousand + hundred + ten + one;
}

int main() {
    GET_INPUT(int, k);

    switch (k) {
        case 0:
        case 1:
        case 2:
            std::cout << "1st quarter\n1st half\n";
            break;

        case 3:
        case 4:
        case 5:
            std::cout << "2nd quarter\n1st half\n";
            break;

        case 6:
        case 7:
        case 8:
            std::cout << "3rd quarter\n2nd half\n";
            break;

        case 9:
        case 10:
        case 11:
            std::cout << "4th quarter\n2nd half\n";
            break;

        default:
            std::cout << "unexpected value\n";
            break;
    }

    if (0 < k && k < 40) {
        std::cout << get_romanized(k) << "\n";
    }

    return 0;
}
