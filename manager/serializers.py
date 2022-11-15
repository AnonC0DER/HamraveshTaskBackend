from rest_framework import serializers
from manager.models import App, Container

class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        exclude = ['app']


class AppSerializer(serializers.ModelSerializer):
    containers = serializers.SerializerMethodField()

    class Meta:
        model = App
        exclude = ['user']

    def get_containers(self, app):
        '''Returns all containers'''
        containers = app.container_set.all()
        serializer = ContainerSerializer(containers, many=True)
        return serializer.data