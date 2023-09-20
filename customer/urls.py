from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('', views.home, name='home'),
    path('them-moi/', views.add, name='add'),
    path('cap-nhat/<int:pk>/', views.update, name='update'),
    path('xoa/<int:pk>/', views.delete, name='delete'),
]
