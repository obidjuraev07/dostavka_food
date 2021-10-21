from django.urls import path, include
from .views import dashboard,foods_list

urlpatterns = [
   path('', dashboard, name='dashboard'),
   path('foods/', foods_list, name='list-foods'),

]