add_executable(task1 task1.cpp)
target_link_libraries(task1 PRIVATE project_options project_warnings)
target_link_system_libraries(task1 PRIVATE fmt::fmt)

package_project(TARGETS project_options project_warnings task1)
