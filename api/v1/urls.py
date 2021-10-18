from django.urls import path, include
from .views import FoodsView,CategoryView


urlpatterns = [
   path('foods/', FoodsView.as_view(), name='foods-list'),
   path('foods/<int:pk>/', FoodsView.as_view(), name='foods-one'),
   path('category/',CategoryView.as_view(),name='category-list'),
   path('category/<int:pk>/',CategoryView.as_view(),name='category-one'),
]