#ifndef AIDS_ALGORITHM_MOVE_HPP_
#define AIDS_ALGORITHM_MOVE_HPP_

#include "src/aids/type_traits/remove_reference.hpp"

namespace aids {
    template<typename T>
    constexpr aids::remove_reference_t<T>&& move(T&& obj) noexcept {
        return static_cast<aids::remove_reference_t<T>&&>(obj);
    }
}  // namespace aids

#endif  // AIDS_ALGORITHM_MOVE_HPP_
