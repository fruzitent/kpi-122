#include "../src/menu.hpp"

#include <catch2/catch_test_macros.hpp>

namespace menu {
    constexpr auto MENU_REPR = R"([1]: Option 1
[q]: Quit
> )";

    auto execute(const std::string &commands) -> std::string {
        auto input  = std::make_shared<std::istringstream>(commands);
        auto output = std::make_shared<std::ostringstream>();

        const myproject::menu::StreamView view(input, output);
        myproject::menu::Presenter        presenter(view);

        presenter.add("1", "Option 1", [&] {
            view.write("Option 1 called\n");
        });

        bool is_quit = false;
        presenter.add("q", "Quit", [&] {
            view.write("Exiting...\n");
            is_quit = true;
        });

        while (!is_quit) {
            presenter.execute();
        }

        return output->str();
    }
} // namespace menu

TEST_CASE("StreamView", "[menu]") {
    SECTION("Found") {
        constexpr auto commands = R"(
            1
            q
        )";

        std::string to_expect;
        to_expect += menu::MENU_REPR;
        to_expect += "Option 1 called\n";
        to_expect += menu::MENU_REPR;
        to_expect += "Exiting...\n";

        REQUIRE(to_expect == menu::execute(commands));
    }

    SECTION("Not Found") {
        constexpr auto commands = R"(
            3
            q
        )";

        std::string to_expect;
        to_expect += menu::MENU_REPR;
        to_expect += "Invalid Option: 3\n";
        to_expect += menu::MENU_REPR;
        to_expect += "Exiting...\n";

        REQUIRE(to_expect == menu::execute(commands));
    }
}
