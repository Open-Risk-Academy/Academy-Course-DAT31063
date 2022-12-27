cmake_minimum_required(VERSION 3.19)
project(Academy_Course_DAT31063)
set(CMAKE_CXX_STANDARD 17)

add_executable(main
    Borrower.h
    CorporateBorrower.h
    PrivateBorrower.h
    Borrower.cpp
    CorporateBorrower.cpp
    PrivateBorrower.cpp
    main.cpp)

