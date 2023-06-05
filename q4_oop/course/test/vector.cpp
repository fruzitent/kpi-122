#include "../src/vector.hpp"

#include <catch2/catch_test_macros.hpp>
#include <cstddef>

// NOLINTBEGIN(readability-function-cognitive-complexity)

TEST_CASE("construct", "[vector]") {
    using size_type  = std::size_t;
    using value_type = int;

    constexpr size_type  size  = 3;
    constexpr value_type value = 42;

    SECTION("default") {
        const myproject::vector<value_type> vec;
        REQUIRE(vec.empty());
    }

    SECTION("default.size") {
        const myproject::vector<value_type> vec(size);
        REQUIRE(size == vec.size());
        REQUIRE(size <= vec.capacity());
    }

    SECTION("default.size_with_allocator") {
        const std::allocator<value_type>    allocator;
        const myproject::vector<value_type> vec(size, allocator);
        REQUIRE(size == vec.size());
        REQUIRE(size <= vec.capacity());
    }

    SECTION("default.value") {
        myproject::vector<value_type> vec(size, value);
        REQUIRE(size == vec.size());
        REQUIRE(size <= vec.capacity());
        for (size_type i = 0; i < size; ++i) {
            REQUIRE(value == vec[i]);
        }
    }

    SECTION("default.value_with_allocator") {
        const std::allocator<value_type> allocator;
        myproject::vector<value_type>    vec(size, value, allocator);
        REQUIRE(size == vec.size());
        REQUIRE(size <= vec.capacity());
        for (size_type i = 0; i < size; ++i) {
            REQUIRE(value == vec[i]);
        }
    }

    SECTION("copy.constructor") {
        const myproject::vector<value_type> vec0(size, value);
        myproject::vector<value_type>       vec1(vec0); // NOLINT(performance-unnecessary-copy-initialization)
        REQUIRE(size == vec1.size());
        REQUIRE(size <= vec1.capacity());
        for (size_type i = 0; i < size; ++i) {
            REQUIRE(value == vec1[i]);
        }
    }

    SECTION("copy.assignment") {
        const myproject::vector<value_type> vec0(size, value);
        myproject::vector<value_type>       vec1;
        vec1 = vec0;
        REQUIRE(size == vec1.size());
        REQUIRE(size <= vec1.capacity());
        for (size_type i = 0; i < size; ++i) {
            REQUIRE(value == vec1[i]);
        }
    }

    SECTION("move.constructor") {
        myproject::vector<value_type> vec0(size, value);
        myproject::vector<value_type> vec1(std::move(vec0));

        // NOLINTNEXTLINE(bugprone-use-after-move,hicpp-invalid-access-moved)
        REQUIRE(vec0.empty()); // cppcheck-suppress accessMoved

        REQUIRE(size == vec1.size());
        REQUIRE(size <= vec1.capacity());
        for (size_type i = 0; i < size; ++i) {
            REQUIRE(value == vec1[i]);
        }
    }

    SECTION("move.assignment") {
        myproject::vector<value_type> vec0(size, value);
        myproject::vector<value_type> vec1;
        vec1 = std::move(vec0);

        // NOLINTNEXTLINE(bugprone-use-after-move,hicpp-invalid-access-moved)
        REQUIRE(vec0.empty()); // cppcheck-suppress accessMoved

        REQUIRE(size == vec1.size());
        REQUIRE(size <= vec1.capacity());
        for (size_type i = 0; i < size; ++i) {
            REQUIRE(value == vec1[i]);
        }
    }
}

TEST_CASE("member_functions", "[vector]") {
    using size_type  = std::size_t;
    using value_type = int;

    constexpr size_type  size  = 3;
    constexpr value_type value = 42;

    SECTION("assign.iterator") {
        // NOLINTBEGIN(cppcoreguidelines-owning-memory,cppcoreguidelines-pro-bounds-pointer-arithmetic)
        const auto *arr = new value_type[size]{1, 2, 3};

        myproject::vector<value_type> vec;
        vec.assign(arr, arr + size);

        REQUIRE(size == vec.size());
        REQUIRE(size <= vec.capacity());
        for (size_type i = 0; i < size; ++i) {
            REQUIRE(arr[i] == vec[i]);
        }

        delete[] arr;
        // NOLINTEND(cppcoreguidelines-owning-memory,cppcoreguidelines-pro-bounds-pointer-arithmetic)
    }

    SECTION("assign.value") {
        myproject::vector<value_type> vec;
        vec.assign(size, value);

        REQUIRE(size == vec.size());
        REQUIRE(size <= vec.capacity());
        for (size_type i = 0; i < size; ++i) {
            REQUIRE(value == vec[i]);
        }
    }

    SECTION("assign.initializer_list") {}

    SECTION("get_allocator") {
        std::allocator<value_type>          allocator;
        const myproject::vector<value_type> vec(allocator);
        REQUIRE(allocator == vec.get_allocator());
    }
}

TEST_CASE("element_access", "[vector]") {
    using size_type  = std::size_t;
    using value_type = int;

    SECTION("at") {}
    SECTION("operator[]") {}

    SECTION("front") {
        myproject::vector<value_type> vec;
        REQUIRE_THROWS_AS(vec.front(), std::out_of_range);
    }

    SECTION("back") {
        constexpr size_type size = 1;

        myproject::vector<value_type> vec(size);
        REQUIRE(vec.back() == value_type{});
        vec.clear();
        REQUIRE_THROWS_AS(vec.back(), std::out_of_range);
    }

    SECTION("data") {}
}

TEST_CASE("iterators", "[vector]") {
    SECTION("begin") {}
    SECTION("end") {}
    SECTION("rbegin") {}
    SECTION("rend") {}
    SECTION("cbegin") {}
    SECTION("cend") {}
    SECTION("crbegin") {}
    SECTION("crend") {}
}

TEST_CASE("capacity", "[vector]") {
    using value_type = int;
    using size_type  = std::size_t;

    constexpr size_type size = 3;

    SECTION("capacity") {}
    SECTION("empty") {}
    SECTION("max_size") {}

    SECTION("reserve") {
        myproject::vector<value_type> vec(size);
        REQUIRE(vec.size() == size);
        REQUIRE(vec.capacity() >= size);

        {
            constexpr std::size_t new_size = 10;
            vec.reserve(new_size);
            REQUIRE(vec.size() == size);
            REQUIRE(vec.capacity() >= new_size);
        }

        {
            constexpr std::size_t new_size = 0;
            vec.reserve(new_size);
            REQUIRE(vec.size() == size);
            REQUIRE(vec.capacity() >= new_size);
        }
    }

    SECTION("shrink_to_fit") {}
    SECTION("size") {}
}

TEST_CASE("modifiers", "[vector]") {
    using value_type = int;

    SECTION("clear") {}
    SECTION("emplace") {}
    SECTION("emplace_back") {}
    SECTION("erase.position") {}
    SECTION("erase.iterator") {}
    SECTION("insert.l-value") {}
    SECTION("insert.r-value") {}
    SECTION("insert.size") {}
    SECTION("insert.iterator") {}
    SECTION("insert.initializer_list") {}

    SECTION("pop_back") {
        myproject::vector<value_type> vec;
        vec.push_back(value_type{});
        vec.pop_back();
        REQUIRE_THROWS_AS(vec.pop_back(), std::out_of_range);
    }

    SECTION("push_back.l-value") {}
    SECTION("push_back.r-value") {}
    SECTION("resize") {}
    SECTION("resize") {}
    SECTION("swap") {}
}

// NOLINTEND(readability-function-cognitive-complexity)
