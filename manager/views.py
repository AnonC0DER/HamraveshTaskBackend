from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from jdatetime import datetime
from manager.serializers import AppSerializer, ContainerSerializer
from manager.models import App, Container

class AppListCreateView(ListCreateAPIView):
    '''
        POST : Create an app, (needs to be authorized)
        GET : Returns all apps created by the user
    '''
    serializer_class = AppSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.app_set.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AppDetailUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    '''
        GET : Returns app details
        PUT : Update the app
        PATCH : Update a specific field of the app
        DELETE : Delete the app and its containers
    '''
    serializer_class = AppSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.app_set.all()


class AppHistoryView(APIView):
    '''
        Returns changes history of an app 
    '''
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        app = App.objects.get(id=pk)
        return Response(app.get_history, 200)


class RunAppView(APIView):
    '''
        Run an app,
        last_run will be automatically change after each run request,
        full_docker_command will be automatically set after each run request. 
    '''
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        app = get_object_or_404(App, id=pk)
        container = Container.objects.create(app=app, name=app.image, status='running')
        serializer = ContainerSerializer(container, many=False)
        app.last_run = datetime.now()
        app.save()
        return Response(serializer.data, 200)


class ContainerListView(APIView):
    '''
        GET : Returns all the containers connected to the app
    '''
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        containers = Container.objects.filter(app__id=pk)
        serializer = ContainerSerializer(containers, many=True)
        return Response(serializer.data, 200)