from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class AccountsAPIView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            response = {
                'code': status.HTTP_201_CREATED,
                'message': 'Registered successfully',
                'data': serializer.data,
            }

            return Response(response, status=status.HTTP_201_CREATED)

    def get(self, request, username):
        if request.user.is_authenticated:
            user = User.objects.filter(username=username).first()
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:

            response = {
                'code': status.HTTP_401_UNAUTHORIZED,
                'message': 'LOGIN REQUIRED',
            }

            return Response(response, status=status.HTTP_401_UNAUTHORIZED)







