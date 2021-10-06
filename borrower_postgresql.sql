create TABLE borrower (
                        name            text
);

create TABLE corporate_borrower (
    market_capitalisation           float
) INHERITS (borrower);

create TABLE private_borrower (
    annual_income float
) INHERITS (borrower);