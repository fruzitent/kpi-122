add_executable(main main.cpp)
target_link_libraries(main PRIVATE project_options project_warnings)
target_link_system_libraries(main PRIVATE fmt::fmt)

package_project(TARGETS project_options project_warnings main)
