from django.urls import path
from . import views
urlpatterns = [
    # 회원가입
    path('', views.AccountsAPIView.as_view()),
]