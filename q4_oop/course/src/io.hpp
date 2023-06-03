#ifndef MYPROJECT_IO_HPP_
#define MYPROJECT_IO_HPP_

#include <concepts>
#include <cstddef>
#include <iostream>
#include <memory>
#include <string>
#include <typeinfo>

namespace myproject {
    template <typename T>
    constexpr auto read(std::istream &is, T *obj) noexcept -> void = delete;

    template <typename T>
    constexpr auto write(std::ostream &os, const T &obj) noexcept -> void = delete;
} // namespace myproject

namespace myproject {
    template <typename T>
    concept Readable = requires(std::istream &is, T *obj) {
        { obj->read(is) } -> std::same_as<void>;
    };

    template <Readable T>
    constexpr auto read(std::istream &is, T *obj) noexcept -> void {
        obj->read(is);
    }

    template <typename T>
    concept Writable = requires(std::ostream &os, const T &obj) {
        { obj.write(os) } -> std::same_as<void>;
    };

    template <Writable T>
    constexpr auto write(std::ostream &os, const T &obj) noexcept -> void {
        obj.write(os);
    }
} // namespace myproject

// NOLINTBEGIN(cppcoreguidelines-pro-type-reinterpret-cast)

namespace myproject {
    auto read(std::istream &is, std::size_t *obj) noexcept -> void {
        is.read(reinterpret_cast<char *>(obj), sizeof(*obj));
    }

    auto write(std::ostream &os, const std::size_t &obj) noexcept -> void {
        os.write(reinterpret_cast<const char *>(&obj), sizeof(obj));
    }
} // namespace myproject

namespace myproject {
    auto read(std::istream &is, std::string *obj) noexcept -> void {
        std::streamsize size{};
        is.read(reinterpret_cast<char *>(&size), sizeof(size));
        obj->resize(static_cast<std::size_t>(size));
        is.read(obj->data(), size);
    }

    auto write(std::ostream &os, const std::string &obj) noexcept -> void {
        auto size = static_cast<std::streamsize>(obj.size());
        os.write(reinterpret_cast<const char *>(&size), sizeof(size));
        os.write(obj.data(), size);
    }
} // namespace myproject

// NOLINTEND(cppcoreguidelines-pro-type-reinterpret-cast)

namespace myproject {
    template <typename T>
    constexpr auto read(std::istream &is, std::shared_ptr<T> *obj) noexcept -> void = delete;

    namespace detail {
        template <typename T>
        constexpr auto read(std::istream &is, T *obj) noexcept -> void {
            using myproject::read;

            T item{};
            read(is, &item);
            *obj = item;
        }

        template <typename T>
        constexpr auto read(std::istream &is, std::shared_ptr<T> *obj, auto &&factory) noexcept -> void {
            std::size_t hash_code{};
            read(is, &hash_code);
            auto item = factory(hash_code);
            read(is, item.get());
            *obj = item;
        }
    } // namespace detail

    template <typename T>
    constexpr auto write(std::ostream &os, const std::shared_ptr<T> &obj) noexcept -> void {
        write(os, typeid(*obj).hash_code());
        write(os, *obj);
    }
} // namespace myproject

#endif // MYPROJECT_IO_HPP_
