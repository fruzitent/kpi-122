#include <iostream>
#include <string>

struct user {
    std::string name;
    int         variant {};
};

int main() {
    auto [name, variant] = user();
    std::cout << "Enter your name:\n";
    std::getline(std::cin, name);
    std::cout << "Enter your variant:\n";
    std::cin >> variant;
    std::cout << "Hello, " << name << "! You're #" << variant << ".\n";
    return 0;
}
