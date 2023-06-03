#include "../src/application.hpp"

#include "../src/menu.hpp"

#include <catch2/catch_test_macros.hpp>
#include <chrono> // NOLINT(build/c++11)
#include <sstream>

namespace application {
    constexpr auto MENU_REPR = R"([1]: Make CarPlant
[2]: Make Shipyard
[3]: Print Container
[4]: Erase Container
[5]: Load from File
[6]: Save to File
[7]: Sort Container
[8]: Total in Container
[q]: Quit
> )";

    auto execute(const std::string &commands) -> std::string {
        auto input  = std::make_shared<std::istringstream>(commands);
        auto output = std::make_shared<std::ostringstream>();

        const myproject::menu::StreamView view(input, output);
        const myproject::menu::Presenter  presenter(view);
        myproject::Application            application(presenter);
        application.execute();

        return output->str();
    }
} // namespace application

TEST_CASE("Make CarPlant", "[application]") {
    constexpr auto commands = R"(
        1
        Kyiv
        12
        BMW
        3
        q
    )";

    std::string to_expect;
    to_expect += application::MENU_REPR;
    to_expect += "Enter location: Enter employees: Enter manufacturer: ";
    to_expect += application::MENU_REPR;
    to_expect += "Location: Kyiv\nEmployees: 12\nManufacturer: BMW\n";
    to_expect += application::MENU_REPR;
    to_expect += "Exiting...\n";

    REQUIRE(to_expect == application::execute(commands));
}

TEST_CASE("Make Shipyard", "[application]") {
    constexpr auto commands = R"(
        2
        Odesa
        42
        5
        3
        q
    )";

    std::string to_expect;
    to_expect += application::MENU_REPR;
    to_expect += "Enter location: Enter employees: Enter ships: ";
    to_expect += application::MENU_REPR;
    to_expect += "Location: Odesa\nEmployees: 42\nShips: 5\n";
    to_expect += application::MENU_REPR;
    to_expect += "Exiting...\n";

    REQUIRE(to_expect == application::execute(commands));
}

TEST_CASE("Print Container", "[application]") {
    constexpr auto commands = R"(
        1
        Kyiv
        12
        BMW
        3
        q
    )";

    std::string to_expect;
    to_expect += application::MENU_REPR;
    to_expect += "Enter location: Enter employees: Enter manufacturer: ";
    to_expect += application::MENU_REPR;
    to_expect += "Location: Kyiv\nEmployees: 12\nManufacturer: BMW\n";
    to_expect += application::MENU_REPR;
    to_expect += "Exiting...\n";

    REQUIRE(to_expect == application::execute(commands));
}

TEST_CASE("Erase Container", "[application]") {
    constexpr auto commands = R"(
        1
        Kyiv
        12
        BMW
        3
        4
        3
        q
    )";

    std::string to_expect;
    to_expect += application::MENU_REPR;
    to_expect += "Enter location: Enter employees: Enter manufacturer: ";
    to_expect += application::MENU_REPR;
    to_expect += "Location: Kyiv\nEmployees: 12\nManufacturer: BMW\n";
    to_expect += application::MENU_REPR;
    to_expect += application::MENU_REPR;
    to_expect += application::MENU_REPR;
    to_expect += "Exiting...\n";

    REQUIRE(to_expect == application::execute(commands));
}

