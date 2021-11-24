from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Recipes


class RecipesSerializer(ModelSerializer):

    class Meta:
        model = Recipes
        fields = ("pk","name", "description","image","price","category","amount",)


