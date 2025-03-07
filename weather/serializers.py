from rest_framework import serializers
from .models import Weather


class weatherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)


class weatherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = "__all__"

    def get(request):
        data = Weather.objects.all()
        print(data)
        return data
