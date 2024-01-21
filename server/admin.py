from django.contrib import admin
from .models import Banking, BalanceTransaction


# Register your models here.

class BankingAdmin(admin.ModelAdmin):
    list_display = ["user_name", "bank", "bank_number", "status", "created_at", "updated_at"]


class BalanceTransactionAdmin(admin.ModelAdmin):
    list_display = ["user", "transaction_type", "description", "amount", "status", "created_at", "updated_at"]
    list_filter = ["user", "transaction_type", ]


admin.site.register(Banking, BankingAdmin)
admin.site.register(BalanceTransaction, BalanceTransactionAdmin)
