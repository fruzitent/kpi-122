cmake_minimum_required(VERSION 3.21)
project(q2_algorithms@p07)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_program(CPPLINT "cpplint")
if (CPPLINT)
    set(CMAKE_CXX_CPPLINT "${CPPLINT};--quiet")
endif ()

if (MSVC)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /FS")
endif ()

include_directories(${CMAKE_SOURCE_DIR})
add_executable(task1 src/task1.cpp)
add_executable(task2 src/task2.cpp)
