#include <array>
#include <fmt/core.h>
#include <fmt/ostream.h>
#include <iostream>
#include <numeric>
#include <vector>

template <typename... Args>
class Polynomial {
  public:
    using value_type = double;
    using size_type  = std::size_t;

  protected:
    static constexpr size_type   size = sizeof...(Args);
    std::array<value_type, size> _coefficients;

  private:
    struct Extrema {
        std::vector<value_type> maxima;
        std::vector<value_type> minima;
    };

    struct Range {
        value_type from;
        value_type upto;
        value_type step;
    };

  public:
    explicit constexpr Polynomial(Args &&...args) noexcept : _coefficients{std::forward<Args>(args)...} {}

    [[nodiscard]] constexpr auto coefficient(size_type index) const noexcept -> value_type {
        return _coefficients.at(index);
    }

    [[nodiscard]] constexpr auto degree() const noexcept -> size_type {
        return _coefficients.size() - 1;
    }

    [[nodiscard]] auto repr() const noexcept -> std::string {
        std::string text;

        auto power = degree();
        for (const auto &value : _coefficients) {
            if (value == 0) {
                --power;
                continue;
            }

            if (!text.empty()) {
                text += value > 0 ? " + " : " - ";
            } else if (value < 0) {
                text += "-";
            }

            if (std::abs(value) != 1 || power == 0) {
                text += fmt::format("{}", std::abs(value));
            }

            if (power > 0) {
                if (power == 1) {
                    text += "x";
                } else {
                    text += fmt::format("x^{}", power);
                }
            }

            --power;
        }

        return text;
    }

    constexpr auto operator/(const Polynomial &other) const noexcept -> bool {
        if (degree() != other.degree()) {
            return false;
        }

        for (size_type i = 0; i < degree(); ++i) {
            const auto lhs = _coefficients.at(i);
            const auto rhs = other._coefficients.at(i);

            if (lhs != 0 && rhs != 0) {
                if (lhs < 0 && rhs > 0) {
                    return true;
                }
                if (lhs > 0 && rhs < 0) {
                    return true;
                }
            }
        }

        return false;
    }

    constexpr auto operator||(const Polynomial &other) const noexcept -> bool {
        if (degree() != other.degree()) {
            return false;
        }

        for (size_type i = 0; i < degree(); ++i) {
            if (_coefficients.at(i) != other._coefficients.at(i)) {
                return false;
            }
        }

        return true;
    }

    [[nodiscard]] constexpr auto derivative(value_type x, // NOLINT(misc-no-recursion)
                                            value_type error,
                                            size_type  order) const noexcept -> value_type {
        // Reference: https://en.wikipedia.org/wiki/Finite_difference

        if (order == 0) {
            return execute(x);
        }

        if (order > degree()) {
            return 0;
        }

        const auto prev = derivative(x + error, error, order - 1);
        const auto next = derivative(x - error, error, order - 1);
        return (prev - next) / (2 * error);
    }

    [[nodiscard]] constexpr auto execute(value_type x) const noexcept -> value_type {
        return std::accumulate(_coefficients.begin(), _coefficients.end(), 0.0, [x](auto acc, auto coeff) {
            return acc * x + coeff;
        });
    }

    [[nodiscard]] constexpr auto extrema(Range range, value_type error) const noexcept -> Extrema {
        Extrema result;

        for (auto i = 0; i <= (range.upto - range.from) / range.step; ++i) {
            const auto x   = range.from + i * range.step;
            const auto d1y = derivative(x, error, 1);
            const auto d2y = derivative(x, error, 2);

            if (d1y == 0) {
                if (d2y < 0) {
                    result.maxima.push_back(x);
                } else if (d2y > 0) {
                    result.minima.push_back(x);
                }
            }
        }

        return result;
    }
};

template <typename... Args>
auto operator<<(std::ostream &os, const Polynomial<Args...> &poly) -> std::ostream & {
    return os << poly.repr();
}

template <typename... Args>
struct fmt::formatter<Polynomial<Args...>> : public fmt::formatter<fmt::string_view> {
    auto format(const Polynomial<Args...> &value, fmt::format_context &ctx) -> fmt::appender {
        return fmt::format_to(ctx.out(), "{}", value.repr());
    }
};

auto main() -> int {
    constexpr Polynomial poly0{1.0, 4.0, -6.0};
    constexpr Polynomial poly1(-1.0, -6.0, 3.0);

    fmt::println("Poly #0: {}", poly0);
    fmt::println("Poly #1: {}", poly1);

    fmt::println("Cross: {}", poly0 / poly1);
    fmt::println("Match: {}", poly0 || poly1);

    constexpr auto from  = -5.0;
    constexpr auto upto  = 5.0;
    constexpr auto step  = 0.5;
    constexpr auto error = 1e-6;

    // TODO: calculate widths
    fmt::println("{:>8} | {:>8} | {:>8} | {:>8} | {:>8}", "x", "y", "d1y", "d2y", "d3y");
    for (auto i = 0; i <= (upto - from) / step; ++i) {
        const auto x   = from + i * step;
        const auto y   = poly0.execute(x);
        const auto d1y = poly0.derivative(x, error, 1);
        const auto d2y = poly0.derivative(x, error, 2);
        const auto d3y = poly0.derivative(x, error, 3);
        fmt::println("{:>8.4} | {:>8.4} | {:>8.4} | {:>8.4} | {:>8.4}", x, y, d1y, d2y, d3y);
    }

    const auto extrema = poly0.extrema({from, upto, step}, error);

    for (const auto &value : extrema.maxima) {
        fmt::println("maxima: {:.4}", value);
    }

    for (const auto &value : extrema.minima) {
        fmt::println("minima: {:.4}", value);
    }
}
