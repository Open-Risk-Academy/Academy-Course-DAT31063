#include <iostream>
#include "Borrower.h"
#include "PrivateBorrower.h"
#include "CorporateBorrower.h"

int main(int argc, char *argv[]) {

     CorporateBorrower c_borrower;
     c_borrower.setName("Corporate Name");
     c_borrower.setMarket_capitalization(10000);

     std::cout << c_borrower.getName() << std::endl;

    return 0;
}