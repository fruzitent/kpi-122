#ifndef EXECUTOR_HPP_
#define EXECUTOR_HPP_

#include <cmath>

#include "src/models.hpp"

inline auto get_series(double x, double abs_error, double epsilon) {
    Series series {
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

inline double get_function(double x) {
    if (x == 0) {
        return 0;
    }
    return (1 - std::exp(-std::pow(x, 2) / 2)) / x;
}

inline UserOutput tick(double x, double epsilon) {
    return (x == 0) ? UserOutput {}
                    : UserOutput {
                        .x      = x,
                        .y      = get_function(x),
                        .series = get_series(x, x / 2, epsilon),
                    };
}

inline void execute(const UserInput& input, const std::size_t size, UserOutput* output) {
    for (std::size_t i = 0; i < size; ++i) {
        double x  = input.start + input.step * static_cast<double>(i);
        output[i] = tick(x, input.epsilon);
    }
}

#endif  // EXECUTOR_HPP_
