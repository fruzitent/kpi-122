#ifndef AIDS_ALGORITHM_SWAP_HPP_
#define AIDS_ALGORITHM_SWAP_HPP_

#include <cstddef>

#include "src/aids/algorithm/move.hpp"

namespace aids {
    template<typename T>
    constexpr void swap(T& lhs, T& rhs) {
        T tmp = aids::move(lhs);
        lhs   = aids::move(rhs);
        rhs   = aids::move(tmp);
    }

    template<typename T, std::size_t size>
    constexpr void swap(T (&lhs)[size], T (&rhs)[size]) {
        for (std::size_t i = 0; i < size; ++i) {
            aids::swap(lhs[i], rhs[i]);
        }
    }
}  // namespace aids

#endif  // AIDS_ALGORITHM_SWAP_HPP_
