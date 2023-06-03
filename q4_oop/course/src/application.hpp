#ifndef MYPROJECT_APPLICATION_HPP_
#define MYPROJECT_APPLICATION_HPP_

#include "./enterprise.hpp"
#include "./menu.hpp"
#include "./stack.hpp"
#include "./throw_exception.hpp"

#include <cstddef>
#include <filesystem>
#include <fmt/core.h>
#include <iostream>
#include <memory>
#include <string>
#include <system_error>

namespace myproject {
    template <menu::View View = menu::ConsoleView>
    class Application {
      protected:
        bool _is_quit = false;

        menu::Presenter<View>              _presenter;
        stack<std::shared_ptr<Enterprise>> _stack;

      private:
        template <typename T>
        auto _get_input(const std::string &prompt) const noexcept -> T {
            _presenter._view.write(fmt::format("Enter {}: ", prompt));

            T value{};

            std::istringstream stream(_presenter._view.read());
            if constexpr (std::is_same_v<T, std::string>) {
                std::getline(stream, value);
            } else {
                stream >> value;
            }

            return value;
        }

        constexpr auto _make_carplant() -> void {
            auto location     = _get_input<std::string>("location");
            auto employees    = _get_input<std::size_t>("employees");
            auto manufacturer = _get_input<std::string>("manufacturer");
            _stack.emplace(myproject::CarPlant::create(location, employees, manufacturer));
        }

        constexpr auto _make_shipyard() -> void {
            auto location  = _get_input<std::string>("location");
            auto employees = _get_input<std::size_t>("employees");
            auto ships     = _get_input<std::size_t>("ships");
            _stack.emplace(myproject::Shipyard::create(location, employees, ships));
        }

        constexpr auto _print_container() const noexcept -> void {
            auto callback = [&](const auto &item) {
                _presenter._view.write(fmt::format("{}\n", item->repr()));
            };
            myproject::for_each(_stack, callback);
        }

        constexpr auto _erase_container() -> void {
            myproject::erase(&_stack);
        }

        auto _load_from_file() -> void {
            myproject::erase(&_stack);

            auto path = _get_input<std::filesystem::path>("path");

            std::ifstream file(path, std::ios::binary);
            if (!file.is_open()) {
                myproject::throw_with_location(
                    std::filesystem::filesystem_error("Could not open file",
                                                      path,
                                                      std::make_error_code(std::errc::io_error)));
            }

            myproject::read(file, &_stack);
        }

        auto _save_to_file() -> void {
            auto path = _get_input<std::filesystem::path>("path");

            std::ofstream file{path, std::ios::binary};
            if (!file.is_open()) {
                myproject::throw_with_location(
                    std::filesystem::filesystem_error("Could not open file",
                                                      path,
                                                      std::make_error_code(std::errc::io_error)));
            }

            myproject::write(file, _stack);
        }

        constexpr auto _sort_container() noexcept -> void {
            constexpr auto predicate = [](const auto &lhs, const auto &rhs) {
                return lhs->employees() < rhs->employees();
            };
            myproject::sort(&_stack, predicate);
        }

        constexpr auto _total_in_container() noexcept -> void {
            auto        location = _get_input<std::string>("location");
            std::size_t employees{};

            auto callback = [&](const auto &item) {
                if (item->location() == location) {
                    employees += item->employees();
                }
            };
            myproject::for_each(_stack, callback);

            _presenter._view.write(fmt::format("{} employees in {}\n", employees, location));
        }

        constexpr auto _quit() noexcept -> void {
            _presenter._view.write("Exiting...\n");
            _is_quit = true;
        }

        constexpr auto _setup() -> void {
            _presenter.add("1", "Make CarPlant", [&] {
                _make_carplant();
            });

            _presenter.add("2", "Make Shipyard", [&] {
                _make_shipyard();
            });

            _presenter.add("3", "Print Container", [&] {
                _print_container();
            });

            _presenter.add("4", "Erase Container", [&] {
                _erase_container();
            });

            _presenter.add("5", "Load from File", [&] {
                _load_from_file();
            });

            _presenter.add("6", "Save to File", [&] {
                _save_to_file();
            });

            _presenter.add("7", "Sort Container", [&] {
                _sort_container();
            });

            _presenter.add("8", "Total in Container", [&] {
                _total_in_container();
            });

            _presenter.add("q", "Quit", [&] {
                _quit();
            });
        }

      public:
        constexpr Application() {
            _setup();
        }

        explicit constexpr Application(menu::Presenter<View> presenter) : _presenter(presenter) {
            _setup();
        }

        constexpr auto execute() noexcept -> void {
            while (!_is_quit) {
                _presenter.execute();
            }
        }
    };
} // namespace myproject

#endif // MYPROJECT_APPLICATION_HPP_
