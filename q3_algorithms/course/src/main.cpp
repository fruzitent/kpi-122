#include <cmath>
#include <cstring>
#include <iostream>
#include <memory>

#include "src/aids.hpp"
#include "src/io.hpp"

auto get_series(double x, double abs_error, double epsilon) {
    SeriesReturn series {
        .sigma   = 0,
        .members = 2,
    };

    while (std::abs(abs_error) > epsilon) {
        series.sigma += abs_error;
        abs_error *= -std::pow(x, 2) / (static_cast<double>(series.members) * 2);
        ++series.members;
    }

    return series;
}

double get_function(double x) {
    if (x == 0) {
        return 0;
    }
    return (1 - std::exp(-std::pow(x, 2) / 2)) / x;
}

void run(const UserInput &input, UserOutput *output, std::size_t size) {
    for (decltype(size) i = 0; i < size; ++i) {
        const double x = input.xbegin + static_cast<double>(i) * input.xstep;

        if (x == 0) {
            continue;
        }

        auto fy        = get_function(x);
        auto series    = get_series(x, x / 2, input.epsilon);
        auto abs_error = std::abs(fy - series.sigma);
        output[i]      = UserOutput {x, fy, series, abs_error};
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

void loop([[maybe_unused]] int argc, char **argv) {
    if (argc < 2) {
        throw std::invalid_argument("Not enough arguments. Run `./main --help` to see avaliable options");
    }

    if (std::strcmp(argv[1], "--help") == 0) {
        usage(std::cout);
        return;
    }

    auto input = std::unique_ptr<Input>(nullptr);

    const char *input_path  = nullptr;
    const char *output_path = nullptr;

    if (std::strcmp(argv[1], "file") == 0) {
        input.reset(Input::make_input(InputType::File));
        input_path  = argv[2];
        output_path = argv[3];
    }

    if (std::strcmp(argv[1], "standard") == 0) {
        input.reset(Input::make_input(InputType::Standard));
    }

    if (input == nullptr) {
        throw std::invalid_argument("Unknown input type");
    }

    const UserInput user_input = input->read(input_path);

    auto output_size = user_input.size();
    auto user_output = std::unique_ptr<UserOutput[]>(new UserOutput[output_size] {});

    run(user_input, user_output.get(), output_size);
    input->save(output_path, user_output.get(), output_size);
}

int main(int argc, char **argv) {
    try {
        loop(argc, argv);
        return 0;
    } catch (const std::exception &error) {
        std::cerr << "ERROR: " << error.what() << "\n";
        return 1;
    }
}
