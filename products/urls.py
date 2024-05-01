from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductAPIView.as_view()),
    path('<int:product_id>/', views.ProductAPIView.as_view()),
]