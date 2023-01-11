#ifndef AIDS_CONCEPTS_SAME_AS_HPP_
#define AIDS_CONCEPTS_SAME_AS_HPP_

#include "src/aids/type_traits/is_same.hpp"

namespace aids {
    template<typename T, typename U>
    concept same_as = aids::is_same_v<T, U> && aids::is_same_v<U, T>;
}

#endif  // AIDS_CONCEPTS_SAME_AS_HPP_
