#ifndef MODELS_HPP_
#define MODELS_HPP_

#include <cstddef>
#include <cstring>
#include <stdexcept>

#include "src/aids/memory/unique_ptr.hpp"

struct Series {
    double      sigma;
    std::size_t members;
};

struct UserInput {
    double start;
    double stop;
    double step;
    double epsilon;

    constexpr UserInput() :
        start(0),
        stop(0),
        step(0),
        epsilon(0) {}

    constexpr UserInput(double start_, double stop_, double step_, double epsilon_) :
        start(start_),
        stop(stop_),
        step(step_),
        epsilon(epsilon_) {
        validate();
    }

    [[nodiscard]] constexpr std::size_t size() const { return static_cast<std::size_t>((stop - start) / step); }

    constexpr void validate() const {
        if (start >= stop) {
            throw std::invalid_argument("Start must be less than stop");
        }

        if (step <= 0) {
            throw std::invalid_argument("Step must be greater than 0");
        }

        if (epsilon <= 0) {
            throw std::invalid_argument("Epsilon must be greater than 0");
        }
    }
};

struct UserOutput {
    double x;
    double y;
    Series series;

    [[nodiscard]] double abs_error() const { return std::abs(y - series.sigma); }

    static constexpr int         COLUMNS         = 5;
    static constexpr const char* HEADER[COLUMNS] = {
        "x",
        "y",
        "sigma",
        "members",
        "abs_error",
    };

    static constexpr const char* DELIMITER = "  ";

    static void print(std::FILE* stream, UserOutput* output, const std::size_t& size) {
        auto widths = aids::make_unique<std::size_t[]>(std::size_t(COLUMNS));

        for (auto i = 0; i < COLUMNS; ++i) {
            widths[i] = std::max(widths[i], std::strlen(HEADER[i]));
        }

        for (auto i = 0; i < static_cast<int>(size); ++i) {
            // clang-format off
            widths[0] = std::max(widths[0], static_cast<std::size_t>(std::snprintf(nullptr, 0, "%g", output[i].x)));
            widths[1] = std::max(widths[1], static_cast<std::size_t>(std::snprintf(nullptr, 0, "%g", output[i].y)));
            widths[2] = std::max(widths[2], static_cast<std::size_t>(std::snprintf(nullptr, 0, "%g", output[i].series.sigma)));
            widths[3] = std::max(widths[3], static_cast<std::size_t>(std::snprintf(nullptr, 0, "%zu", output[i].series.members)));
            widths[4] = std::max(widths[4], static_cast<std::size_t>(std::snprintf(nullptr, 0, "%g", output[i].abs_error())));
            // clang-format on
        }

        for (auto i = 0; i < COLUMNS; ++i) {
            std::fprintf(stream, "%*s%s", static_cast<int>(widths[i]), HEADER[i], DELIMITER);
        }
        std::fprintf(stream, "\n");

        for (auto i = 0; i < static_cast<int>(size); ++i) {
            std::fprintf(stream, "%*g%s", static_cast<int>(widths[0]), output[i].x, DELIMITER);
            std::fprintf(stream, "%*g%s", static_cast<int>(widths[1]), output[i].y, DELIMITER);
            std::fprintf(stream, "%*g%s", static_cast<int>(widths[2]), output[i].series.sigma, DELIMITER);
            std::fprintf(stream, "%*zu%s", static_cast<int>(widths[3]), output[i].series.members, DELIMITER);
            std::fprintf(stream, "%*g\n", static_cast<int>(widths[4]), output[i].abs_error());
        }
    }
};

#endif  // MODELS_HPP
