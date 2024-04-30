from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views
urlpatterns = [
    # 회원가입
    path('', views.AccountsAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('<str:username>/', views.AccountsAPIView.as_view()),
]