#include <iostream>

#define GET(member)                                                                 \
    [[nodiscard]] constexpr auto get##member() const noexcept -> decltype(member) { \
        return member;                                                              \
    }

#define SET(member)                                                       \
    constexpr auto set##member(decltype(member) value) noexcept -> void { \
        this->member = value;                                             \
    }

namespace gsl {
    using czstring = const char*;
}  // namespace gsl

enum class Occupation {
    Manager,
    None,
    Worker,
};

auto operator<<(std::ostream& os, const Occupation& occupation) -> std::ostream& {
    switch (occupation) {
        case Occupation::Manager:
            return os << "Manager";
        case Occupation::None:
            return os << "None";
        case Occupation::Worker:
            return os << "Worker";
        default:
            os.setstate(std::ios::failbit);
    }
}

class Person {
  private:
    gsl::czstring _name    = "";
    gsl::czstring _surname = "";

  public:
    GET(_name)
    GET(_surname)

    SET(_name)
    SET(_surname)

    constexpr Person() = default;

    constexpr Person(gsl::czstring name, gsl::czstring surname) :
        _name(name),
        _surname(surname) {}

    constexpr Person(const Person&)                    = default;
    constexpr auto operator=(const Person&) -> Person& = default;

    constexpr Person(Person&&) noexcept                    = default;
    constexpr auto operator=(Person&&) noexcept -> Person& = default;

    virtual constexpr ~Person() = default;

    friend auto operator<<(std::ostream& os, const Person& other) -> std::ostream& { return other.print(os); }

    virtual auto print(std::ostream& os) const -> std::ostream& {
        os << "Name: " << _name << "\n";
        os << "Surname: " << _surname << "\n";
        return os;
    }
};

class Employee final : public Person {
  private:
    Occupation    _occupation         = Occupation::None;
    std::intmax_t _salary             = 0;
    std::intmax_t _year_of_employment = 0;

  public:
    GET(_occupation)
    GET(_salary)
    GET(_year_of_employment)

    SET(_occupation)
    SET(_salary)
    SET(_year_of_employment)

    constexpr Employee() = default;

    constexpr Employee(
        gsl::czstring name,
        gsl::czstring surname,
        Occupation    occupation,
        std::intmax_t salary,
        std::intmax_t year_of_employment
    ) :
        Person(name, surname),
        _occupation(occupation),
        _salary(salary),
        _year_of_employment(year_of_employment) {}

    constexpr Employee(const Employee&)                    = default;
    constexpr auto operator=(const Employee&) -> Employee& = default;

    constexpr Employee(Employee&&) noexcept                    = default;
    constexpr auto operator=(Employee&&) noexcept -> Employee& = default;

    constexpr ~Employee() override = default;

    auto print(std::ostream& os) const -> std::ostream& override {
        Person::print(os);
        os << "Occupation: " << _occupation << "\n";
        os << "Salary: " << _salary << "\n";
        os << "Year of employment: " << _year_of_employment << "\n";
        return os;
    }
};

auto main() -> int {
    {
        Employee employee("Rich", "Campbell", Occupation::Worker, 1850, 2020);
        std::cout << employee << "\n";
        employee.set_occupation(Occupation::Manager);
        employee.set_salary(3000);
        std::cout << employee;
    }

    return 0;
}
