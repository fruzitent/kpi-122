#ifndef AIDS_UTILITY_FORWARD_HPP_
#define AIDS_UTILITY_FORWARD_HPP_

#include "src/aids/type_traits/remove_reference.hpp"

namespace aids {
    template<typename T>
    constexpr T&& forward(aids::remove_reference_t<T>& t) noexcept {
        return static_cast<T&&>(t);
    }

    template<typename T>
    constexpr T&& forward(aids::remove_reference_t<T>&& t) noexcept {
        static_assert(!aids::is_lvalue_reference_v<T>);
        return static_cast<T&&>(t);
    }
}  // namespace aids

#endif  // AIDS_UTILITY_FORWARD_HPP_
