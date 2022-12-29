"""
   Copyright 2022 Open Risk (www.openriskmanagement.com)

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

from django.db import models


class Borrower(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class CorporateBorrower(Borrower):
    market_capitalisation = models.FloatField()

    class Meta:
        verbose_name = "Corporate Borrower"

    verbose_name_plural = "Corporate Borrowers"


class PrivateBorrower(Borrower):
    annual_income = models.FloatField()

    class Meta:
        verbose_name = "Private Borrower"

    verbose_name_plural = "Private Borrowers"
