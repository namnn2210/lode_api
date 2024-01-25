from django.contrib import admin
from .models import NotificationCategoryModel, NotificationModel


# Register your models here.

class NotificationCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "status", "created_at", "updated_at"]


class NotificationAdmin(admin.ModelAdmin):
    list_display = ["category", "user", "title", "content", "status", "created_at", "updated_at"]
    search_fields = ["content", ]
    list_filter = ["category", "user", ]


admin.site.register(NotificationCategoryModel, NotificationCategoryAdmin)
admin.site.register(NotificationModel, NotificationAdmin)
