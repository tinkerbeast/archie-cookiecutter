{{cookiecutter.project}}
===========

This is boilerplate code generated by archie code scaffolding system based on the `{{cookiecutter._archetype}}` archetype.

Build behaviour modifying flags
-------------------------------

### ARCHIE_BUILD_TYPE

This replaces the `CMAKE_BUILD_TYPE` and provies the same functionality. It also provides additional build types like "Coverage". If `ARCHIE_BUILD_TYPE` is not set, it takes the value from `CMAKE_BUILD_TYPE`. By default `ARCHIE_BUILD_TYPE` is set to "Debug".

### ARCHIE_ENABLE_GTEST

This enables unit testing targets and dependencies for the build. Currently the only unit testing framework integrated is `GoogleTest`. The reason this exists a configuration flag and not just a build target is to keep test dependencies optional.

Archie make targets
-------------------

### all

Default make target which builds libraries and executables. This target is augmented by setting `ARCHIE_BUILD_TYPE=Coverage`, in which case all libraries and executables are instrumented with coverage code and linked with coverage libraries.

### test

Run the test executables via CTest. See https://cmake.org/cmake/help/latest/manual/ctest.1.html for CTest command line options. The `test` target is only available with `ARCHIE_ENABLE_GTEST=ON`. Note that the **binaries must already be built before invcation**.

### check

Build tests and run them. This target is only available with `ARCHIE_ENABLE_GTEST=ON`.

### clean

Removes all output files (libraries, executables, test executables, generated files, etc).

### coverage

Generates code coverage report for The coverage instrumented executables need to be run before this target so that the Gcov data files are already generated. This target is only available when `ARCHIE_BUILD_TYPE=Coverage` is set and `lcov` tool is present.

### docs

Gererates API documentaion present in sources with the help of `doxygen`. Target will not be available without `doxygen` tool present.

### site

Generates additional documentation based on README file and docs folder. The target requires Sphinx docuemntation generation tool with MySt plugin to be available. 

