#ifndef MYPROJECT_THROW_EXCEPTION_HPP_
#define MYPROJECT_THROW_EXCEPTION_HPP_

#include <source_location>
#include <type_traits>
#include <utility>

namespace myproject {
    class throw_location {
      protected:
        std::source_location _location;

      public:
        explicit constexpr throw_location(std::source_location location) noexcept : _location(location) {}

        [[nodiscard]] constexpr auto location() const noexcept -> std::source_location {
            return _location;
        }
    };

    template <typename Error>
    class with_throw_location : public Error, public throw_location {
      public:
        constexpr with_throw_location(const Error &error, const std::source_location &location) :
            Error(error),
            throw_location(location) {}

        constexpr with_throw_location(Error &&error, const std::source_location &location) :
            Error(std::move(error)),
            throw_location(location) {}
    };

    template <typename Error>
    [[noreturn]] inline constexpr auto
    throw_with_location(Error &&error, const std::source_location &location = std::source_location::current()) -> void {
        throw with_throw_location(std::decay_t<Error>(std::forward<Error>(error)), location);
    }

    template <typename Error>
    constexpr auto get_throw_location(const Error &error) -> std::source_location {
        if (const auto *exception = dynamic_cast<const throw_location *>(&error)) {
            return exception->location();
        }
        return {};
    }
} // namespace myproject

#endif // MYPROJECT_THROW_EXCEPTION_HPP_
