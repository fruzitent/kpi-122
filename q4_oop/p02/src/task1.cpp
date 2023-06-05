#include "./vector.hpp"

#include <algorithm>
#include <chrono> // NOLINT(build/c++11)
#include <compare>
#include <cstdlib>
#include <exception>
#include <fmt/core.h>
#include <fmt/ostream.h>
#include <iostream>
#include <ranges>
#include <ratio>
#include <string>
#include <typeinfo>
#include <unordered_map>

auto year_to_str(const std::chrono::year &value) -> std::string {
    return value.ok() ? fmt::format("{}", static_cast<int>(value))
                      : fmt::format("{} is not a valid year", static_cast<int>(value));
}

auto operator<<(std::ostream &os, const std::chrono::year &value) -> std::ostream & {
    return os << year_to_str(value);
}

template <>
struct fmt::formatter<std::chrono::year> : public fmt::formatter<fmt::string_view> {
    static auto format(const std::chrono::year &value, fmt::format_context &ctx) -> fmt::appender {
        return fmt::format_to(ctx.out(), "{}", year_to_str(value));
    }
};

enum class Occupation : std::size_t {
    Analyst,
    Architect,
    Artist,
    Engineer,
    Manager,
    None,
    QA,
    Recruiter,
    Sales,
};

auto occupation_to_str(const Occupation &value) -> std::string {
    static const std::unordered_map<Occupation, std::string> map{
        {Occupation::Analyst,   "Analyst"  },
        {Occupation::Architect, "Architect"},
        {Occupation::Artist,    "Artist"   },
        {Occupation::Engineer,  "Engineer" },
        {Occupation::Manager,   "Manager"  },
        {Occupation::None,      "None"     },
        {Occupation::QA,        "QA"       },
        {Occupation::Recruiter, "Recruiter"},
        {Occupation::Sales,     "Sales"    },
    };
    return map.at(value);
}

auto operator<<(std::ostream &os, const Occupation &value) -> std::ostream & {
    return os << occupation_to_str(value);
}

template <>
struct fmt::formatter<Occupation> : public fmt::formatter<fmt::string_view> {
    static auto format(const Occupation &value, fmt::format_context &ctx) -> fmt::appender {
        return fmt::format_to(ctx.out(), "{}", occupation_to_str(value));
    }
};

struct Employee {
    std::string       name;
    std::string       surname;
    Occupation        occupation = Occupation::None;
    double            salary;
    std::chrono::year employed_at;

    [[nodiscard]] auto repr() const -> std::string {
        std::string value;
        value += fmt::format("{} {}\n", name, surname);
        value += fmt::format("occupation: {}\n", occupation);
        value += fmt::format("salary: {}\n", salary);
        value += fmt::format("employed_at: {}", employed_at);
        return value;
    }
};

auto operator<<(std::ostream &os, const Employee &value) -> std::ostream & {
    return os << value.repr();
}

template <>
struct fmt::formatter<Employee> : public fmt::formatter<fmt::string_view> {
    static auto format(const Employee &value, fmt::format_context &ctx) -> fmt::appender {
        return fmt::format_to(ctx.out(), "{}", value.repr());
    }
};

auto main() -> int try {
    myproject::vector<Employee> vec;

    {
        // NOLINTBEGIN(*-magic-numbers)
        using std::literals::chrono_literals::operator""y;
        vec.emplace_back("Zachery", "Austin", Occupation::Artist, 701, 2021y);
        vec.emplace_back("Rylee", "Cabrera", Occupation::Sales, 1458, 2011y);
        vec.emplace_back("Desmond", "Cortez", Occupation::Analyst, 2928, 2004y);
        vec.emplace_back("Victor", "Daugherty", Occupation::QA, 4489, 1995y);
        vec.emplace_back("Larissa", "Ewing", Occupation::Engineer, 4539, 2015y);
        vec.emplace_back("Talon", "Finley", Occupation::Analyst, 2512, 2008y);
        vec.emplace_back("Caitlin", "Hamilton", Occupation::Manager, 3820, 2002y);
        vec.emplace_back("Jayla", "Jackson", Occupation::QA, 525, 2016y);
        vec.emplace_back("Heidi", "Kim", Occupation::Recruiter, 971, 2022y);
        vec.emplace_back("Jaida", "Leblanc", Occupation::Artist, 2680, 2017y);
        vec.emplace_back("Abel", "Lester", Occupation::Sales, 1657, 2022y);
        vec.emplace_back("Valentino", "Young", Occupation::Architect, 8966, 2014y);
        // NOLINTEND(*-magic-numbers)
    }

    constexpr auto print = [](auto &&view) -> void {
        for (std::size_t index = 0; const auto &item : view) {
            fmt::println("[{:02}]: {}\n", ++index, item);
        }
    };

    {
        constexpr auto required  = std::chrono::years(10);
        constexpr auto predicate = [required](const Employee &value) -> bool {
            auto now   = std::chrono::system_clock::now();
            auto today = std::chrono::year_month_day(std::chrono::floor<std::chrono::days>(now));
            auto diff  = today.year() - value.employed_at;
            return diff >= required;
        };

        fmt::println("Employees whose work experience exceeds a specified number of years, `{}`", required.count());
        print(vec | std::ranges::views::filter(predicate));
    }

    {
        constexpr auto required  = 3000;
        constexpr auto predicate = [](const Employee &value) -> bool {
            return value.salary > required;
        };

        fmt::println("Employees whose salary is more than a given one, `{}`", required);
        print(vec | std::ranges::views::filter(predicate));
    }

    {
        constexpr auto required  = Occupation::Artist;
        constexpr auto predicate = [](const Employee &value) {
            return value.occupation == required;
        };

        fmt::println("Employees who hold a given position, `{}`", required);
        print(vec | std::ranges::views::filter(predicate));
    }

    return EXIT_SUCCESS;
} catch (const std::exception &error) {
    fmt::println(std::cerr, "std::terminate called after throwing an exception:\n");
    fmt::println(std::cerr, "      type: {}", typeid(error).name());
    fmt::println(std::cerr, "    what(): {}", error.what());
    return EXIT_FAILURE;
} catch (...) {
    fmt::println(std::cerr, "std::terminate called after throwing an unknown exception");
    return EXIT_FAILURE;
}
