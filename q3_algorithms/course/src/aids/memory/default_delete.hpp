#ifndef AIDS_MEMORY_DEFAULT_DELETE_HPP_
#define AIDS_MEMORY_DEFAULT_DELETE_HPP_

#include <stdexcept>

namespace aids {
    template<typename T>
    struct default_delete {
        constexpr void operator()(T* pointer) const {
            delete pointer;  // NOLINT
        }
    };

    template<typename T>
    struct default_delete<T[]> {
        constexpr void operator()(T* array) const {
            delete[] array;  // NOLINT
        }
    };

    template<>
    struct default_delete<std::FILE> {
        void operator()(std::FILE* file) const {
            if (std::fclose(file) < 0) {  // NOLINT
                throw std::runtime_error("Could not close file\n");
            }
        }
    };
}  // namespace aids

#endif  // AIDS_MEMORY_DEFAULT_DELETE_HPP_
