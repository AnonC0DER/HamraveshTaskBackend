from rest_framework import serializers
from manager.models import App, Container

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        exclude = ['user']
        read_only_fields = ['full_docker_command']


class ContainerSerializer(serializers.ModelSerializer):
    app = AppSerializer(many=False)

    class Meta:
        model = Container
        fields = '__all__'