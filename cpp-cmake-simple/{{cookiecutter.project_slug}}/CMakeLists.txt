project({{cookiecutter.__cmakeNamespace}}-{{cookiecutter.__projectLower}}
    DESCRIPTION "{{cookiecutter.project_desc}}"
    LANGUAGES CXX)
cmake_minimum_required(VERSION 3.21.7)


{% include "defaults.cmake" %}

{% include "builds.cmake" %}

{% include "gtest.cmake" %}

{% include "docs.cmake" %}

# === Adding project wide settings============================================

# Set global properties (WARNING: Only to be done at top level CMake file)
set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE ${ARCHIE_COMPILER_CACHE})
#set_property(GLOBAL PROPERTY RULE_LAUNCH_LINK ${ARCHIE_LINKER_CACHE}) # linker cache disabled because of no major speed improvements

# Set directory scope variables which affect target properties
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


# === Adding individual libraries =============================================

archie_cxx_library("{{cookiecutter.__cmakeNamespace}}" "{{cookiecutter.__projectLower}}"
  SRCS ${CMAKE_CURRENT_SOURCE_DIR}/{{cookiecutter.__projectLower}}.cpp
  HDRS_PUBL ${CMAKE_CURRENT_SOURCE_DIR}/{{cookiecutter.__projectLower}}.h
  INCLS_PUBL ${CMAKE_CURRENT_SOURCE_DIR}/
  COPTS_PRIV ${ARCHIE_CXX_COPTS}
)

archie_cxx_executable("{{cookiecutter.__cmakeNamespace}}" "{{cookiecutter.__projectLower}}-main"
  SRCS ${CMAKE_CURRENT_SOURCE_DIR}/{{cookiecutter.__projectLower}}_main.cpp
  DEPS_PRIV {{cookiecutter.__cmakeNamespace}}::{{cookiecutter.__projectLower}}
  COPTS_PRIV ${ARCHIE_CXX_COPTS}
)

if(ARCHIE_ENABLE_GTEST)
  archie_cxx_gtest("{{cookiecutter.__cmakeNamespace}}" "{{cookiecutter.__projectLower}}-test"
    SRCS ${CMAKE_CURRENT_SOURCE_DIR}/{{cookiecutter.__projectLower}}_test.cpp
    DEPS_PRIV {{cookiecutter.__cmakeNamespace}}::{{cookiecutter.__projectLower}}
    COPTS_PRIV ${ARCHIE_CXX_COPTS}
  )
endif()

if(DOXYGEN_FOUND)
  doxygen_add_docs(docs
      "include" "src"
      COMMENT "ARCHIE: Doxygen found and custom target `docs` added")
endif()
if(ARCHIE_SPHINX_FOUND)
  archie_sphinx_add_docs(site
      "docs"
      COMMENT "ARCHIE: Sphinx found and custom target `site` added")
endif()
