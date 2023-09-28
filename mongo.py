"""
   Copyright 2022 - 2023 Open Risk (www.openriskmanagement.com)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

# This code accompanies the Open Risk Academy course "Class Inheritance in Data Science"
# https://www.openriskacademy.com/mod/book/view.php?id=720


import numpy as np
from mongoengine import *

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
