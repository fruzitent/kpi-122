#ifndef AIDS_MEMORY_UNIQUE_PTR_HPP_
#define AIDS_MEMORY_UNIQUE_PTR_HPP_

#include "src/aids/algorithm/move.hpp"
#include "src/aids/memory/default_delete.hpp"
#include "src/aids/type_traits/is_array.hpp"
#include "src/aids/type_traits/remove_extent.hpp"
#include "src/aids/utility/exchange.hpp"
#include "src/aids/utility/swap.hpp"

namespace aids {
    template<typename T, typename Deleter = aids::default_delete<T>>
    class unique_ptr {
      private:
        T*      _ptr = nullptr;
        Deleter _deleter;

      public:
        constexpr unique_ptr() = default;

        explicit constexpr unique_ptr(T* ptr, Deleter deleter = aids::default_delete<T>()) noexcept :
            _ptr(ptr),
            _deleter(deleter) {}

        constexpr unique_ptr(const unique_ptr&)            = delete;
        constexpr unique_ptr& operator=(const unique_ptr&) = delete;

        constexpr unique_ptr(unique_ptr&& other) noexcept :
            unique_ptr() {
            reset(other.release());
            _deleter = aids::move(other._deleter);  // NOLINT
        }

        constexpr unique_ptr& operator=(unique_ptr&& other) noexcept {
            reset(other.release());
            _deleter = aids::move(other._deleter);
            return *this;
        }

        template<typename U, typename E>
        requires std::is_convertible_v<U*, T*> && std::is_assignable_v<Deleter&, E&&>
        constexpr unique_ptr& operator=(unique_ptr&& other) noexcept {
            reset(static_cast<T*>(other.release()));
            _deleter = aids::move(other._deleter);
            return *this;
        }

        ~unique_ptr() { reset(); }

        [[nodiscard]] constexpr T* release() noexcept { return aids::exchange(_ptr, nullptr); }

        constexpr void reset(T* ptr = nullptr) noexcept {
            auto old = aids::exchange(_ptr, ptr);
            if (old != nullptr) {
                _deleter(old);
            }
        }

        [[nodiscard]] constexpr T* get() const noexcept { return _ptr; }

        explicit constexpr operator bool() const noexcept { return get() != nullptr; }

        constexpr T& operator*() const noexcept { return *get(); }

        constexpr T* operator->() const noexcept { return get(); }

        void swap(unique_ptr& other) noexcept {
            aids::swap(_ptr, other._ptr);
            aids::swap(_deleter, other._deleter);
        }
    };

    template<typename T, typename Deleter>
    class unique_ptr<T[], Deleter> : public unique_ptr<T, Deleter> {
      private:
        T*      _ptr = nullptr;
        Deleter _deleter;

      public:
        constexpr unique_ptr() :
            aids::unique_ptr<T>() {}

        explicit constexpr unique_ptr(T* ptr, Deleter deleter = aids::default_delete<T[]>()) noexcept :
            aids::unique_ptr<T, Deleter>(ptr, deleter) {}

        constexpr T& operator[](std::ptrdiff_t index) const noexcept { return this->get()[index]; }
    };

    template<typename T, typename... Args>
    constexpr aids::unique_ptr<T> make_unique(Args&&... args) {
        return aids::unique_ptr<T>(new T(aids::forward<Args>(args)...));
    }

    template<typename T>
    requires aids::is_array_v<T>
    constexpr aids::unique_ptr<T> make_unique(std::size_t size) {
        return aids::unique_ptr<T>(new aids::remove_extent_t<T>[size]());
    }
}  // namespace aids

#endif  // AIDS_MEMORY_UNIQUE_PTR_HPP_
