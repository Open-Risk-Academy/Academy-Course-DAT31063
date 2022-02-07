-- Concrete Table Inheritance
CREATE TABLE Borrower3 (
    Name varchar(255)
);

CREATE TABLE CorporateBorrower3 (
    Name varchar(255),
    MarketCapitalisation numeric (10,3)
);

CREATE TABLE PrivateBorrower3 (
    Name varchar(255),
    AnnualIncome numeric (10,3)
);