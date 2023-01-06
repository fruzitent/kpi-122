cmake_minimum_required(VERSION 3.24)

project(CmakeConfigPackageTests LANGUAGES CXX)

if(PROJECT_IS_TOP_LEVEL OR TEST_INSTALLED_VERSION)
  enable_testing()
  find_package(myproject CONFIG REQUIRED)
  if(NOT TARGET myproject::project_options)
    message(FATAL_ERROR "Requiered config package not found!")
    return()
  endif()
endif()

add_test(NAME cli.has_help COMMAND main --help)

add_test(NAME cli.version_matches COMMAND main --version)
set_tests_properties(cli.version_matches PROPERTIES PASS_REGULAR_EXPRESSION
                                                    "${PROJECT_VERSION}")

add_executable(tests tests.cpp)
target_link_libraries(
  tests PRIVATE myproject::project_warnings myproject::project_options
                Catch2::Catch2WithMain)

include(CTest)
include(Catch)
catch_discover_tests(tests)
