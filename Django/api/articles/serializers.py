from rest_framework import serializers
from .models import Article, Comment

# 아하 modelserializer에서 fields의 역할은
# 1 필드에 있는 항목만 검증/저장 
# 2 필드에 있는 항목만 JSON 생성

# 근데 이제 read_only_fields에 추가해두면 2만 해준다!
# 오 1만 하고 싶다면 write_only_fields


class ArticleSerializer(serializers.ModelSerializer):

    class CommentListSerializer(serializers.ModelSerializer):

        class Meta:
            model = Comment
            fields = ("id", "content")

    # custom fields
    title = serializers.CharField(min_length=2, max_length=100)
    content = serializers.CharField(min_length=2)
    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        # fields에 쓸 수 있는 것들: article.[???]에 올 수 있는 말 + custom fields
        fields = ("id", "title", "content", "comments", "created_at", "updated_at", )
        read_only_fields = ("comments", )


class ArticleListSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(source="comments.count", read_only=True)
    
    class Meta:
        model = Article
        fields = ("id", "title", "comment_count", )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("id", "article", "content", )
        read_only_fields = ("article", )