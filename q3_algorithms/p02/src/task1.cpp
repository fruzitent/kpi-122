#include <iostream>
#include <map>
#include <string>
// #include <utility> // C++23

#define GET_INPUT(type, name)              \
    type name;                             \
    std::cout << "enter " << #name << ":"; \
    std::cin >> name

// enum class Genre { // C++23
enum class Genre : int {
    Drama,
    Novel,
    Novella,
    Poetry,
    Story,
    MAX_COUNT,
};

static_assert(
    // std::to_underlying(Genre::MAX_COUNT) == 5, // C++23
    static_cast<int>(Genre::MAX_COUNT) == 5,
    "an unexpected number of genres"
);
std::map<Genre, std::string> genre2str = {
    {Genre::Drama,   "Drama"  },
    {Genre::Novel,   "Novel"  },
    {Genre::Novella, "Novella"},
    {Genre::Poetry,  "Poetry" },
    {Genre::Story,   "Story"  },
};

std::istream& operator>>(std::istream& in, Genre& genre) {
    int value;
    in >> value;
    genre = static_cast<Genre>(value);
    return in;
}

std::ostream& operator<<(std::ostream& out, Genre genre) {
    return out << genre2str[genre];
}

int main() {
    std::cout << "12334\n";
    GET_INPUT(Genre, genre);
    std::cout << genre << "\n";
    return 0;
}
