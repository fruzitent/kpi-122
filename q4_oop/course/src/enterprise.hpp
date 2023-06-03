#ifndef MYPROJECT_ENTERPRISE_HPP_
#define MYPROJECT_ENTERPRISE_HPP_

#include "./io.hpp"

#include <cstddef>
#include <fmt/core.h>
#include <fmt/ostream.h>
#include <functional>
#include <iosfwd>
#include <memory>
#include <string>
#include <typeinfo>
#include <unordered_map>
#include <utility>

namespace myproject {
    class Enterprise {
      protected:
        std::string _location{};
        std::size_t _employees{};

      public:
        constexpr Enterprise() = default;

        constexpr Enterprise(const Enterprise &)                     = default;
        constexpr auto operator=(const Enterprise &) -> Enterprise & = default;

        constexpr Enterprise(Enterprise &&) noexcept                     = default;
        constexpr auto operator=(Enterprise &&) noexcept -> Enterprise & = default;

        constexpr Enterprise(decltype(_location) location, decltype(_employees) employees) noexcept :
            _location(std::move(location)),
            _employees(employees) {}

        virtual constexpr ~Enterprise() = default;

        static auto create(auto &&...args) noexcept -> std::shared_ptr<Enterprise> {
            return std::make_shared<Enterprise>(std::forward<decltype(args)>(args)...);
        }

        virtual auto repr() -> std::string {
            std::string result;
            result += fmt::format("Location: {}\n", _location);
            result += fmt::format("Employees: {}", _employees);
            return result;
        }

        [[nodiscard]] constexpr auto employees() noexcept -> decltype(_employees) & {
            return _employees;
        }

        [[nodiscard]] constexpr auto employees() const noexcept -> decltype(_employees) {
            return _employees;
        }

        constexpr auto employees(decltype(_employees) value) noexcept -> void {
            _employees = value;
        }

        [[nodiscard]] constexpr auto location() noexcept -> decltype(_location) & {
            return _location;
        }

        [[nodiscard]] constexpr auto location() const noexcept -> decltype(_location) {
            return _location;
        }

        constexpr auto location(decltype(_location) value) noexcept -> void {
            _location = std::move(value);
        }

        virtual auto read(std::istream &is) noexcept -> void {
            myproject::read(is, &_location);
            myproject::read(is, &_employees);
        }

        virtual auto write(std::ostream &os) const noexcept -> void {
            myproject::write(os, _location);
            myproject::write(os, _employees);
        }
    };

    class CarPlant : public Enterprise {
      protected:
        std::string _manufacturer{};

      public:
        constexpr CarPlant() = default;

        constexpr CarPlant(decltype(_location)     location,
                           decltype(_employees)    employees,
                           decltype(_manufacturer) manufacturer) :
            Enterprise(std::move(location), employees),
            _manufacturer(std::move(manufacturer)) {}

        static auto create(auto &&...args) noexcept -> std::shared_ptr<CarPlant> {
            return std::make_shared<CarPlant>(std::forward<decltype(args)>(args)...);
        }

        auto repr() -> std::string override {
            std::string result;
            result += fmt::format("{}\n", Enterprise::repr());
            result += fmt::format("Manufacturer: {}", _manufacturer);
            return result;
        }

        [[nodiscard]] constexpr auto manufacturer() noexcept -> decltype(_manufacturer) & {
            return _manufacturer;
        }

        [[nodiscard]] constexpr auto manufacturer() const noexcept -> decltype(_manufacturer) {
            return _manufacturer;
        }

        constexpr auto manufacturer(decltype(_manufacturer) value) noexcept -> void {
            _manufacturer = std::move(value);
        }

        auto read(std::istream &is) noexcept -> void override {
            Enterprise::read(is);
            myproject::read(is, &_manufacturer);
        }

        auto write(std::ostream &os) const noexcept -> void override {
            Enterprise::write(os);
            myproject::write(os, _manufacturer);
        }
    };

    class Shipyard : public Enterprise {
      protected:
        std::size_t _ships{};

      public:
        constexpr Shipyard() = default;

        constexpr Shipyard(decltype(_location) location, decltype(_employees) employees, decltype(_ships) ships) :
            Enterprise(std::move(location), employees),
            _ships(ships) {}

        static auto create(auto &&...args) noexcept -> std::shared_ptr<Shipyard> {
            return std::make_shared<Shipyard>(std::forward<decltype(args)>(args)...);
        }

        auto repr() -> std::string override {
            std::string result;
            result += fmt::format("{}\n", Enterprise::repr());
            result += fmt::format("Ships: {}", _ships);
            return result;
        }

        [[nodiscard]] constexpr auto ships() noexcept -> decltype(_ships) & {
            return _ships;
        }

        [[nodiscard]] constexpr auto ships() const noexcept -> decltype(_ships) {
            return _ships;
        }

        constexpr auto ships(decltype(_ships) value) noexcept -> void {
            _ships = value;
        }

        auto read(std::istream &is) noexcept -> void override {
            Enterprise::read(is);
            myproject::read(is, &_ships);
        }

        auto write(std::ostream &os) const noexcept -> void override {
            Enterprise::write(os);
            myproject::write(os, _ships);
        }
    };

    inline auto enterprise_registry() noexcept -> auto & {
        // clang-format off
        static std::unordered_map<std::size_t, std::function<std::shared_ptr<Enterprise>()>> obj{
            {typeid(Enterprise).hash_code(), []{ return Enterprise::create(); }},
            {typeid(CarPlant).hash_code(), []{ return CarPlant::create(); }},
            {typeid(Shipyard).hash_code(), []{ return Shipyard::create(); }},
        };
        // clang-format on
        return obj;
    }

    inline auto read(std::istream &is, std::shared_ptr<Enterprise> *obj) noexcept -> void {
        decltype(typeid(*obj).hash_code()) type{};
        read(is, &type);
        *obj = enterprise_registry().at(type)();
        read(is, obj->get());
    }
} // namespace myproject

#endif // MYPROJECT_ENTERPRISE_HPP_
