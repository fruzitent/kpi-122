#ifndef IO_H_
#define IO_H_

#include <cstring>
#include <iomanip>
#include <memory>

#include "src/aids.hpp"
#include "src/models.hpp"

template<typename T>
static constexpr T get_stdin(const char *name) {
    T value;
    std::cout << "Enter " << name << ":\n";
    std::cin >> value;
    return value;
}

enum class InputType {
    File,
    Standard,
};

class Input {
  public:
    Input()          = default;
    virtual ~Input() = default;

    Input(const Input &)            = default;
    Input &operator=(const Input &) = default;

    Input(Input &&) noexcept            = default;
    Input &operator=(Input &&) noexcept = default;

    static Input *make_input(InputType type);

    virtual UserInput read(const char *path) const = 0;

    virtual void save(const char *path, UserOutput *output, std::size_t size) const = 0;
};

static constexpr auto CSV_DELIMITER = ",";

class FileInput : public Input {
  public:
    UserInput read(const char *path) const override {
        auto file = std::unique_ptr<std::FILE, aids::default_delete<std::FILE *>>(
            std::fopen(path, "r"), aids::default_delete<std::FILE *>()
        );
        if (file == nullptr) {
            throw std::ios_base::failure("Could not open file");
        }

        std::fseek(file.get(), 0, SEEK_END);  // NOLINT
        auto last_byte = std::ftell(file.get());
        std::fseek(file.get(), 0, SEEK_SET);  // NOLINT
        auto file_size = static_cast<std::size_t>(last_byte);

        auto content      = std::unique_ptr<char[]>(new char[file_size]);
        auto content_size = std::fread(content.get(), 1, file_size, file.get());
        if (content_size != file_size) {
            throw std::ios_base::failure("Could not read file");
        }

        return UserInput {
            std::stod(std::strtok(content.get(), CSV_DELIMITER)),  // NOLINT
            std::stod(std::strtok(nullptr, CSV_DELIMITER)),        // NOLINT
            std::stod(std::strtok(nullptr, CSV_DELIMITER)),        // NOLINT
            std::stod(std::strtok(nullptr, CSV_DELIMITER)),        // NOLINT
        };
    }

    void save(const char *path, UserOutput *output, std::size_t size) const override {
        auto file = std::unique_ptr<std::FILE, aids::default_delete<std::FILE *>>(
            std::fopen(path, "w"), aids::default_delete<std::FILE *>()
        );
        if (file == nullptr) {
            throw std::ios_base::failure("Could not open file");
        }

        if (std::fwrite(output, sizeof(UserOutput), size, file.get()) != size) {
            throw std::ios_base::failure("Could not write to file");
        }
    }
};

static constexpr auto TABLE_DELIMITER = "  ";

class StandardInput : public Input {
  public:
    UserInput read(const char * /*path*/) const override {
        auto xbegin  = get_stdin<double>("xbegin");
        auto xend    = get_stdin<double>("xend");
        auto xstep   = get_stdin<double>("xstep");
        auto epsilon = get_stdin<double>("epsilon");
        return UserInput {xbegin, xend, xstep, epsilon};
    }

    void save(const char * /*path*/, UserOutput *output, std::size_t size) const override {
        auto widths = std::unique_ptr<int[]>(new int[USER_OUTPUT_FIELDS]);

        for (std::size_t i = 0; i < USER_OUTPUT_FIELDS; ++i) {
            widths[i] = std::max(widths[i], static_cast<int>(std::strlen(USER_OUTPUT_HEADER[i])));  // NOLINT
        }

        for (std::size_t i = 0; i < size; ++i) {
            widths[0] = std::max(widths[0], std::snprintf(nullptr, 0, "%g", output[i].x));
            widths[1] = std::max(widths[1], std::snprintf(nullptr, 0, "%g", output[i].fy));
            widths[2] = std::max(widths[2], std::snprintf(nullptr, 0, "%g", output[i].series.sigma));
            widths[3] = std::max(widths[3], std::snprintf(nullptr, 0, "%zu", output[i].series.members));
            widths[4] = std::max(widths[4], std::snprintf(nullptr, 0, "%g", output[i].abs_error));
        }

        for (std::remove_const<decltype(USER_OUTPUT_FIELDS)>::type i = 0; i < USER_OUTPUT_FIELDS; ++i) {
            std::cout << std::setw(widths[i]) << USER_OUTPUT_HEADER[i] << TABLE_DELIMITER;  // NOLINT
        }
        std::cout << "\n";

        for (std::size_t i = 0; i < size; ++i) {
            std::cout << std::setw(widths[0]) << output[i].x << TABLE_DELIMITER;
            std::cout << std::setw(widths[1]) << output[i].fy << TABLE_DELIMITER;
            std::cout << std::setw(widths[2]) << output[i].series.sigma << TABLE_DELIMITER;
            std::cout << std::setw(widths[3]) << output[i].series.members << TABLE_DELIMITER;
            std::cout << std::setw(widths[4]) << output[i].abs_error << "\n";
        }
    }
};

inline Input *Input::make_input(InputType type) {
    switch (type) {
        case InputType::File:
            return new FileInput();
        case InputType::Standard:
            return new StandardInput();
        default:
            return nullptr;
    }
}

#endif  // IO_H_
