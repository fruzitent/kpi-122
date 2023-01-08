#ifndef MODELS_H_
#define MODELS_H_

#include <iostream>

struct SeriesReturn {
    double      sigma;
    std::size_t members;
};

struct UserInput {
    double xbegin;
    double xend;
    double xstep;
    double epsilon;

    explicit UserInput(double xbegin_, double xend_, double xstep_, double epsilon_) :
        xbegin(xbegin_),
        xend(xend_),
        xstep(xstep_),
        epsilon(epsilon_) {
        validate();
    }

    [[nodiscard]] auto size() const { return static_cast<std::size_t>(((xend - xbegin) / xstep) + 1); }

    void validate() const {
        if (xbegin > xend) {
            throw std::invalid_argument("ERROR: xbegin must be less or equal to xend");
        }

        if (xstep <= 0) {
            throw std::invalid_argument("ERROR: xstep must be greater than 0");
        }

        if (epsilon <= 0) {
            throw std::invalid_argument("ERROR: epsilon must be greater than 0");
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
    "Δx",
};

#endif  // MODELS_H
