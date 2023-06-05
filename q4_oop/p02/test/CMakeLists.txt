if(PROJECT_IS_TOP_LEVEL OR TEST_INSTALLED_VERSION)
  enable_testing()
endif()

include(${Catch2_SOURCE_DIR}/extras/Catch.cmake)

add_executable(tests vector.cpp)
target_link_libraries(tests PRIVATE project_warnings project_options Catch2::Catch2WithMain)
target_link_system_libraries(tests PRIVATE fmt::fmt)

if(WIN32 AND BUILD_SHARED_LIBS)
  add_custom_command(
    TARGET tests
    PRE_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_RUNTIME_DLLS:tests> $<TARGET_FILE_DIR:tests>
    COMMAND_EXPAND_LISTS
  )
endif()

catch_discover_tests(
  tests
  TEST_PREFIX
  "unittests."
  REPORTER
  XML
  OUTPUT_DIR
  .
  OUTPUT_PREFIX
  "unittests."
  OUTPUT_SUFFIX
  .xml
)
