#ifndef IO_STANDARD_HPP_
#define IO_STANDARD_HPP_

#include <iostream>

namespace io {
    template<typename T>
    static constexpr T get_input(const char* prompt) {
        T value;
        std::cout << prompt;
        std::cin >> value;
        return value;
    }
}  // namespace io

#endif  // IO_STANDARD_HPP_
