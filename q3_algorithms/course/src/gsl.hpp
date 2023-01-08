#ifndef GSL_H_
#define GSL_H_

#include <type_traits>

namespace gsl {
    // Reference: https://github.com/microsoft/GSL

    template<typename T>
    requires std::is_pointer_v<T>
    using owner = T;
}  // namespace gsl

#endif  // GSL_H
