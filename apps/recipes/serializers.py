from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Recipes


class RecipesSerializer(ModelSerializer):

    name = serializers.CharField(
        required=True,
    )
    description = serializers.CharField(
        required=True,
    )
    image = serializers.EmailField(
        required=True,
    )
    price = serializers.CharField(
        write_only=True,
        required=True,
    )

    category = serializers.CharField(write_only=True, required=True)
    amount = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Recipes
        fields = ("name", "description","image","price","category","amount",)

    def get_recipes(self, instance):
        request = self.context["request"]
        query_recipes = request.query_params.get("Recipes", "")
        recipes = Recipes.availables

        return recipes.data

    def create(self, validated_data):
        recipe = Recipes.objects.create_recipe(
            name=validated_data["name"],
            description=validated_data["description"],
            image=validated_data["image"],
            price=validated_data["price"],
            category=validated_data["category"],
            amount=validated_data["amount"]
        )
        return recipe
