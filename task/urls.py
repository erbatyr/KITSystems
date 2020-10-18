from django.urls import path

from django.urls import include

from . import views





urlpatterns = [
    path('', views.AllTasks.as_view(), name='index'),
    path('<int:pk>/', views.TaskDetail.as_view(), name='detail'),
    path('new_task/', views.TaskCreate.as_view(), name='new_task'),
    path('<int:pk>/edit', views.TaskEdit.as_view(), name='edit'),
    path('<int:pk>/delete/', views.TaskDelete.as_view(), name='delete'),
]