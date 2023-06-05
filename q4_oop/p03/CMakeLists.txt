cmake_minimum_required(VERSION 3.21)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_EXTENSIONS OFF)

project(
  myproject
  LANGUAGES CXX C
  VERSION 0.1.0
)

# TOOD: https://github.com/clangd/vscode-clangd/issues/48#issuecomment-987765846
configure_file(.clangd.in ${CMAKE_SOURCE_DIR}/.clangd @ONLY)

set(GIT_SHA
    "Unknown"
    CACHE STRING "SHA this build was generated from"
)
string(SUBSTRING "${GIT_SHA}" 0 8 GIT_SHORT_SHA)

# ------------------------------------------------------------------------------

file(DOWNLOAD https://github.com/cpm-cmake/CPM.cmake/releases/download/v0.38.1/CPM.cmake ${CMAKE_BINARY_DIR}/CPM.cmake)
include(${CMAKE_BINARY_DIR}/CPM.cmake)

# cpmaddpackage("gh:catchorg/Catch2#v3.3.2")
cpmaddpackage("gh:fmtlib/fmt#10.0.0")

# ------------------------------------------------------------------------------

include(FetchContent)

FetchContent_Declare(
  _project_options
  GIT_REPOSITORY https://github.com/aminya/project_options
  GIT_TAG v0.29.0
)

FetchContent_MakeAvailable(_project_options)

include(${_project_options_SOURCE_DIR}/Index.cmake)

dynamic_project_options(
  CPPCHECK_OPTIONS
  --enable=performance,portability,style,warning
  --inconclusive
  --inline-suppr
  --suppress=cppcheckError
  --suppress=functionConst
  --suppress=internalAstError
  --suppress=missingReturn
  --suppress=passedByValue
  --suppress=syntaxError
  --suppress=unmatchedSuppression
  # cmake-format: off
  # ENABLE_BUILD_WITH_TIME_TRACE
  # ENABLE_COVERAGE
  # ENABLE_DOXYGEN
  # ENABLE_INTERPROCEDURAL_OPTIMIZATION
  # LINKER "mold"
  # cmake-format: on
  PCH_HEADERS
  <string>
  <vector>
)

# ------------------------------------------------------------------------------

find_program(CPPLINT NAMES "cpplint")
if(CPPLINT)
  set(CPPLINT_FILTER "--filter=")
  string(APPEND CPPLINT_FILTER "-build/include_order,")
  string(APPEND CPPLINT_FILTER "-legal/copyright,")
  string(APPEND CPPLINT_FILTER "-readability/nolint,")
  string(APPEND CPPLINT_FILTER "-readability/todo,")
  string(APPEND CPPLINT_FILTER "-runtime/indentation_namespace,")
  string(APPEND CPPLINT_FILTER "-whitespace/comments,")
  string(APPEND CPPLINT_FILTER "-whitespace/indent,")
  string(APPEND CPPLINT_FILTER "-whitespace/line_length,")
  string(APPEND CPPLINT_FILTER "-whitespace/parens,")
  set(CMAKE_CXX_CPPLINT "${CPPLINT};${CPPLINT_FILTER}")
endif()

# cmake-format: off
# find_program(FIX_INCLUDES NAMES "fix_includes.py")
# find_program(IWYU_TOOL NAMES "iwyu_tool.py")
# if(FIX_INCLUDES AND IWYU_TOOL)
#   add_custom_target(
#     iwyu ALL COMMAND
#     "${IWYU_TOOL}" -p "${CMAKE_BINARY_DIR}" --
#       -Xiwyu --check_also="${CMAKE_SOURCE_DIR}/src/*.hpp"
#       -Xiwyu --cxx17ns
#       -Xiwyu --no_fwd_decls
#       -Xiwyu --quoted_includes_first
#       | "${FIX_INCLUDES}"
#   )
# endif()
# cmake-format: on

# ------------------------------------------------------------------------------

add_subdirectory(src)

# cmake-format: off
# include(CTest)
# if(BUILD_TESTING)
#   add_subdirectory(test)
# endif()
# cmake-format: on

# ------------------------------------------------------------------------------

set(CPACK_GENERATOR "ZIP")
set(CPACK_PACKAGE_FILE_NAME
    "${CMAKE_PROJECT_NAME}-${CMAKE_PROJECT_VERSION}-${GIT_SHORT_SHA}-${CMAKE_SYSTEM_NAME}-${CMAKE_BUILD_TYPE}-${CMAKE_CXX_COMPILER_ID}-${CMAKE_CXX_COMPILER_VERSION}"
)

include(CPack)
