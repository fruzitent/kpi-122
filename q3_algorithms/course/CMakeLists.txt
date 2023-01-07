cmake_minimum_required(VERSION 3.24)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_EXTENSIONS OFF)

set(ENABLE_DEVELOPER_MODE
    FALSE
    CACHE BOOL "Enable 'developer mode'")

set(OPT_WARNINGS_AS_ERRORS_DEVELOPER_DEFAULT FALSE)

include(FetchContent)

FetchContent_Declare(
  _project_options
  GIT_REPOSITORY https://github.com/aminya/project_options.git
  GIT_TAG v0.26.3)
FetchContent_MakeAvailable(_project_options)
include(${_project_options_SOURCE_DIR}/Index.cmake)

project(myproject VERSION 0.1.0)

set(GIT_SHA
    "Unknown"
    CACHE STRING "SHA this build was generated from")
string(SUBSTRING "${GIT_SHA}" 0 8 GIT_SHORT_SHA)

include(${_project_options_SOURCE_DIR}/src/DynamicProjectOptions.cmake)
dynamic_project_options(
  PCH_HEADERS
  <vector>
  <string>
  CPPCHECK_OPTIONS
  --enable=style,performance,warning,portability
  --inline-suppr
  --suppress=cppcheckError
  --suppress=internalAstError
  --suppress=unmatchedSuppression
  --suppress=passedByValue
  --suppress=syntaxError
  --inconclusive)

find_program(CPPLINT "cpplint")
if(CPPLINT)
  set(CMAKE_CXX_CPPLINT
      "${CPPLINT};--filter=-legal/copyright,-whitespace/indent,-whitespace/line_length;--quiet"
  )
endif()

target_compile_features(project_options INTERFACE cxx_std_${CMAKE_CXX_STANDARD})
add_library(myproject::project_options INTERFACE IMPORTED)
add_library(myproject::project_warnings INTERFACE IMPORTED)

include_directories(${CMAKE_SOURCE_DIR})
add_executable(main src/main.cpp)
target_link_libraries(main PUBLIC project_options project_warnings)

if(MSVC)
  get_all_installable_targets(all_targets)
  message("all_targets=${all_targets}")
  set_target_properties(
    ${all_targets} PROPERTIES VS_DEBUGGER_ENVIRONMENT
                              "PATH=$(VC_ExecutablePath_x64);%PATH%")
endif()
set_property(DIRECTORY PROPERTY VS_STARTUP_PROJECT main)

if(CMAKE_SKIP_INSTALL_RULES)
  return()
elseif(NOT PROJECT_IS_TOP_LEVEL)
  return()
endif()

package_project(TARGETS main project_options project_warnings)
set(CPACK_PACKAGE_FILE_NAME
    "${CMAKE_PROJECT_NAME}-${CMAKE_PROJECT_VERSION}-${GIT_SHORT_SHA}-${CMAKE_SYSTEM_NAME}-${CMAKE_BUILD_TYPE}-${CMAKE_CXX_COMPILER_ID}-${CMAKE_CXX_COMPILER_VERSION}"
)
include(CPack)
