from django.contrib import admin

from .models import ModelOne, ModelTwo


@admin.register(ModelOne)
class ModelTwoAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(ModelTwo)
class ModelTwoAdmin(admin.ModelAdmin):
    autocomplete_fields = ["model_one"]
