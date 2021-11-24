from django.contrib import admin
from .models import Recipes

# Register your models here.
@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ("name", "description", "image","price", "category", "amount",
                       "published_at", "archived_at", "deleted_at")
        }),
    )

    list_display = ("pk","name", "description", "image","price", "category", "amount",
                       "published_at", "archived_at", "deleted_at")


