#ifndef {{cookiecutter.__cppHeaderGuard}}_H_
#define {{cookiecutter.__cppHeaderGuard}}_H_

/**
 * This file has all the implementation details for the
 * {{cookiecutter.project}} class.
 */

namespace {{cookiecutter.__cppNamespace}} {

/**
 * A simple class to do calculation on integers.
 */
class {{cookiecutter.project}} {

public:
    /**
     * A mentod which add two integers.
     *
     * @param[in] a The first number to be added.
     * @param[in] b The second number to be added.
     * @return The sum of the two numbers.
     */
    int add(int a, int b) const;
};

} // namespace {{cookiecutter.__cppNamespace}}

#endif  // {{cookiecutter.__cppHeaderGuard}}_H_
