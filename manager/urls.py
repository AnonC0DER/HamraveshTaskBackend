from django.urls import path
from manager.views import AppListCreateView, AppDetailUpdateDestroyView, ContainerListView

urlpatterns = [
    path('app/', AppListCreateView.as_view()),
    path('app/<int:pk>/', AppDetailUpdateDestroyView.as_view()),
    # path('app/run/<int:pk>/', RunAppView.as_view()),
    # path('app/get_history/<id>/', AppHistoryView.as_view()),

    path('app/<int:pk>/containers/', ContainerListView.as_view()),
]