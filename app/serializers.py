from rest_framework import serializers
from .models import News


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class EmailSendSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    comment = serializers.CharField()
