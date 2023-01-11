#ifndef AIDS_MEMORY_ALLOCATOR_HPP_
#define AIDS_MEMORY_ALLOCATOR_HPP_

#include <cstddef>

namespace aids {
    template<typename T>
    struct allocator {
        using value_type = T;
        using pointer    = value_type*;
        using size_type  = std::size_t;

        [[nodiscard]] static constexpr pointer allocate(size_type size) {
            return static_cast<pointer>(::operator new(size * sizeof(value_type)));
        }

        static constexpr void deallocate(pointer ptr, size_type /*size*/) {
            ::operator delete(static_cast<void*>(ptr));
        }
    };
}  // namespace aids

#endif  // AIDS_MEMORY_ALLOCATOR_HPP_
