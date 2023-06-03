#ifndef MYPROJECT_MENU_HPP_
#define MYPROJECT_MENU_HPP_

#include "./throw_exception.hpp"
#include "./vector.hpp"

#include <algorithm>
#include <concepts>
#include <exception>
#include <fmt/core.h>
#include <fmt/ostream.h>
#include <functional>
#include <iostream>
#include <memory>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>

namespace myproject::menu {
    using key_type = std::string;

    class Model {
      protected:
        key_type              _key;
        std::string           _name;
        std::function<void()> _callback;

      public:
        Model(decltype(_key) key, decltype(_name) name, decltype(_callback) callback) :
            _key(std::move(key)),
            _name(std::move(name)),
            _callback(std::move(callback)) {}

        [[nodiscard]] constexpr auto key() const noexcept -> const std::string & {
            return _key;
        }

        [[nodiscard]] constexpr auto name() const noexcept -> const std::string & {
            return _name;
        }

        auto execute() const -> void {
            _callback();
        }
    };

    template <typename T>
    concept View = requires(T obj, const vector<Model> &items, const std::string &value) {
        { obj.read() } -> std::same_as<key_type>;
        { obj.write(value) } -> std::same_as<void>;
    };

    // NOLINTBEGIN(readability-convert-member-functions-to-static)

    struct ConsoleView {
        [[nodiscard]] auto read() const noexcept -> key_type { // cppcheck-suppress functionStatic
            std::string value{};
            std::getline(std::cin, value);
            return value;
        }

        auto write(const std::string &value) const noexcept -> void { // cppcheck-suppress functionStatic
            fmt::print(std::cout, "{}", value);
        }
    };

    // NOLINTEND(readability-convert-member-functions-to-static)

    class StreamView {
      protected:
        std::shared_ptr<std::istringstream> _input;
        std::shared_ptr<std::ostringstream> _output;

      public:
        explicit StreamView(decltype(_input) input, decltype(_output) output) :
            _input(std::move(input)),
            _output(std::move(output)) {}

        [[nodiscard]] auto read() const noexcept -> key_type {
            std::string value{};
            // std::getline(*_input, value); // TODO: hangs for no reason
            *_input >> value;
            return value;
        }

        auto write(const std::string &value) const noexcept -> void {
            fmt::print(*_output, "{}", value);
        }
    };

    template <View View = ConsoleView>
    class Presenter {
      protected:
        vector<Model> _items;

      public:
        View _view;

        explicit constexpr Presenter(View view = {}) : _view(std::move(view)) {}

        constexpr auto add(auto &&...args) -> void {
            _items.emplace_back(std::forward<decltype(args)>(args)...);
        }

        constexpr auto advance(const key_type &key) const -> void {
            auto model = std::find_if(_items.begin(), _items.end(), [&key](const auto &item) {
                return item.key() == key;
            });

            if (model == _items.end()) {
                throw_with_location(std::invalid_argument(fmt::format("Invalid Option: {}", key)));
            }

            model->execute();
        }

        constexpr auto execute() noexcept -> void {
            render();
            try {
                advance(_view.read());
            } catch (const std::exception &error) {
                _view.write(fmt::format("{}\n", error.what()));
            }
        }

        constexpr auto render() const noexcept -> void {
            for (const auto &item : _items) {
                _view.write(fmt::format("[{}]: {}\n", item.key(), item.name()));
            }
            _view.write("> ");
        }
    };
} // namespace myproject::menu

#endif // MYPROJECT_MENU_HPP_
