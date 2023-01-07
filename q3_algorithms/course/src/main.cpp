#include <cmath>
#include <cstring>
#include <iostream>

#define DEFER_1(x, y) x##y
#define DEFER_2(x, y) DEFER_1(x, y)
#define DEFER_3(x)    DEFER_2(x, __COUNTER__)
#define defer(code)                            \
    auto DEFER_3(_defer_) = make_defer([&]() { \
        code;                                  \
    })

template<typename T>
struct Defer {
    T callback;

    explicit Defer(T callback) :
        callback(callback) {}

    Defer(const Defer &)     = default;
    Defer(Defer &&) noexcept = default;

    ~Defer() { callback(); }

    Defer &operator=(const Defer &)     = default;
    Defer &operator=(Defer &&) noexcept = default;
};

template<typename T>
Defer<T> make_defer(T callback) {
    return Defer<T>(callback);
}

namespace gsl {  // https://github.com/microsoft/GSL
    template<typename T, typename = std::enable_if_t<std::is_pointer<T>::value>>
    using owner = T;

    template<typename T, std::size_t size>
    constexpr T &at(T (&arr)[size], const std::size_t index) {  // NOLINT
        if (index < 0 || index >= size) {
            std::cerr << "ERROR: index out of bounds\n";
            std::_Exit(EXIT_FAILURE);
        }
        return arr[index];
    }
}  // namespace gsl

struct SeriesReturn {
    double      sigma;
    std::size_t members;
};

auto get_series(double x, double abs_error, double epsilon) {
    double      sigma   = 0;
    std::size_t members = 2;

    while (std::abs(abs_error) > epsilon) {
        sigma += abs_error;
        abs_error *= -std::pow(x, 2) / (static_cast<double>(members) * 2);
        ++members;
    }

    return SeriesReturn {sigma, members};
}

double get_function(double x) {
    if (x == 0) {
        return 0;
    }
    return (1 - std::exp(-std::pow(x, 2) / 2)) / x;
}

struct UserInput {
    double xbegin;
    double xend;
    double xstep;
    double epsilon;

    auto size() const { return static_cast<std::size_t>(((xend - xbegin) / xstep) + 1); }
};

struct UserOutput {
    double       x;
    double       fy;
    SeriesReturn series;
    double       abs_error;
};

void run(UserInput input, UserOutput *output, std::size_t size) {
    for (decltype(size) i = 0; i < size; ++i) {
        double x = input.xbegin + static_cast<double>(i) * input.xstep;

        if (x == 0) {
            continue;
        }

        auto fy        = get_function(x);
        auto series    = get_series(x, x / 2, input.epsilon);
        auto abs_error = std::abs(fy - series.sigma);
        output[i]      = UserOutput {x, fy, series, abs_error};
    }
}

enum class InputType {
    File,
    Standard,
};

class Input {
  public:
    Input()                  = default;
    Input(const Input &)     = default;
    Input(Input &&) noexcept = default;

    virtual ~Input() = default;

    Input &operator=(const Input &)     = default;
    Input &operator=(Input &&) noexcept = default;

    static Input *make_input(InputType type);

    virtual UserInput read([[maybe_unused]] const char *filepath) const = 0;

    virtual void save() const = 0;
};

class FileInput : public Input {
  public:
    UserInput read([[maybe_unused]] const char *filepath) const override {
        static constexpr double xbegin  = -5;
        static constexpr double xend    = 5;
        static constexpr double xstep   = 1;
        static constexpr double epsilon = 0.001;
        return UserInput {xbegin, xend, xstep, epsilon};
    }

    void save() const override {}
};

class StandardInput : public Input {
  public:
    UserInput read([[maybe_unused]] const char *filepath) const override {
        static constexpr double xbegin  = -5;
        static constexpr double xend    = 5;
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
        std::_Exit(EXIT_FAILURE);
    }

    if (std::strcmp(argv[1], "--help") == 0) {
        usage(std::cout);
        std::_Exit(EXIT_SUCCESS);
    }

    Input    *input = nullptr;
    UserInput user_input {};

    if (std::strcmp(argv[1], "file") == 0) {
        input      = Input::make_input(InputType::File);
        user_input = input->read(argv[2]);
    }

    if (std::strcmp(argv[1], "standard") == 0) {
        input      = Input::make_input(InputType::Standard);
        user_input = input->read(nullptr);
    }

    if (input == nullptr) {
        usage(std::cerr) << "ERROR: Unknown input type\n";
        std::_Exit(EXIT_FAILURE);
    }

    auto                     output_size = user_input.size();
    gsl::owner<UserOutput *> user_output = new UserOutput[output_size];  // NOLINT
    defer(delete[] user_output);

    run(user_input, user_output, output_size);

    for (decltype(output_size) i = 0; i < output_size; ++i) {
        std::cout << user_output[i].x << "\n";
        std::cout << user_output[i].fy << "\n";
        std::cout << user_output[i].series.sigma << "\n";
        std::cout << user_output[i].series.members << "\n";
        std::cout << user_output[i].abs_error << "\n";
        std::cout << "\n";
    }

    return 0;
}
