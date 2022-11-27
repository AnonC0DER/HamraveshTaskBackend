from django.urls import path
from manager.views import AppListCreateView, AppDetailUpdateDestroyView, \
    ContainerListView, AppHistoryView, RunAppView

urlpatterns = [
    path('app/', AppListCreateView.as_view({'get': 'list', 'post' : 'create'})),
    path('app/<int:pk>/', AppDetailUpdateDestroyView.as_view({'get' : 'retrieve', 'put': 'update', 'patch' : 'partial_update', 'delete' : 'destroy'})),
    path('app/run/<int:pk>/', RunAppView.as_view({'get' : 'retrieve'})),
    path('app/get_history/<int:pk>/', AppHistoryView.as_view({'get' : 'retrieve'})),

    path('app/<int:pk>/containers/', ContainerListView.as_view({'get': 'list'})),
]