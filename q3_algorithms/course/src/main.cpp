#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>

#define GET_INPUT(type, name)                \
    type name;                               \
    std::cout << "Enter " << #name << ":\n"; \
    std::cin >> name

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

    explicit UserInput(double xbegin, double xend, double xstep, double epsilon) :  // NOLINT
        xbegin(xbegin),
        xend(xend),
        xstep(xstep),
        epsilon(epsilon) {
        validate();
    }

    auto size() const { return static_cast<std::size_t>(((xend - xbegin) / xstep) + 1); }

    void validate() const {
        if (xbegin > xend) {
            std::cerr << "ERROR: xbegin must be less or equal to xend\n";
            std::_Exit(EXIT_FAILURE);
        }

        if (xstep <= 0) {
            std::cerr << "ERROR: xstep must be greater than 0\n";
            std::_Exit(EXIT_FAILURE);
        }

        if (epsilon <= 0) {
            std::cerr << "ERROR: epsilon must be greater than 0\n";
            std::_Exit(EXIT_FAILURE);
        }
    }
};

struct UserOutput {
    double       x;
    double       fy;
    SeriesReturn series;
    double       abs_error;
};

static constexpr std::size_t USER_OUTPUT_FIELDS = 5;
// NOLINTNEXTLINE
static const char *USER_OUTPUT_HEADER[USER_OUTPUT_FIELDS] = {
    "x",
    "f(x)",
    "series",
    "members",
    "Δx",  // TODO: fix misaligned table
};

// TODO: possible overflow at invalid input?
void run(const UserInput &input, UserOutput *output, std::size_t size) {
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

    virtual UserInput read(const char *path) const = 0;

    virtual void save(const char *path, UserOutput *output, std::size_t size) const = 0;
};

static constexpr auto CSV_DELIMITER = ",";

class FileInput : public Input {
  public:
    UserInput read(const char *path) const override {
        gsl::owner<std::FILE *> file = std::fopen(path, "r");
        if (file == nullptr) {
            std::cerr << "ERROR: Could not open file\n";
            std::_Exit(EXIT_FAILURE);
        }
        defer(std::fclose(file));  // NOLINT

        // TODO: ask OS for a file size?
        std::fseek(file, 0, SEEK_END);  // NOLINT
        auto last_byte = std::ftell(file);
        std::fseek(file, 0, SEEK_SET);  // NOLINT
        auto file_size = static_cast<std::size_t>(last_byte);

        gsl::owner<char *> content = new char[file_size];  // NOLINT
        if (content == nullptr) {
            std::cerr << "ERROR: Could not allocate memory\n";
            std::_Exit(EXIT_FAILURE);
        }
        defer(delete[] content);

        auto content_size = std::fread(content, 1, file_size, file);
        if (content_size != file_size) {
            std::cerr << "ERROR: Could not read file\n";
            std::_Exit(EXIT_FAILURE);
        }

        // TODO: std::strtok is thread unsafe
        // TODO: extract csv parsing to separate function
        return UserInput {
            std::stod(std::strtok(content, CSV_DELIMITER)),  // NOLINT
            std::stod(std::strtok(nullptr, CSV_DELIMITER)),  // NOLINT
            std::stod(std::strtok(nullptr, CSV_DELIMITER)),  // NOLINT
            std::stod(std::strtok(nullptr, CSV_DELIMITER)),  // NOLINT
        };
    }

    void save(const char *path, UserOutput *output, std::size_t size) const override {
        gsl::owner<std::FILE *> file = std::fopen(path, "w");
        if (file == nullptr) {
            std::cerr << "ERROR: Could not open file\n";
            std::_Exit(EXIT_FAILURE);
        }
        defer(std::fclose(file));  // NOLINT

        if (std::fwrite(output, sizeof(UserOutput), size, file) != size) {
            std::cerr << "ERROR: Could not write to file\n";
            std::_Exit(EXIT_FAILURE);
        }
    }
};

static constexpr auto TABLE_DELIMITER = "  ";

class StandardInput : public Input {
  public:
    UserInput read([[maybe_unused]] const char *path) const override {
        GET_INPUT(double, xbegin);
        GET_INPUT(double, xend);
        GET_INPUT(double, xstep);
        GET_INPUT(double, epsilon);
        return UserInput {xbegin, xend, xstep, epsilon};
    }

    void save([[maybe_unused]] const char *path, UserOutput *output, std::size_t size) const override {
        gsl::owner<int *> widths = new int[USER_OUTPUT_FIELDS];  // NOLINT
        defer(delete[] widths);

        for (std::remove_const<decltype(USER_OUTPUT_FIELDS)>::type i = 0; i < USER_OUTPUT_FIELDS; ++i) {
            widths[i] = std::max(widths[i], static_cast<int>(std::strlen(gsl::at(USER_OUTPUT_HEADER, i))));
        }

        for (decltype(size) i = 0; i < size; ++i) {
            widths[0] = std::max(widths[0], std::snprintf(nullptr, 0, "%g", output[i].x));                // NOLINT
            widths[1] = std::max(widths[1], std::snprintf(nullptr, 0, "%g", output[i].fy));               // NOLINT
            widths[2] = std::max(widths[2], std::snprintf(nullptr, 0, "%g", output[i].series.sigma));     // NOLINT
            widths[3] = std::max(widths[3], std::snprintf(nullptr, 0, "%lu", output[i].series.members));  // NOLINT
            widths[4] = std::max(widths[4], std::snprintf(nullptr, 0, "%g", output[i].abs_error));        // NOLINT
        }

        for (std::remove_const<decltype(USER_OUTPUT_FIELDS)>::type i = 0; i < USER_OUTPUT_FIELDS; ++i) {
            std::cout << std::setw(widths[i]) << gsl::at(USER_OUTPUT_HEADER, i) << TABLE_DELIMITER;
        }
        std::cout << "\n";

        for (decltype(size) i = 0; i < size; ++i) {
            std::cout << std::setw(widths[0]) << output[i].x << TABLE_DELIMITER;
            std::cout << std::setw(widths[1]) << output[i].fy << TABLE_DELIMITER;
            std::cout << std::setw(widths[2]) << output[i].series.sigma << TABLE_DELIMITER;
            std::cout << std::setw(widths[3]) << output[i].series.members << TABLE_DELIMITER;
            std::cout << std::setw(widths[4]) << output[i].abs_error << "\n";
        }
    }
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

    Input      *input       = nullptr;
    const char *input_path  = nullptr;
    const char *output_path = nullptr;

    if (std::strcmp(argv[1], "file") == 0) {
        input       = Input::make_input(InputType::File);
        input_path  = argv[2];
        output_path = argv[3];
    }

    if (std::strcmp(argv[1], "standard") == 0) {
        input = Input::make_input(InputType::Standard);
    }

    if (input == nullptr) {
        usage(std::cerr) << "ERROR: Unknown input type\n";
        std::_Exit(EXIT_FAILURE);
    }

    UserInput user_input = input->read(input_path);

    auto                     output_size = user_input.size();
    gsl::owner<UserOutput *> user_output = new UserOutput[output_size];  // NOLINT
    if (user_output == nullptr) {
        std::cerr << "ERROR: Could not allocate memory\n";
        std::_Exit(EXIT_FAILURE);
    }
    defer(delete[] user_output);

    run(user_input, user_output, output_size);
    input->save(output_path, user_output, output_size);

    return 0;
}
