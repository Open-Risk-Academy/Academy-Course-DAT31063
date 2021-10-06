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
