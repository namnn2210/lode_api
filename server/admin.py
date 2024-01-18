from django.contrib import admin
from .models import Banking


# Register your models here.

class BankingAdmin(admin.ModelAdmin):
    list_display = ["user_name", "bank_name", "bank_number", "status", "created_at", "updated_at"]


admin.site.register(Banking,BankingAdmin)
