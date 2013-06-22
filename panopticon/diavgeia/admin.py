# -*- coding: utf-8 *-*
from django.contrib import admin
from panopticon.diavgeia.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'typeof', 'source')
    list_filter = ('typeof', 'category')

admin.site.register(Transaction, TransactionAdmin)
