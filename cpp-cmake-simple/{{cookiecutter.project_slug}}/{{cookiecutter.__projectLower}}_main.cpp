#include "{{cookiecutter.__projectLower}}.h"

#include <iostream>

int main() {
    {{cookiecutter.__cppNamespace}}::{{cookiecutter.project}} obj;
    std::cout << "2 + 3 = " << obj.add(2, 3) << std::endl;
    return EXIT_SUCCESS;
}
