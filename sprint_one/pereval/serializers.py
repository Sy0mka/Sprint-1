from rest_framework import serializers
from .models import PerevalAdded, PerevalImages
import base64

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = ['img']

    def to_internal_value(self, data):
        # Конвертируем base64 в bytes
        return {'img': base64.b64decode(data['img'])}

class PerevalAddedSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = PerevalAdded
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        pereval = PerevalAdded.objects.create(**validated_data)
        for image_data in images_data:
            PerevalImages.objects.create(pereval=pereval, **image_data)
        return pereval