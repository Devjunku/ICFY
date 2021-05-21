from rest_framework import serializers
from .models import Movie, Review, Comment


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'poster_path', 'vote_average', 'adult', )


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user',)


# class ArticleSerializer(serializers.ModelSerializer):
#     # 기존 필드 override
#     # 첫번째 방법
#     # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     # 두번째 방법
#     comment_set = CommentListSerializer(many=True, read_only=True)
#     comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

#     class Meta:
#         model = Article
#         fields = '__all__'
