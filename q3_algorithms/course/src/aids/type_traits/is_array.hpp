#ifndef AIDS_TYPE_TRAITS_IS_ARRAY_HPP_
#define AIDS_TYPE_TRAITS_IS_ARRAY_HPP_

#include <cstddef>

#include "src/aids/type_traits/integral_constant.hpp"

namespace aids {
    template<typename T>
    struct is_array : public aids::false_type {};

    template<typename T, std::size_t size>
    struct is_array<T[size]> : public aids::true_type {};

    template<typename T>
    struct is_array<T[]> : public aids::true_type {};

    template<typename T>
    constexpr bool is_array_v = is_array<T>::value;
}  // namespace aids

#endif  // AIDS_TYPE_TRAITS_IS_ARRAY_HPP_
