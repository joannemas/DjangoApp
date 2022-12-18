from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('view/', views.view, name='view'),
    path('view/<id>', views.detail, name='detail'),
    path('update/<id>', views.update, name='update'),
    path('delete/<id>', views.delete, name='delete'),
]