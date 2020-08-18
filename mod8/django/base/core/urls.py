from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:data_id>/', views.update, name='update'),
    path('delete/<int:data_id>/', views.delete, name='delete' )
]