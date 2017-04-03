cmake_minimum_required(VERSION 3.7)
project(RandomBinaryTree)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp CLinkedQueue.cpp CLinkedQueue.h CMySLL.cpp CMySLL.h)
add_executable(RandomBinaryTree ${SOURCE_FILES})