import numpy as np
import json

ascii = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')


class Borrower:
    def __init__(self):
        self._name = None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, a: str):
        self._name = a


class CorporateBorrower(Borrower):
    def __init__(self):
        super().__init__()
        self._market_capitalization = None

    @property
    def market_capitalization(self) -> float:
        return self._market_capitalization

    @market_capitalization.setter
    def market_capitalization(self, a: float):
        self._market_capitalization = a


class PrivateBorrower(Borrower):
    def __init__(self):
        super().__init__()
        self._annual_income = None

    @property
    def annual_income(self) -> float:
        return self._annual_income

    @annual_income.setter
    def annual_income(self, a: float):
        self._annual_income = a


def main():
    print('Object Inheritance in Python')
    print(80 * '=')

    clist = []
    for i in range(5):
        alist = np.random.choice(ascii, size=5)
        name = ''.join(alist)
        c_borrower = CorporateBorrower()
        c_borrower.name = name
        c_borrower.market_capitalization = np.random.randint(1, 1000000000)
        clist.append(c_borrower.__dict__)
        print(c_borrower.name, c_borrower.market_capitalization)

    plist = []
    for i in range(5):
        alist = np.random.choice(ascii, size=5)
        name = ''.join(alist)
        p_borrower = PrivateBorrower()
        p_borrower.name = name
        p_borrower.annual_income = np.random.randint(1, 100000)
        # p_borrower.market_capitalization = 'This is wrong but it goes through'
        # print(p_borrower.name, p_borrower.annual_income, p_borrower.market_capitalization)
        plist.append(p_borrower.__dict__)
        print(p_borrower.name, p_borrower.annual_income)

    json.dump(clist, open('corporate_borrower.json', mode='w'))
    json.dump(plist, open('private_borrower.json', mode='w'))


if __name__ == "__main__":
    main()
