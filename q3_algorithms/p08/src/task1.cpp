#include <iostream>

struct Person {
    const char* name;
    const char* patronymic;
    const char* surname;

    constexpr void print(std::ostream& out) const { out << name << " " << patronymic << " " << surname; }

    friend constexpr std::ostream& operator<<(std::ostream& out, const Person& person) {
        person.print(out);
        return out;
    }
};

struct Wage {
    const double hours;
    const double rate;

    static constexpr double overtime_hours      = 144;
    static constexpr double overtime_multiplier = 2;
    static constexpr double tax                 = 0.12;

    constexpr void print(std::ostream& out) const { out << total() << " (net: " << net() << ")"; }

    friend constexpr std::ostream& operator<<(std::ostream& out, const Wage& wage) {
        wage.print(out);
        return out;
    }

    [[nodiscard]] constexpr double total() const {
        auto regular  = rate * std::min(hours, overtime_hours);
        auto overtime = rate * std::max(hours - overtime_hours, 0.0);
        return regular + (overtime * overtime_multiplier);
    }

    [[nodiscard]] constexpr double net() const { return total() * (1 - tax); }
};

struct Employee {
    const std::size_t id;
    const Person      person;
    const Wage        wage;

    constexpr void print(std::ostream& out) const {
        out << "#: " << id << "\n";
        out << "Name: " << person << "\n";
        out << "Wage: " << wage;
    }

    friend constexpr std::ostream& operator<<(std::ostream& out, const Employee& employee) {
        employee.print(out);
        return out;
    }
};

int main() try {
    constexpr std::size_t employee_count = 3;

    const auto* employees = new Employee[employee_count] {
        Employee {0, {"Abel", "Janszoon", "Tasman"}, {75, 3} },
        Employee {1, {"Daniel", "Jonson", "Rasmus"}, {125, 3}},
        Employee {2, {"Jon", "Andersen", "Cain"},    {150, 3}},
    };

    for (auto i = 0; i < employee_count; ++i) {
        std::cout << employees[i] << "\n\n";
    }

    delete[] employees;
    return 0;
} catch (const std::exception& error) {
    std::cerr << "ERROR: " << error.what();
    return 1;
}
