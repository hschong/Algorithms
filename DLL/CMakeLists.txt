cmake_minimum_required(VERSION 3.7)
project(DLL)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp CMyDLL.cpp CMyDLL.h)
add_executable(DLL ${SOURCE_FILES})