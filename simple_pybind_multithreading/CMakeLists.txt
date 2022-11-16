cmake_minimum_required(VERSION 3.4.0)
set (CMAKE_CXX_STANDARD 17)
project(pybind_multithreading VERSION 0.1.0)


# add_executable(pybind_multithreading main.cpp)

add_subdirectory(extern/pybind11)
pybind11_add_module(pybind_multithreading main.cpp)

