#include "src/aids.hpp"
#include "src/executor.hpp"
#include "src/flag.hpp"
#include "src/io.hpp"
#include "src/models.hpp"

namespace csv {
    static UserInput parse(char(buffer)[]) {
        return UserInput {
            std::strtod(std::strtok(buffer, ","), nullptr),   // NOLINT
            std::strtod(std::strtok(nullptr, ","), nullptr),  // NOLINT
            std::strtod(std::strtok(nullptr, ","), nullptr),  // NOLINT
            std::strtod(std::strtok(nullptr, ","), nullptr),  // NOLINT
        };
    }
}  // namespace csv

enum class Mode {
    File,
    Standard,
};

int main(int argc, char** argv) try {
    const auto* inp_path = flag::CStr("i", "", "Input filepath");
    const auto* out_path = flag::CStr("o", "", "Output filepath");
    flag::parse(argc, argv);

    Mode      mode = std::strlen(*inp_path) == 0 && std::strlen(*out_path) == 0 ? Mode::Standard : Mode::File;
    UserInput user_input {};

    switch (mode) {
        case Mode::File: {
            user_input = csv::parse(io::read(*inp_path).get());
            break;
        }

        case Mode::Standard: {
            user_input = UserInput {
                io::get_input<double>("Start:\n"),
                io::get_input<double>("Stop:\n"),
                io::get_input<double>("Step:\n"),
                io::get_input<double>("Epsilon:\n"),
            };
            break;
        }

        default: {
            throw std::runtime_error("Unreachable\n");
        }
    }

    auto user_output = aids::make_unique<UserOutput[]>(user_input.size());
    execute(user_input, user_input.size(), user_output.get());

    switch (mode) {
        case Mode::File: {
            auto out_file = aids::make_unique<std::FILE*>(std::fopen(*out_path, "wb"));  // NOLINT
            if (*out_file == nullptr) {
                throw std::runtime_error("Could not open file\n");
            }

            user_output->print(*out_file, user_output.get(), user_input.size());
            break;
        }

        case Mode::Standard: {
            user_output->print(stdout, user_output.get(), user_input.size());
            break;
        }
    }
} catch (const std::exception& error) {
    std::cerr << "ERROR: " << error.what();
    return 1;
}
