#ifndef AIDS_H_
#define AIDS_H_

#include <iostream>

#include "src/gsl.hpp"

namespace aids {
    template<typename T>
    struct default_delete {
        void operator()(gsl::owner<T> pointer) const { delete pointer; }
    };

    template<typename T>
    struct default_delete<T[]> {
        void operator()(gsl::owner<T *> array) const { delete[] array; }
    };

    template<>
    struct default_delete<std::FILE *> {
        void operator()(gsl::owner<std::FILE *> file) const {
            std::fclose(file);  // NOLINT
        }
    };

    template<typename Resource, typename Deleter = default_delete<Resource>>
    class unique_ptr {
      public:
        using value_type      = Resource;
        using const_pointer   = const value_type *;
        using const_reference = const value_type &;
        using pointer         = value_type *;
        using reference       = value_type &;

      private:
        gsl::owner<value_type> _resource;
        Deleter                _deleter;

      public:
        explicit unique_ptr(gsl::owner<value_type> resource, Deleter deleter = default_delete<Resource>()) :
            _resource(resource),
            _deleter(deleter) {}

        unique_ptr(const unique_ptr &)                     = default;
        unique_ptr(unique_ptr &&other) noexcept            = default;
        unique_ptr &operator=(const unique_ptr &other)     = default;
        unique_ptr &operator=(unique_ptr &&other) noexcept = default;

        ~unique_ptr() { _deleter(_resource); }
    };

    template<typename Resource, typename Deleter>
    class unique_ptr<Resource[], Deleter> {
      public:
        using value_type      = Resource;
        using const_pointer   = const value_type *;
        using const_reference = const value_type &;
        using pointer         = value_type *;
        using reference       = value_type &;

      private:
        gsl::owner<pointer> _resource;
        Deleter             _deleter;

      public:
        explicit unique_ptr(gsl::owner<pointer> resource, Deleter deleter = default_delete<value_type[]>()) :
            _resource(resource),
            _deleter(deleter) {}

        unique_ptr(const unique_ptr &)                     = default;
        unique_ptr(unique_ptr &&other) noexcept            = default;
        unique_ptr &operator=(const unique_ptr &other)     = default;
        unique_ptr &operator=(unique_ptr &&other) noexcept = default;

        ~unique_ptr() { _deleter(_resource); }
    };
}  // namespace aids

#endif  // AIDS_H
