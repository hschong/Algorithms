cmake_minimum_required(VERSION 3.7)
project(RandomBinaryTreeForBFS)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp CMyRandomBinaryTree.cpp CMyRandomBinaryTree.h CNodeForRBT.cpp
        CNodeForRBT.h)
add_executable(RandomBinaryTreeForBFS ${SOURCE_FILES})