library(random)
setClass("Borrower", slots=list(name="character"))
setClass("CorporateBorrower", representation(market_capitalization = "numeric"), contains = "Borrower")
setClass("PrivateBorrower", representation(annual_income = "numeric"), contains = "Borrower")

clist<-list()

for (i in 1:5){
  name <- toString(randomStrings(n=1, len=5, digits=FALSE, upperalpha=TRUE, loweralpha=FALSE, unique=TRUE, check=TRUE))
  m <- as.numeric(randomNumbers(n=1, min=1, col=1, max=1000000))
  c <- new("CorporateBorrower",name=name, market_capitalization=m)
  clist[[i]]<-c
}
  