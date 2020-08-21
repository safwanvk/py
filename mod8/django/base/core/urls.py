from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:data_id>/', views.update, name='update'),
    path('delete/<int:data_id>/', views.delete, name='delete' ),
    path('register/', views.register_view, name='register'),
    path('', include('django.contrib.auth.urls'), name='login')
]
