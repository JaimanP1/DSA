#include <iostream>

int testfunc(int n, int a, int b) {
    if (n == 0) {
        return a;
    }
    return testfunc(n - 1, b, a + b);
}

int main() {
    int input;
    std::cout << "Enter number: " << std::endl;
    std::cin >> input;
    
    int output = testfunc(input, 0, 1);
    std::cout << "Output: " << output << std::endl;
    
    return 0;
}

