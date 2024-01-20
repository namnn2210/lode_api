from django.contrib import admin
from .models import Order
from authentication.models import UserProfile


# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone','code', 'balance', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('phone','code',)


class OrderAdmin(admin.ModelAdmin):
    list_display = (
    'user', 'order_date', 'city', 'mode', 'numbers', 'pay_number', 'total', 'win', 'result', 'note', 'status',
    'created_at', 'updated_at')
    list_filter = ('user', 'order_date', 'city', 'mode', 'win')
    search_fields = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Order, OrderAdmin)
