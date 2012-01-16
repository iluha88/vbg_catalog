# -*- coding: utf-8 -*-
from firm_app.models import *
from django.contrib import admin


class RubricInline(admin.TabularInline):
    model=Rubric.firm.through
    extra=1

class AdressInline(admin.TabularInline):
    model = Adress.firm.through
    extra=1

class ContactInline(admin.TabularInline):
    model=Contact.firm.through
    extra=1

class FirmAdminm(admin.ModelAdmin):
    #filter_horizontal = ('Rubric',)
    inlines = [
        RubricInline, AdressInline, ContactInline
    ]

admin.site.register(Firm, FirmAdminm)
admin.site.register(Rubric)
admin.site.register(Adress)
admin.site.register(Contact)