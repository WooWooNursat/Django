from django.urls import path
from main import views

urlpatterns = [
    path('', views.TodoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:id>/', views.TodoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete'})),
    path('<int:id>/tasks/completed/', views.TaskViewSet.as_view({'get': 'list_marked'})),
    path('<int:id>/tasks/', views.TaskViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:id>/tasks/<int:id2>/', views.TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete'}))
]