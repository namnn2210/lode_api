from django.contrib import admin
from .models import Bank


# Register your models here.
class BankAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'code', 'bin', 'short_name')
    list_filter = ('bin',)
    search_fields = ('code',)


admin.site.register(Bank, BankAdmin)
