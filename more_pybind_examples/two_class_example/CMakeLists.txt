# use: cmake -DPYBIND11_PYTHON_VERSION=3.9.7 .

cmake_minimum_required(VERSION 3.18.2)
set (CMAKE_CXX_STANDARD 17)
project(pybind_multithreading VERSION 0.1.0)

# comment out below line if using pybind
# add_executable(more_pybind_multithreading main.cpp)

add_subdirectory(extern/pybind11)
pybind11_add_module(pybind_multithreading main.cpp)

