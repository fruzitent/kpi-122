#ifndef AIDS_ARRAY_HPP_
#define AIDS_ARRAY_HPP_

#include <cstddef>
#include <stdexcept>

#include "src/aids/algorithm/fill.hpp"
#include "src/aids/memory/unique_ptr.hpp"

namespace aids {
    template<typename T, std::size_t N>
    class array {
      public:
        using value_type      = T;
        using pointer         = value_type*;
        using const_pointer   = const pointer*;
        using reference       = value_type&;
        using const_reference = const value_type&;
        using size_type       = std::size_t;
        using iterator        = T*;
        using const_iterator  = const T*;

      private:
        aids::unique_ptr<T[N]> _buffer;
        size_type              _size;

      public:
        constexpr const_reference at(size_type index) const {
            if (index >= _size) {
                throw std::out_of_range("Out of Range\n");
            }
            return _buffer[index];
        }

        constexpr const_reference operator[](size_type index) const { return _buffer[index]; }

        constexpr const_pointer data() const noexcept { return _buffer; }

        constexpr const_iterator begin() const noexcept { return &_buffer[0]; }

        constexpr const_iterator end() const noexcept { return &_buffer[size()]; }

        [[nodiscard]] static constexpr size_type size() noexcept { return N; }

        constexpr void swap(array& other) noexcept { aids::swap(_buffer, other._buffer); }

        constexpr void fill(const value_type& value) const { aids::fill_n(begin(), size(), value); }
    };
}  // namespace aids

#endif  // AIDS_ARRAY_HPP_
