from django.urls import path
from apps.recipes.views import RecipesRetrieveView

urlpatterns = [
    path("recipes/", RecipesRetrieveView.as_view(),
         name="recipes")
]
