#ifndef AIDS_UTILITY_EXCHANGE_HPP_
#define AIDS_UTILITY_EXCHANGE_HPP_

#include "src/aids/algorithm/move.hpp"
#include "src/aids/utility/forward.hpp"

namespace aids {
    template<typename T, typename Up = T>
    constexpr T exchange(T& obj, Up&& value) {
        T old = aids::move(obj);
        obj   = aids::forward<Up>(value);
        return old;
    }
}  // namespace aids

#endif  // AIDS_UTILITY_EXCHANGE_HPP_