TEST_CASE("Load from File / Save to File", "[application]") {
    auto now  = std::chrono::system_clock::now();
    auto time = std::chrono::system_clock::to_time_t(now);
    auto path = std::filesystem::temp_directory_path() / fmt::format("{}.bin", time);

    SECTION("Found") {
        const auto commands = fmt::format(R"(
            1
            Kyiv
            12
            BMW
            3
            6
            {}
            4
            5
            {}
            3
            q
        )",
                                          path.string(),
                                          path.string());

        std::string to_expect;
        to_expect += application::MENU_REPR;
        to_expect += "Enter location: Enter employees: Enter manufacturer: ";
        to_expect += application::MENU_REPR;
        to_expect += "Location: Kyiv\nEmployees: 12\nManufacturer: BMW\n";
        to_expect += application::MENU_REPR;
        to_expect += "Enter path: ";
        to_expect += application::MENU_REPR;
        to_expect += application::MENU_REPR;
        to_expect += "Enter path: ";
        to_expect += application::MENU_REPR;
        to_expect += "Location: Kyiv\nEmployees: 12\nManufacturer: BMW\n";
        to_expect += application::MENU_REPR;
        to_expect += "Exiting...\n";

        REQUIRE(to_expect == application::execute(commands));
        std::filesystem::remove(path);
    }

    SECTION("Not Found") {
        const auto commands = fmt::format(R"(
            5
            {}
            q
        )",
                                          path.string());

        std::string to_expect;
        to_expect += application::MENU_REPR;
        to_expect += "Enter path: ";
#if defined(__linux__)
        to_expect += fmt::format("filesystem error: Could not open file: Input/output error [{}]\n", path.string());
#elif defined(_WIN32)
        to_expect += fmt::format("Could not open file: io error: \"{}\"\n", path.string());
#endif
        to_expect += application::MENU_REPR;
        to_expect += "Exiting...\n";

        REQUIRE(to_expect == application::execute(commands));
    }
}

TEST_CASE("Sort Container", "[application]") {
    constexpr auto commands = R"(
        1
        Kyiv
        12
        BMW
        2
        Odesa
        42
        5
        1
        Kharkiv
        69
        Toyota
        3
        7
        3
        q
    )";

    std::string to_expect;
    to_expect += application::MENU_REPR;
    to_expect += "Enter location: Enter employees: Enter manufacturer: ";
    to_expect += application::MENU_REPR;
    to_expect += "Enter location: Enter employees: Enter ships: ";
    to_expect += application::MENU_REPR;
    to_expect += "Enter location: Enter employees: Enter manufacturer: ";
    to_expect += application::MENU_REPR;
    to_expect += "Location: Kharkiv\nEmployees: 69\nManufacturer: Toyota\n";
    to_expect += "Location: Odesa\nEmployees: 42\nShips: 5\n";
    to_expect += "Location: Kyiv\nEmployees: 12\nManufacturer: BMW\n";
    to_expect += application::MENU_REPR;
    to_expect += application::MENU_REPR;
    to_expect += "Location: Kyiv\nEmployees: 12\nManufacturer: BMW\n";
    to_expect += "Location: Odesa\nEmployees: 42\nShips: 5\n";
    to_expect += "Location: Kharkiv\nEmployees: 69\nManufacturer: Toyota\n";
    to_expect += application::MENU_REPR;
    to_expect += "Exiting...\n";

    REQUIRE(to_expect == application::execute(commands));
}

TEST_CASE("Total in Container", "[application]") {
    SECTION("Found") {
        constexpr auto commands = R"(
            1
            Kyiv
            12
            BMW
            8
            Kyiv
            q
        )";

        std::string to_expect;
        to_expect += application::MENU_REPR;
        to_expect += "Enter location: Enter employees: Enter manufacturer: ";
        to_expect += application::MENU_REPR;
        to_expect += "Enter location: ";
        to_expect += "12 employees in Kyiv\n";
        to_expect += application::MENU_REPR;
        to_expect += "Exiting...\n";

        REQUIRE(to_expect == application::execute(commands));
    }

    SECTION("Not Found") {
        constexpr auto commands = R"(
            1
            Kyiv
            12
            BMW
            8
            Odesa
            q
        )";

        std::string to_expect;
        to_expect += application::MENU_REPR;
        to_expect += "Enter location: Enter employees: Enter manufacturer: ";
        to_expect += application::MENU_REPR;
        to_expect += "Enter location: ";
        to_expect += "0 employees in Odesa\n";
        to_expect += application::MENU_REPR;
        to_expect += "Exiting...\n";

        REQUIRE(to_expect == application::execute(commands));
    }
}
