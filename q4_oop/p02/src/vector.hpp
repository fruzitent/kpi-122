#ifndef MYPROJECT_VECTOR_HPP_
#define MYPROJECT_VECTOR_HPP_

#include <algorithm>
#include <initializer_list>
#include <iterator>
#include <limits>
#include <memory>
#include <stdexcept>
#include <type_traits>
#include <utility>
#include <variant>

#ifdef _MSC_VER
#define myproject_no_unique_address [[msvc::no_unique_address]]
#else
#define myproject_no_unique_address [[no_unique_address]]
#endif

namespace myproject {
    template <typename Contained, typename Allocator = std::allocator<Contained>>
    class vector {
      public:
        using value_type       = Contained;
        using allocator_type   = Allocator;
        using allocator_traits = std::allocator_traits<allocator_type>;

        using pointer         = typename allocator_traits::pointer;
        using const_pointer   = typename allocator_traits::const_pointer;
        using reference       = value_type &;
        using const_reference = const value_type &;

        // TODO: wrap_iter https://quuxplusone.github.io/blog/2022/03/03/why-isnt-vector-iterator-just-t-star
        using iterator               = value_type *;
        using const_iterator         = const value_type *;
        using reverse_iterator       = std::reverse_iterator<iterator>;
        using const_reverse_iterator = std::reverse_iterator<const_iterator>;

        using difference_type = typename allocator_traits::difference_type;
        using size_type       = typename allocator_traits::size_type;

        static_assert(std::is_same_v<allocator_type, typename allocator_traits::template rebind_alloc<value_type>>);
        static_assert(std::is_same_v<value_type, std::remove_cv_t<value_type>>);
        static_assert(std::is_same_v<value_type, typename allocator_type::value_type>);

      protected:
        myproject_no_unique_address allocator_type _allocator;

        pointer _begin;
        pointer _end;
        pointer _capacity;

      private:
        constexpr auto _adopt_allocations_of(vector &other) noexcept -> void {
            _begin    = std::exchange(other._begin, nullptr);
            _end      = std::exchange(other._end, nullptr);
            _capacity = std::exchange(other._capacity, nullptr);
        }

        constexpr auto _allocate(size_type size) -> void {
            if (size > max_size()) {
                throw std::length_error("");
            }

            _begin    = allocator_traits::allocate(_allocator, size);
            _end      = _begin;
            _capacity = _begin + size;
        }

        constexpr auto _deallocate() noexcept -> void {
            if (_begin != nullptr) {
                allocator_traits::deallocate(_allocator, _begin, capacity());
                _begin    = pointer{};
                _end      = pointer{};
                _capacity = pointer{};
            }
        }

        struct _constructor {      // NOLINT(*-special-member-functions)
            vector       &_vector; // NOLINT(cppcoreguidelines-avoid-const-or-ref-data-members)
            pointer       _old_end;
            const_pointer _new_end;

            explicit constexpr _constructor(vector &vector, size_type size) :
                _vector(vector),
                _old_end(vector._end),
                _new_end(vector._end + size) {}

            constexpr _constructor(const _constructor &)                     = delete;
            constexpr auto operator=(const _constructor &) -> _constructor & = delete;

            constexpr ~_constructor() noexcept {
                _vector._end = _old_end;
            }
        };

        constexpr auto _construct_one_at_end(auto &&...args) -> void {
            _constructor guard(*this, 1);
            allocator_traits::construct(_allocator,
                                        std::to_address(guard._old_end),
                                        std::forward<decltype(args)>(args)...);
            ++guard._old_end;
        }

        constexpr auto _construct_at_end(size_type size, const_reference value = {}) -> void {
            _constructor guard(*this, size);
            while (guard._old_end != guard._new_end) {
                allocator_traits::construct(_allocator, std::to_address(guard._old_end), value);
                ++guard._old_end;
            }
        }

        template <std::input_iterator Iterator>
        constexpr auto _construct_at_end(Iterator first, Iterator last, size_type size) -> void {
            _constructor guard(*this, size);
            guard._old_end = std::uninitialized_copy(first, last, guard._old_end);
        }

        constexpr auto _destruct_at_end(pointer new_end) noexcept -> void {
            pointer old_end = _end;
            while (old_end != new_end) {
                --old_end;
                allocator_traits::destroy(_allocator, std::to_address(old_end));
            }
            _end = new_end;
        }

        constexpr auto _emplace_back(auto &&...args) -> void {
            reserve(_recommend(size() + 1));
            allocator_traits::construct(_allocator, std::to_address(_end), std::forward<decltype(args)>(args)...);
            ++_end;
        }

        constexpr auto _push_back(auto &&value) -> void {
            reserve(_recommend(size() + 1));
            allocator_traits::construct(_allocator, std::to_address(_end), std::forward<decltype(value)>(value));
            ++_end;
        }

        constexpr auto _recommend(size_type size) const -> size_type {
            if (size > max_size()) {
                throw std::length_error("");
            }

            if (size <= capacity()) {
                return capacity();
            }

            return std::max<size_type>(size, capacity() * 2);
        }

