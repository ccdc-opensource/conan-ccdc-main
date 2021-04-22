cmake_minimum_required(VERSION 3.1)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(Fontconfig REQUIRED)
find_package(openscenegraph REQUIRED)
find_package(csdprotobufs REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example Fontconfig::Fontconfig)
target_link_libraries(example openscenegraph::openscenegraph)
target_link_libraries(example csdprotobufs::csdprotobufs)
set_target_properties(example PROPERTIES CXX_STANDARD 17)
