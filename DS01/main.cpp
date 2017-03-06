#include <iostream>
#ifdef _WIN32
#include <cstdlib>
#endif

int main() {
    std::cout << "Hello, World!" << std::endl;
    std::cout << "Hello, World!" << std::endl;
    std::cout << "Hello, World!" << std::endl;
	std::cout << "Hello, World!" << std::endl;
	std::cout << "Hello, World!" << std::endl;
#ifdef _WIN32
    system("pause");
#endif
    return 0;
}