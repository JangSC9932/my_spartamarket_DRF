from rest_framework import status
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
from .models import Product
from django.shortcuts import get_object_or_404


class ProductAPIView(APIView):

    # 로그인 에러 Response
    login_rquired_response = {
        'code': status.HTTP_401_UNAUTHORIZED,
        'message': 'LOGIN REQUIRED',
    }

    # 권한 에러 Response
    permission_denied_response = {
        'code': status.HTTP_403_FORBIDDEN,
        'message': 'Permission denied.'
    }

    # 게시글 등록
    def post(self, request):
        # 로그인 체크
        if request.user.is_authenticated:
            serializer = ProductSerializer(data=request.data)
            # 데이터 체크
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=request.user)

                response = {
                    'code': status.HTTP_201_CREATED,
                    'message': 'PRODUCT CREATED SUCCESSFULLY',
                    'data': serializer.data
                }

                return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(self.login_rquired_response, status=status.HTTP_401_UNAUTHORIZED)

    # 게시글 목록
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 게시글 수정
    def put(self, request, product_id):
        # 로그인 체크
        if request.user.is_authenticated:
            product = get_object_or_404(Product, pk=product_id)

            # 작성자 체크
            if product.author != request.user:
                return Response(self.permission_denied_response, status=status.HTTP_403_FORBIDDEN)

            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                response = {
                    'code': status.HTTP_200_OK,
                    'message': 'PRODUCT UPDATED SUCCESSFULLY',
                    'data': serializer.data
                }

                return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(self.login_rquired_response, status=status.HTTP_401_UNAUTHORIZED)

    # 게시글 삭제
    def delete(self, request, product_id):
        # 로그인 체크
        if request.user.is_authenticated:
            product = get_object_or_404(Product, pk=product_id)

            # 작성자 체크
            if product.author != request.user:
                return Response(self.permission_denied_response, status=status.HTTP_403_FORBIDDEN)
            product.delete()

            response = {
                'code': status.HTTP_204_NO_CONTENT,
                'message': 'PRODUCT DELETED SUCCESSFULLY',
            }

            return Response(response, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(self.login_rquired_response, status=status.HTTP_401_UNAUTHORIZED)