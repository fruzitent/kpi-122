#include <chrono>
#include <iostream>

#define GET_INPUT(type, name)              \
    type name;                             \
    std::cout << "enter " << #name << ":"; \
    std::cin >> name

auto get_date(auto day, auto month, auto year) {
    return std::chrono::year_month_day(
        std::chrono::year(year),
        std::chrono::month(month),
        std::chrono::day(day)
    );
}

int main() {
    GET_INPUT(int, day);
    GET_INPUT(int, month);
    GET_INPUT(int, year);  // 1973, 1979, 1990, 2001, 2007, 2018, 2029

    const auto date = get_date(day, month, year);
    if (!date.ok()) {
        throw std::invalid_argument("invalid date");
    }

    if (std::chrono::weekday(get_date(1, 1, year)) != std::chrono::Monday) {
        throw std::invalid_argument("year does not start on monday");
    }

    const auto weekday = std::chrono::weekday(date);
    std::cout << "date: " << date << "\n";
    std::cout << "weekday: " << weekday << "\n";

    return 0;
}
