cmake_minimum_required(VERSION 3.7)
project(SLL)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp CMySLL.h CMyNode.h)
add_executable(SLL ${SOURCE_FILES})