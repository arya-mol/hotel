from rest_framework.serializers import ModelSerializer
from menuapi.models import CoursesOfMeals
from rest_framework import serializers

class MenuSerializers(ModelSerializer):
    class Meta:
        model = CoursesOfMeals
        fields ="__all__"