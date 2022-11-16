from rest_framework import serializers
from manager.models import App, Container

class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        exclude = ['app']


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        exclude = ['user']