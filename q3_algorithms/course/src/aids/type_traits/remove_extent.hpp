#ifndef AIDS_TYPE_TRAITS_REMOVE_EXTENT_HPP_
#define AIDS_TYPE_TRAITS_REMOVE_EXTENT_HPP_

#include <cstddef>

namespace aids {
    template<typename T>
    struct remove_extent {
        using type = T;
    };

    template<typename T, std::size_t size>
    struct remove_extent<T[size]> {
        using type = T;
    };

    template<typename T>
    struct remove_extent<T[]> {
        using type = T;
    };

    template<typename T>
    using remove_extent_t = typename remove_extent<T>::type;

    template<typename T>
    struct remove_all_extents {
        using type = T;
    };

    template<typename T, std::size_t size>
    struct remove_all_extents<T[size]> {
        using type = typename remove_all_extents<T>::type;
    };

    template<typename T>
    struct remove_all_extents<T[]> {
        using type = typename remove_all_extents<T>::type;
    };

    template<typename T>
    using remove_all_extents_t = typename remove_all_extents<T>::type;
}  // namespace aids

#endif  // AIDS_TYPE_TRAITS_REMOVE_EXTENT_HPP_
