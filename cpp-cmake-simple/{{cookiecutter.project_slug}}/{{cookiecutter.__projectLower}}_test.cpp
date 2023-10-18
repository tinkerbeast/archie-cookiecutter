#include "{{cookiecutter.__projectLower}}.h"
#include "gtest/gtest.h"

TEST({{cookiecutter.project}}, sum_zero)
{
  {{cookiecutter.__cppNamespace}}::{{cookiecutter.project}} obj;
  ASSERT_EQ(obj.add(1, -1), 0);
}

TEST({{cookiecutter.project}}, sum_five)
{
  {{cookiecutter.__cppNamespace}}::{{cookiecutter.project}} obj;
  ASSERT_EQ(obj.add(2, 3), 5);
}

