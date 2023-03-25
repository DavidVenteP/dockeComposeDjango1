from django.contrib import admin
from .models import feature_item
# Register your models here.
@admin.register(feature_item)
class Feature_ItemsAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "description", "icon")
    search_filter = ("pk", "title", "icon")
    search_fields = ("pk", "title", "icon")
    ordering = ("-pk",)