      public:
        explicit constexpr vector(const allocator_type &allocator = {}) noexcept(
            std::is_nothrow_default_constructible_v<allocator_type>) :
            _allocator(allocator),
            _begin(pointer{}),
            _end(pointer{}),
            _capacity(pointer{}) {}

        explicit constexpr vector(size_type size, const allocator_type &allocator = {}) : vector(allocator) {
            _allocate(size);
            _construct_at_end(size);
        }

        explicit constexpr vector(size_type size, const_reference value, const allocator_type &allocator = {}) :
            vector(allocator) {
            _allocate(size);
            _construct_at_end(size, value);
        }

        constexpr vector(std::forward_iterator auto first,
                         std::forward_iterator auto last,
                         const allocator_type      &allocator = {}) :
            vector(allocator) {
            for (; first != last; ++first) {
                emplace_back(*first);
            }
        }

        constexpr vector(std::input_iterator auto first,
                         std::input_iterator auto last,
                         const allocator_type    &allocator = {}) :
            vector(allocator) {
            auto dist = static_cast<size_type>(std::distance(first, last));
            _allocate(dist);
            _construct_at_end(first, last, dist);
        }

        constexpr vector(std::initializer_list<value_type> list); // cppcheck-suppress noExplicitConstructor
        constexpr vector(std::initializer_list<value_type> list, const allocator_type &allocator);
        constexpr auto operator=(std::initializer_list<value_type> list) -> vector &;

        constexpr vector(const vector &other) : // noexcept(std::is_nothrow_copy_constructible_v<allocator_type>) :
            vector(allocator_traits::select_on_container_copy_construction(other._allocator)) {
            _allocate(other.size());
            _construct_at_end(other._begin, other._end, other.size());
        }

        constexpr auto operator=(const vector &other) noexcept(std::is_nothrow_copy_assignable_v<allocator_type>)
            -> vector & {
            if (this == std::addressof(other)) {
                return *this;
            }

            if (allocator_traits::propagate_on_container_copy_assignment::value) {
                if (_allocator != other._allocator) {
                    _deallocate();
                }
                _allocator = other._allocator;
            }

            assign(other._begin, other._end);
            return *this;
        }

        constexpr vector(vector &&other) noexcept(std::is_nothrow_move_constructible_v<allocator_type>) :
            vector(std::move(other._allocator)) {
            if (_allocator == other._allocator) {
                _adopt_allocations_of(other);
            } else {
                assign(other._begin, other._end);
                other.clear();
            }
        }

        constexpr auto operator=(vector &&other) noexcept(std::is_nothrow_move_assignable_v<allocator_type>)
            -> vector & {
            if (allocator_traits::propagate_on_container_move_assignment::value) {
                _deallocate();
                _allocator = std::move(other._allocator);
                _adopt_allocations_of(other);
            } else if (_allocator == other._allocator) {
                _deallocate();
                _adopt_allocations_of(other);
            } else {
                assign(other._begin, other._end);
                other.clear();
            }
            return *this;
        }

        constexpr ~vector() {
            clear();
            _deallocate();
        }

        // Member functions

        constexpr auto assign(std::forward_iterator auto first, std::forward_iterator auto last) -> void {
            auto dist = static_cast<size_type>(std::distance(first, last));

            if (dist > capacity()) {
                _deallocate();
                _allocate(_recommend(dist));
                _construct_at_end(first, last, dist);
                return;
            }

            if (dist > size()) {
                auto mid = std::next(first, static_cast<difference_type>(size()));
                std::copy(first, mid, _begin);
                _construct_at_end(mid, last, dist - size());
            } else {
                auto mid = std::copy(first, last, _begin);
                _destruct_at_end(mid);
            }
        }

        constexpr auto assign(std::input_iterator auto first, std::input_iterator auto last) -> void {
            clear();
            for (; first != last; ++first) {
                emplace_back(*first);
            }
        }

        constexpr auto assign(size_type size, const_reference value) -> void {
            if (size > capacity()) {
                _deallocate();
                _allocate(_recommend(size));
                _construct_at_end(size, value);
                return;
            }

            std::fill_n(_begin, std::min(size, this->size()), value);

            if (size > this->size()) {
                _construct_at_end(size - this->size(), value);
            } else {
                _destruct_at_end(_begin + size);
            }
        }

        constexpr auto assign(std::initializer_list<value_type> list) -> void;

        constexpr auto get_allocator() const noexcept -> allocator_type {
            return _allocator;
        }

        // Element access

        constexpr auto at(size_type index) -> reference {
            if (index >= size()) {
                throw std::out_of_range("");
            }
            return *(_begin + index);
        }

        constexpr auto at(size_type index) const -> const_reference {
            if (index >= size()) {
                throw std::out_of_range("");
            }
            return *(_begin + index);
        }

        constexpr auto operator[](size_type index) noexcept -> reference {
            return *(_begin + index);
        }

        constexpr auto operator[](size_type index) const noexcept -> const_reference {
            return *(_begin + index);
        }

        constexpr auto front() -> reference {
            if (empty()) {
                throw std::out_of_range("");
            }
            return *_begin;
        }

