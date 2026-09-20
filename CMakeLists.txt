cmake_minimum_required(VERSION 3.20)
project(rimkeep LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()
add_compile_options(-Wall -Wextra -Wpedantic -fno-exceptions -fno-rtti)
add_executable(rimkeep-eval
  src/leapsec.cpp src/spice_daf.cpp src/ephemeris.cpp
  src/landing_eval.cpp src/lola_dem.cpp src/catalog.cpp src/cli.cpp)
target_include_directories(rimkeep-eval PRIVATE src)
