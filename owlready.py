from owlready2 import *

import numpy as np

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
