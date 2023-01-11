#ifndef AIDS_ALGORITHM_FILL_HPP_
#define AIDS_ALGORITHM_FILL_HPP_

namespace aids {
    template<typename Out, typename Size, typename U>
    Out fill_n(Out dest, Size size, const U& value) {
        while (size) {
            *dest = value;
            ++dest;
            --size;
        }
        return dest;
    }
}  // namespace aids

#endif  // AIDS_ALGORITHM_FILL_HPP_
