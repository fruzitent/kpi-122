#include <concepts>
#include <fmt/core.h>
#include <fmt/ostream.h>
#include <iostream>
#include <memory>
#include <vector>

template <template <typename...> typename Base, typename Derived>
struct is_specialization_of {
    template <typename... Ts>
    static constexpr auto test(const Base<Ts...> *) -> std::true_type;
    static constexpr auto test(...) -> std::false_type;
    using type = decltype(test(std::declval<Derived *>())); // NOLINT(*-vararg)
};

template <template <typename...> typename Base, typename Derived>
inline constexpr bool is_specialization_of_v = is_specialization_of<Base, Derived>::type::value;

template <typename Derived, typename T>
class unit {
  protected:
    T _value;

  public:
    explicit constexpr unit(decltype(_value) value = {}) : _value(value) {}

    constexpr unit(const unit &)                     = default;
    constexpr auto operator=(const unit &) -> unit & = default;

    constexpr unit(unit &&) noexcept                     = default;
    constexpr auto operator=(unit &&) noexcept -> unit & = default;

    virtual constexpr ~unit() = default;

    [[nodiscard]] constexpr auto operator()() const noexcept -> decltype(_value) {
        return _value;
    }

    constexpr auto operator()(const decltype(_value) value) noexcept -> void {
        _value = value;
    }

    [[nodiscard]] virtual auto repr() const noexcept -> std::string {
        return fmt::format("{}", _value);
    }
};

template <typename Derived, typename T>
auto operator<<(std::ostream &os, const unit<Derived, T> &value) -> std::ostream & {
    return os << value.repr();
}

template <typename T>
requires is_specialization_of_v<unit, T> //
struct fmt::formatter<T> : public fmt::formatter<fmt::string_view> {
    static auto format(const T &value, fmt::format_context &ctx) -> fmt::appender {
        return fmt::format_to(ctx.out(), "{}", value.repr());
    }
};

struct kg : public unit<kg, double> {
    using unit::unit;

    [[nodiscard]] constexpr auto repr() const noexcept -> std::string override {
        return fmt::format("{} kg", _value);
    }
};

struct kts : public unit<kts, double> {
    using unit::unit;

    [[nodiscard]] constexpr auto repr() const noexcept -> std::string override {
        return fmt::format("{} kts", _value);
    }
};

class Plane {
  protected:
    std::string_view _registration{};
    kts              _ground_speed{};

  public:
    constexpr Plane() = default;

    constexpr Plane(decltype(_registration) registration, decltype(_ground_speed) ground_speed) :
        _registration(registration),
        _ground_speed(std::move(ground_speed)) {}

    constexpr Plane(const Plane &)                     = default;
    constexpr auto operator=(const Plane &) -> Plane & = default;

    constexpr Plane(Plane &&) noexcept                     = default;
    constexpr auto operator=(Plane &&) noexcept -> Plane & = default;

    virtual constexpr ~Plane() = default;

    [[nodiscard]] virtual auto repr() const -> std::string {
        std::string value;
        value += fmt::format("{}\n", _registration);
        value += fmt::format("type: {}\n", typeid(*this).name()); // TODO: clang and gcc need unmangling
        value += fmt::format("ground_speed: {}", _ground_speed);
        return value;
    }
};

auto operator<<(std::ostream &os, const Plane &value) -> std::ostream & {
    return os << value.repr();
}

template <typename T>
requires std::derived_from<T, Plane> //
struct fmt::formatter<T> : public fmt::formatter<fmt::string_view> {
    static auto format(const T &value, fmt::format_context &ctx) -> fmt::appender {
        return fmt::format_to(ctx.out(), "{}", value.repr());
    }
};

class Airliner : public Plane {
  protected:
    std::size_t _passengers{};

  public:
    constexpr Airliner() = default;

    constexpr Airliner(decltype(_registration) registration,
                       decltype(_ground_speed) ground_speed,
                       decltype(_passengers)   passengers) :
        Plane(registration, std::move(ground_speed)),
        _passengers(passengers) {}

    [[nodiscard]] auto repr() const -> std::string override {
        std::string value;
        value += fmt::format("{}\n", Plane::repr());
        value += fmt::format("passengers: {}", _passengers);
        return value;
    }
};

class Bomber : public Plane {
  protected:
    kg _payload{};

  public:
    constexpr Bomber() = default;

    constexpr Bomber(decltype(_registration) registration,
                     decltype(_ground_speed) ground_speed,
                     decltype(_payload)      payload) :
        Plane(registration, std::move(ground_speed)),
        _payload(std::move(payload)) {}

    [[nodiscard]] auto repr() const -> std::string override {
        std::string value;
        value += fmt::format("{}\n", Plane::repr());
        value += fmt::format("payload: {}", _payload);
        return value;
    }
};

auto main() -> int try {
    std::vector<std::shared_ptr<Plane>> planes{
        // NOLINTBEGIN(*-magic-numbers)
        std::make_shared<Airliner>("Boeing 777", kts{135}, 350),
        std::make_shared<Bomber>("B-2", kts{486}, kg{1100}),
        // NOLINTEND(*-magic-numbers)
    };

    for (std::size_t index = 0; const auto &plane : planes) {
        fmt::println("[{:02}]: {}\n", ++index, *plane);
    }

    return EXIT_SUCCESS;
} catch (const std::exception &error) {
    fmt::println(std::cerr, "std::terminate called after throwing an exception:\n");
    fmt::println(std::cerr, "      type: {}", typeid(error).name());
    fmt::println(std::cerr, "    what(): {}", error.what());
    return EXIT_FAILURE;
} catch (...) {
    fmt::println(std::cerr, "std::terminate called after throwing an unknown exception");
    return EXIT_FAILURE;
}