        constexpr auto front() const -> const_reference {
            if (empty()) {
                throw std::out_of_range("");
            }
            return *_begin;
        }

        constexpr auto back() -> reference {
            if (empty()) {
                throw std::out_of_range("");
            }
            return *(_end - 1);
        }

        constexpr auto back() const -> const_reference {
            if (empty()) {
                throw std::out_of_range("");
            }
            return *(_end - 1);
        }

        constexpr auto data() noexcept -> pointer {
            return _begin;
        }

        constexpr auto data() const noexcept -> const_pointer {
            return _begin;
        }

        // Iterators

        constexpr auto begin() noexcept -> iterator {
            return _begin;
        }

        constexpr auto begin() const noexcept -> const_iterator {
            return _begin;
        }

        constexpr auto end() noexcept -> iterator {
            return _end;
        }

        constexpr auto end() const noexcept -> const_iterator {
            return _end;
        }

        constexpr auto rbegin() noexcept -> reverse_iterator {
            return end();
        }

        constexpr auto rbegin() const noexcept -> const_reverse_iterator {
            return end();
        }

        constexpr auto rend() noexcept -> reverse_iterator {
            return begin();
        }

        constexpr auto rend() const noexcept -> const_reverse_iterator {
            return begin();
        }

        constexpr auto cbegin() const noexcept -> const_iterator {
            return begin();
        }

        constexpr auto cend() const noexcept -> const_iterator {
            return end();
        }

        constexpr auto crbegin() const noexcept -> const_reverse_iterator {
            return rbegin();
        }

        constexpr auto crend() const noexcept -> const_reverse_iterator {
            return rend();
        }

        // Capacity

        [[nodiscard]] constexpr auto capacity() const noexcept -> size_type {
            return static_cast<size_type>(_capacity - _begin);
        }

        [[nodiscard]] constexpr auto empty() const noexcept -> bool {
            return _begin == _end;
        }

        [[nodiscard]] constexpr auto max_size() const noexcept -> size_type {
            const size_type max_diff = std::numeric_limits<difference_type>::max() / sizeof(value_type);
            const size_type max_size = allocator_traits::max_size(_allocator);
            return std::min<size_type>(max_diff, max_size);
        }

        constexpr auto reserve(size_type size) -> void {
            if (size > max_size()) {
                throw std::length_error("");
            }

            if (size > capacity()) {
                vector tmp(_allocator);
                tmp._allocate(size);
                tmp._construct_at_end(_begin, _end, this->size());
                swap(tmp);
            }
        }

        constexpr auto shrink_to_fit() noexcept -> void;

        [[nodiscard]] constexpr auto size() const noexcept -> size_type {
            return static_cast<size_type>(_end - _begin);
        }

        // Modifiers

        constexpr auto clear() noexcept -> void {
            _destruct_at_end(_begin);
        }

        constexpr auto emplace(const_iterator position, auto &&...args) -> iterator;

        constexpr auto emplace_back(auto &&...args) -> reference {
            if (size() < capacity()) {
                _construct_one_at_end(std::forward<decltype(args)>(args)...);
            } else {
                _emplace_back(std::forward<decltype(args)>(args)...);
            }
            return back();
        }

        constexpr auto erase(const_iterator position) -> iterator;
        constexpr auto erase(const_iterator first, const_iterator last) -> iterator;

        constexpr auto insert(const_iterator position, const_reference value) -> iterator;
        constexpr auto insert(const_iterator position, value_type &&value) -> iterator;
        constexpr auto insert(const_iterator position, size_type size, const_reference value) -> iterator;

        constexpr auto insert(const_iterator position, std::input_iterator auto first, std::input_iterator auto last)
            -> iterator;

        constexpr auto insert(const_iterator position, std::initializer_list<value_type> list) -> iterator;

        constexpr auto pop_back() -> void {
            if (empty()) {
                throw std::out_of_range("");
            }
            _destruct_at_end(_end - 1);
        }

        constexpr auto push_back(const_reference value) -> void {
            if (size() < capacity()) {
                _construct_one_at_end(value);
            } else {
                _push_back(value);
            }
        }

        constexpr auto push_back(value_type &&value) -> void {
            if (size() < capacity()) {
                _construct_one_at_end(std::move(value));
            } else {
                _push_back(std::move(value));
            }
        }

        constexpr auto resize(size_type size) -> void;
        constexpr auto resize(size_type size, const_reference value) -> void;

        constexpr auto swap(vector &other) noexcept(std::is_nothrow_swappable_v<allocator_type>) -> void {
            using std::swap;
            if (allocator_traits::propagate_on_container_swap::value) {
                swap(_allocator, other._allocator);
                swap(_begin, other._begin);
                swap(_end, other._end);
                swap(_capacity, other._capacity);
            } else if (_allocator == other._allocator) {
                swap(_begin, other._begin);
                swap(_end, other._end);
                swap(_capacity, other._capacity);
            } else {
                auto tmp = std::move(*this);
                *this    = std::move(other);
                other    = std::move(tmp);
            }
        }
    };
} // namespace myproject

#endif // MYPROJECT_VECTOR_HPP_
