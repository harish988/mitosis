from rest_framework import serializers
from .models import Model, Upload

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = "__all__"