import docker
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from jdatetime import datetime
from manager.serializers import AppSerializer, ContainerSerializer
from manager.models import App, Container

class AppListCreateView(ModelViewSet):
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


class AppDetailUpdateDestroyView(ModelViewSet):
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


class AppHistoryView(ModelViewSet):
    '''
        Returns changes history of an app 
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = AppSerializer
    queryset = App.objects.all()
    
    def retrieve(self, request, pk):
        app = get_object_or_404(App, id=pk)
        return Response(app.get_history, 200)


class RunAppView(ModelViewSet):
    '''
        Run an app,
        last_run will be automatically change after each run request,
        full_docker_command will be automatically set after each run request. 
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = ContainerSerializer
    queryset = Container.objects.all()

    def retrieve(self, request, pk):
        app = get_object_or_404(App, id=pk)
        container = Container.objects.create(app=app, name=app.image, status='running')
        serializer = ContainerSerializer(container, many=False)
        
        # This part should be a celery task
        client = docker.from_env()
        user_container = client.containers.run(app.image, app.command, detach=True)
        user_container.reload()
        
        container.status = 'finished' if user_container.status == 'exited' else 'running'
        print(user_container.status)
        app.last_run = datetime.now()
        container.save()
        app.save()
        return Response(serializer.data, 200)


class ContainerListView(ModelViewSet):
    '''
        GET : Returns all the containers connected to the app
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = ContainerSerializer

    def get_queryset(self):
        return Container.objects.filter(app__id=self.kwargs.get('pk'))