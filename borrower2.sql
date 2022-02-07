-- Class Table Inheritance
CREATE TABLE Borrower2 (
    Name varchar(255)
);

CREATE TABLE CorporateBorrower2 (
    MarketCapitalisation numeric (10,3)
);

CREATE TABLE PrivateBorrower2 (
    AnnualIncome numeric (10,3)
);