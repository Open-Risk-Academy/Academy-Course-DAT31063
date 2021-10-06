from django.contrib import admin
from .models import CorporateBorrower, PrivateBorrower


@admin.register(CorporateBorrower)
class RequestDemoAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = ('name', 'market_capitalisation')


@admin.register(PrivateBorrower)
class RequestDemoAdmin(admin.ModelAdmin):
    save_as = True
    view_on_site = False
    list_display = ('name', 'annual_income')
