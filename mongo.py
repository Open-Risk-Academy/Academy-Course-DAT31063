from mongoengine import *
import numpy as np

connect('test')

ascii = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')


class Borrower(Document):
    name = StringField(max_length=200, required=True)
    meta = {'allow_inheritance': True}


class CorporateBorrower(Borrower):
    market_capitalisation = FloatField()


class PrivateBorrower(Borrower):
    annual_income = FloatField()


for i in range(5):
    alist = np.random.choice(ascii, size=5)
    name = ''.join(alist)
    c_borrower = CorporateBorrower(name=name, market_capitalisation=np.random.randint(1, 1000000000))
    c_borrower.save()

for i in range(5):
    alist = np.random.choice(ascii, size=5)
    name = ''.join(alist)
    p_borrower = PrivateBorrower(name=name, annual_income=np.random.randint(1, 100000))
    p_borrower.save()

print(Borrower.objects().count())
