# 
#    Copyright 2022 - 2023 Open Risk (www.openriskmanagement.com)
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0
# 
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


# This code accompanies the Open Risk Academy course "Class Inheritance in Data Science"
# https://www.openriskacademy.com/mod/book/view.php?id=720

# the random package has to be installed. depending on your system you may need to install additional
# libraries

# install.packages("curl")
# install.packages("random")

library(random)

# create base class
setClass("Borrower", slots = list(name = "character"))

# create derived classes
setClass("CorporateBorrower", representation(market_capitalization = "numeric"), contains = "Borrower")
setClass("PrivateBorrower", representation(annual_income = "numeric"), contains = "Borrower")

clist <- list()

# create sample of cororate borrowers
for (i in 1:5){
  name <- toString(randomStrings(n = 1, len = 5, digits = FALSE, upperalpha = TRUE, loweralpha = FALSE, unique = TRUE, check = TRUE))
  m <- as.numeric(randomNumbers(n = 1, min = 1, col = 1, max = 1000000))
  c <- new("CorporateBorrower",name=name, market_capitalization=m)
  clist[[i]] <- c
}

