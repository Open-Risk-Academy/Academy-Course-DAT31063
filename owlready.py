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
from owlready2 import *

ascii = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

onto = get_ontology("borrower.owl").load()

for c in onto.classes():
    print(c)

with onto:
    for i in range(5):
        alist = np.random.choice(ascii, size=5)
        name = ''.join(alist)
        c_borrower = onto.CorporateBorrower(name, market_capitalization=[np.random.randint(1, 1000000000)])

    for i in range(5):
        alist = np.random.choice(ascii, size=5)
        name = ''.join(alist)
        p_borrower = onto.PrivateBorrower(name, namespace=onto, annual_income=[np.random.randint(1, 100000)])

onto.save(file="borrower_instances.owl", format="rdfxml")
