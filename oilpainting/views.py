from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from oilpainting import serializers
from oilpainting.models import Article
from oilpainting.serializers import ArticleSerializer, ArticleListSerializer, ArticleCreateSerializer
from django.db.models import Q


# Create your views here.

# 게시글의 전체 리스트(GET) + 게시글 작성하기(POST)
class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all( )

        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class LikeView(APIView):
    # 좋아요 한적 없으면 post 가능하게 / 있으면 아무기능 없게
    def post(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user in article.likes.all():
            article.likes.remove(request.user)
            return Response("unlike", status=status.HTTP_200_OK)
        else:
            article.likes.add(request.user)
            return Response("like", status=status.HTTP_200_OK)
