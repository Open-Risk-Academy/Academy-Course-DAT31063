cmake_minimum_required(VERSION 3.19)
project(Academy_Course_DAT31063)
set(CMAKE_CXX_STANDARD 17)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

conan_basic_setup()

include_directories(.)

add_executable(Academy_Course_DAT31063 Borrower.h main.cpp)

## set the POCO paths and libs
#set(POCO_PREFIX "/usr/local") # the directory containing "include" and "lib"
#set(POCO_INCLUDE_DIR"${POCO_PREFIX}/include")
#
## Manually installed shared libraries
#set(POCO_LIB_DIR "${POCO_PREFIX}/lib")
#
## System installed shared libraries (Ubuntu Trusty)
## TODO Too old (missing JSON)
## Explore newer images
## set(POCO_LIB_DIR /usr/lib)
#
#set(POCO_LIBS
#        "${POCO_LIB_DIR}/libPocoNet.so"
#        "${POCO_LIB_DIR}/libPocoUtil.so"
#        "${POCO_LIB_DIR}/libPocoJSON.so"
#        "${POCO_LIB_DIR}/libPocoNetSSL.so"
#        "${POCO_LIB_DIR}/libPocoFoundation.so")

target_link_libraries(Academy_Course_DAT31063 ${CONAN_LIBS})