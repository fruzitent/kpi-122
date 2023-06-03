#include "./application.hpp"
#include "./throw_exception.hpp"

#include <cstdlib>
#include <exception>
#include <fmt/core.h>
#include <fmt/ostream.h>
#include <iostream>
#include <source_location>
#include <typeinfo>

auto main() -> int try {
    myproject::Application application;
    application.execute();
    return EXIT_SUCCESS;
} catch (const std::exception &error) {
    auto location = myproject::get_throw_location(error);

    fmt::println(std::cerr, "std::terminate called after throwing an exception:\n");
    fmt::println(std::cerr, "      type: {}", typeid(error).name());
    fmt::println(std::cerr, "    what(): {}", error.what());
    fmt::println(std::cerr,
                 "  location: {}:{}:{} in function '{}'",
                 location.file_name(),
                 location.line(),
                 location.column(),
                 location.function_name());

    return EXIT_FAILURE;
} catch (...) {
    fmt::println(std::cerr, "std::terminate called after throwing an unknown exception");
    return EXIT_FAILURE;
}
