from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Comment
from .serializers import (
    ArticleSerializer, 
    ArticleListSerializer, 
    CommentSerializer
)
from articles import serializers


@api_view(["GET", "POST"])
def article_index_create(request):

    def article_index():
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    def article_create():
        serializer = ArticleSerializer(data=request.data)
        # raise_exception: is_valid하지 않을 때를 자동으로 처리
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # POST, create
    if request.method == "POST":
        return article_create()
    # GET, index
    else:
        return article_index()
    


@api_view(["GET", "PUT", "DELETE"])
def article_detail_update_delete(request, article_pk):
    
    article = get_object_or_404(Article, pk=article_pk)

    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def article_update():
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def article_delete():
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    if request.method == "GET":
        return article_detail()

    elif request.method == "PUT":
        return article_update()

    elif request.method == "DELETE":
        return article_delete()


@api_view(["POST"])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        # serializer의 save에는 commit=False가 없다
        # 걍 이 아티클이 내 아티클이다 라고 말하면 됨
        serializer.save(article=article)
        return Response(serializer.data)


@api_view(["PUT", "DELETE"])
def comment_update_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def comment_update():
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 댓글의 원글을 수정하진 않으므로 따로 article=을 지정해주지 않음
            serializer.save()
            return Response(serializer.data)

    def comment_delete():
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == "PUT":
        return comment_update()

    elif request.method == "DELETE":
        return comment_delete()