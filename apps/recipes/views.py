from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from apps.recipes.models import Recipes
from .serializers import RecipesSerializer


class RecipesRetrieveView(ListAPIView):
    queryset = Recipes.availables.all()
    serializer_class = RecipesSerializer
