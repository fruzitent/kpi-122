#ifndef AIDS_ALGORITHM_COPY_HPP_
#define AIDS_ALGORITHM_COPY_HPP_

#include "src/aids/type_traits/integral_constant.hpp"

namespace aids {
    template<typename In, typename Out, typename Pred>
    Out copy_if(In first, In last, Out dest, Pred pred) {
        while (first != last) {
            if (pred(*first)) {
                *dest = *first;
                ++dest;
            }
            ++first;
        }
        return dest;
    }

    template<typename In, typename Out>
    Out copy(In first, In last, Out dest) {
        return aids::copy_if(first, last, dest, aids::true_type());
    }
}  // namespace aids

#endif  // AIDS_ALGORITHM_COPY_HPP_
