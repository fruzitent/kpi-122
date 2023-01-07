#include <cmath>
#include <cstring>
#include <iostream>

struct UserInput {
    double xbegin;
    double xend;
    double xstep;
    double epsilon;

    auto size() const { return static_cast<std::size_t>(std::floor((xend - xbegin) / xstep)); }
};

struct UserOutput {
    double      x;
    double      fy;
    double      sy;
    double      abs_error;
    std::size_t members;
};

enum class InputType {
    File,
    Standard,
};

class Input {
  public:
    Input()                         = default;
    Input(const Input &)            = default;
    Input(Input &&)                 = default;
    virtual ~Input()                = default;
    Input &operator=(const Input &) = default;
    Input &operator=(Input &&)      = default;

    static Input *make_input(InputType type);

    virtual UserInput read([[maybe_unused]] const char *filepath) const = 0;

    virtual void save() const = 0;
};

class FileInput : public Input {
  public:
    UserInput read([[maybe_unused]] const char *filepath) const override {
        static constexpr double xbegin  = -9;
        static constexpr double xend    = 9;
        static constexpr double xstep   = 1;
        static constexpr double epsilon = 0.001;
        return UserInput {xbegin, xend, xstep, epsilon};
    }

    void save() const override {}
};

class StandardInput : public Input {
  public:
    UserInput read([[maybe_unused]] const char *filepath) const override {
        static constexpr double xbegin  = -9;
        static constexpr double xend    = 9;
        static constexpr double xstep   = 1;
        static constexpr double epsilon = 0.001;
        return UserInput {xbegin, xend, xstep, epsilon};
    }

    void save() const override {}
};

Input *Input::make_input(InputType type) {
    switch (type) {
        case InputType::File:
            return new FileInput();
        case InputType::Standard:
            return new StandardInput();
        default:
            return nullptr;
    }
}

std::ostream &usage(std::ostream &out) {
    out << "Description:\n";
    out << "  This program approximates function using Maclaurin Series\n";
    out << "\n";

    out << "Usage:\n";
    out << "  ./main [options] [--] <name>\n";
    out << "\n";

    out << "Arguments:\n";
    out << "  name: path to csv-file\n";
    out << "\n";

    out << "Options:\n";
    out << "  --help: show this message and exit\n";
    return out;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        usage(std::cerr) << "ERROR: Not enough arguments\n";
        return 1;
    }

    if (std::strcmp(argv[1], "--help") == 0) {
        usage(std::cout);
        return 0;
    }

    Input    *input = nullptr;
    UserInput userinput {};

    if (std::strcmp(argv[1], "file") == 0) {
        input     = Input::make_input(InputType::File);
        userinput = input->read(argv[2]);
    }

    if (std::strcmp(argv[1], "standard") == 0) {
        input     = Input::make_input(InputType::Standard);
        userinput = input->read(nullptr);
    }

    return 0;
}
