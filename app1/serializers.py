from rest_framework import serializers
from .models import *

class SavolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savol
        fields = '__all__'

class JavobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Javob
        fields = "__all__"
