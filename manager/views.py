from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from jdatetime import datetime
from manager.serializers import AppSerializer, ContainerSerializer
from manager.models import App, Container


class AppListCreateView(ListCreateAPIView):
    serializer_class = AppSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.app_set.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AppDetailUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = AppSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.app_set.all()