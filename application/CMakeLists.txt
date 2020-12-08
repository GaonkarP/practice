cmake_minimum_required(VERSION 3.10)

# set the project name
project(Mytest)

# add the executable
add_executable("${PROJECT_NAME}" "src/main.c" "src/hello.c" "src/armstrong.c")

target_include_directories("${PROJECT_NAME}" PUBLIC "C:/GAP7KOR/Repo/myproject/Repo/practice/application/inc")

install (TARGETS "${PROJECT_NAME}" DESTINATION bin)     #"${CMAKE_INSTALL_PREFIX}/bin"
install (FILES "${PROJECT_NAME}" DESTINATION src)       #"${CMAKE_INSTALL_PREFIX}/src"