cmake_minimum_required(VERSION 4.0)

project(withHeader)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

set(SOURCES
src/main.cpp
src/hello.cpp)

add_executable(${PROJECT_NAME} ${SOURCES})