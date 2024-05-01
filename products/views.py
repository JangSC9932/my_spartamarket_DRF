from rest_framework import status
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
from .models import Product
from django.shortcuts import get_object_or_404


class ProductAPIView(APIView):
    @staticmethod
    def post(request):
        if request.user.is_authenticated:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=request.user)
                return Response("물품등록 성공", status=status.HTTP_201_CREATED)
        else:
            return Response("로그인이 필요합니다.", status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def get(request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request, product_id):
        if request.user.is_authenticated:
            product = get_object_or_404(Product, pk=product_id)

            if product.author != request.user:
                return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)

            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response("수정 성공", status=status.HTTP_200_OK)
        else:
            return Response("로그인이 필요합니다.", status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def delete(request, product_id):
        if request.user.is_authenticated:
            product = get_object_or_404(Product, pk=product_id)

            if product.author != request.user:
                return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)

            product.delete()
            return Response("삭제 성공", status=status.HTTP_200_OK)
        else:
            return Response("로그인이 필요합니다.", status=status.HTTP_401_UNAUTHORIZED)