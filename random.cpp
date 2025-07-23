// mt19937_random.cpp
#include <iostream>
#include <random>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: ./mt19937_random <seed>\n";
        return 1;
    }

    unsigned int seed = std::stoul(argv[1]);
    std::mt19937 gen(seed);

    for (int i = 0; i < 10; ++i) {
        std::cout << gen() << " ";
    }

    std::cout << std::endl;
    return 0;
}
