
cmake_minimum_required(VERSION 2.8.12)
project(annealing_helpers)
# Set source directory
set(SOURCE_DIR "src/annealing_helpers")
# Tell CMake that headers are also in SOURCE_DIR
include_directories(${SOURCE_DIR})
set(SOURCES "${SOURCE_DIR}/alpha_intersect.cpp")

add_subdirectory(lib/pybind11)
pybind11_add_module(alphacalc ${SOURCES} "${SOURCE_DIR}/bindings.cpp")