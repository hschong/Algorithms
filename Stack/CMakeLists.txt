cmake_minimum_required(VERSION 3.7)
project(Stack)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp CMyStack.cpp CMyStack.h CMySLL.cpp CMySLL.h)
add_executable(Stack ${SOURCE_FILES})