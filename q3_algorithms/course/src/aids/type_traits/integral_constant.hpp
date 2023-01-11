#ifndef AIDS_TYPE_TRAITS_INTEGRAL_CONSTANT_HPP_
#define AIDS_TYPE_TRAITS_INTEGRAL_CONSTANT_HPP_

namespace aids {
    template<typename T, T v>
    struct integral_constant {
        using value_type = T;
        using type       = integral_constant;

        static constexpr T value = v;

        explicit constexpr operator value_type() const noexcept { return value; }

        constexpr value_type operator()() const noexcept { return value; }
    };

    template<bool B>
    using bool_constant = integral_constant<bool, B>;
    using false_type    = bool_constant<false>;
    using true_type     = bool_constant<true>;
}  // namespace aids

#endif  // AIDS_TYPE_TRAITS_INTEGRAL_CONSTANT_HPP_
