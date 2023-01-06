#include <cmath>
#include <cstring>
#include <iostream>
#include <memory>

class Input {
  public:
    Input()                         = default;
    Input(const Input &)            = default;
    Input(Input &&)                 = default;
    virtual ~Input()                = default;
    Input &operator=(const Input &) = default;
    Input &operator=(Input &&)      = default;

    virtual void read() { std::cout << "Input Read\n"; }

    virtual void save() {}
};

class ConsoleInput : public Input {
  public:
    void read() override { std::cout << "Console Read\n"; }

    void save() override {}
};

class FileInput : public Input {
  public:
    void read() override { std::cout << "File Read\n"; }

    void save() override {}
};

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

    if (std::strcmp(argv[1], "console") == 0) {
        ConsoleInput input;
        input.read();
        return 0;
    }

    if (std::strcmp(argv[1], "file") == 0) {
        FileInput input;
        input.read();
        return 0;
    }

    usage(std::cerr) << "ERROR: Unknown argument\n";
    return 1;
}
