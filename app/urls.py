from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('project/<int:id>', views.project, name='project'),
]

