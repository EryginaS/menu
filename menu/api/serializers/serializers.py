from rest_framework import serializers

from position.models import Position, Category, Allergen


class AllergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergen
        fields = "name"


class PositionSerializer(serializers.ModelSerializer):
    allergens = AllergenSerializer(read_only=True, many=True)

    class Meta:
        model = Position
        fields = [
            "name",
            "image",
            "price",
            "proteins",
            "fats",
            "carbohydrates",
            "calories",
            "allergens",
            "category"
        ]
