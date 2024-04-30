from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class AccountsAPIView(APIView):

    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("회원가입 성공", status=status.HTTP_201_CREATED)

    @staticmethod
    def get(request, username):
        if request.user.is_authenticated:
            user = User.objects.filter(username=username).first()
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("로그인이 필요합니다.", status=status.HTTP_401_UNAUTHORIZED)







