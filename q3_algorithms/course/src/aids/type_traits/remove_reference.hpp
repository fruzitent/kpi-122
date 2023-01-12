#ifndef AIDS_TYPE_TRAITS_REMOVE_REFERENCE_HPP_
#define AIDS_TYPE_TRAITS_REMOVE_REFERENCE_HPP_

#include "src/aids/type_traits/integral_constant.hpp"

namespace aids {
    template<typename T>
    struct remove_reference {
        using type = T;
    };

    template<typename T>
    struct remove_reference<T&> {
        using type = T;
    };

    template<typename T>
    struct remove_reference<T&&> {
        using type = T;
    };

    template<typename T>
    using remove_reference_t = typename remove_reference<T>::type;

    template<typename T>
    struct is_lvalue_reference : public aids::false_type {};

    template<typename T>
    struct is_lvalue_reference<T&> : public aids::true_type {};

    template<typename T>
    constexpr bool is_lvalue_reference_v = is_lvalue_reference<T>::value;

    template<typename T>
    struct is_rvalue_reference : public aids::false_type {};

    template<typename T>
    struct is_rvalue_reference<T&&> : public aids::true_type {};

    template<typename T>
    constexpr bool is_rvalue_reference_v = is_rvalue_reference<T>::value;
}  // namespace aids

#endif  // AIDS_TYPE_TRAITS_REMOVE_REFERENCE_HPP_
