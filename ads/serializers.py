from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import BooleanField
from ads.models import Ads, Categories, Selection
from ads.validators import not_true
from users.models import User


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    is_published = BooleanField(validators=[not_true], required=False)
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Ads
        fields = ['id', 'name', 'author', 'price', 'description', 'is_published', 'image', 'category']


class SelectionSerializer(ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field="username", read_only=True)

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["owner"] = request.user
        return super().create(validated_data)

    class Meta:
        model = Selection
        fields = "__all__"
