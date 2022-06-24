#include <algorithm>
#include <bitset>
#include <iostream>
#include <string>
#include <vector>

template<typename T>
auto to_binary(const T& number) {
    return std::bitset<sizeof(T) * CHAR_BIT>(number);
}

void chop_left_padding(std::string* binary, const char padding) {
    binary->erase(0, binary->find_first_not_of(padding));
}

std::string dec2bin_str(auto number) {
    auto binary = to_binary(number).to_string();
    chop_left_padding(&binary, '0');
    return binary;
}

template<typename T>
auto get_zeros(T numbers, auto at_least_zeros) {
    std::vector<std::string> strings {};
    for (auto& item : numbers) {
        auto value = dec2bin_str(item);
        strings.push_back(value);
    }

    auto filter = [](auto s1, auto s2) {
        return s1.size() < s2.size();
    };
    auto min_item = *std::ranges::min_element(strings, filter);

    for (auto& item : strings) {
        std::ranges::reverse(item);
    }

    auto counter = 0;
    for (int i = 0; i < min_item.size(); i++) {
        auto value = 0;
        for (auto& item : strings) {
            if (item[i] == '0') {
                value += 1;
            }
        }
        if (value >= at_least_zeros) {
            counter += 1;
        }
    }
    return counter;
}

int main() {
    const std::vector<int> numbers {5139, 84, 2517, 45};
    /*        + + +
     * 1010000010011
     *       1010100
     *  100111010101
     *        101101
     * */
    const auto result = get_zeros(numbers, 3);
    std::cout << "result: " << result << "\n";
    return 0;
}
