from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
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
            return Response("SUCCESS CREATE USER", status=status.HTTP_201_CREATED)

    @staticmethod
    def get(request, username):
        user = User.objects.filter(username=username).first()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileAPIView(APIView):

    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, username):
        user = User.objects.filter(username=username).first()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)







