from django.contrib import admin
from .models import UserProfile


# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'balance', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('phone',)


admin.site.register(UserProfile, UserProfileAdmin)
