#ifndef AIDS_TYPE_TRAITS_IS_SAME_HPP_
#define AIDS_TYPE_TRAITS_IS_SAME_HPP_

#include "src/aids/type_traits/integral_constant.hpp"

namespace aids {
    template<typename T, typename U>
    struct is_same : aids::false_type {};

    template<typename T>
    struct is_same<T, T> : aids::true_type {};

    template<typename T, typename U>
    constexpr bool is_same_v = is_same<T, U>::value;
}  // namespace aids

#endif  // AIDS_TYPE_TRAITS_IS_SAME_HPP_
