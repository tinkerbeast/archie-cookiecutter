if(ARCHIE_ENABLE_GTEST)
  include(CTest)
  enable_testing()

  # Fetch and populate gtest during configuration
  include(FetchContent)
  # Google test v1.14
  FetchContent_Declare(
    googletest
    URL https://github.com/google/googletest/archive/f8d7d77c06936315286eb55f8de22cd23c188571.zip
  )
  # For Windows: Prevent overriding the parent project's compiler/linker settings
  set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
  FetchContent_MakeAvailable(googletest)

  include(GoogleTest)

  function(archie_cxx_gtest namespace target)
    if(NOT TARGET check)
        add_custom_target(check COMMAND ${CMAKE_CTEST_COMMAND})
    endif()
    archie_cxx_executable(${namespace} ${target} EXCLUDE_FROM_ALL ${ARGN})
    # TODO: combine link libraries and archie_cxx_executable
    target_link_libraries("${namespace}-${target}" PRIVATE GTest::gtest_main)
    add_dependencies(check "${namespace}-${target}")
    gtest_discover_tests("${namespace}-${target}")
    # TODO: remove gtest_add_tests in favour of gtest_discover_tests
    #gtest_add_tests(TARGET "${namespace}-${target}" TEST_PREFIX "${namespace}:")
  endfunction()

endif()
