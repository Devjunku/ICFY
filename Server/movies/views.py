
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.contrib.auth import get_user_model
from django.shortcuts import  get_object_or_404, get_list_or_404
from .models import Movie, Review, Comment
from .serializers import MovieListSerializer, ReviewListSerializer, CommentSerializer

# 머신러닝을 위한 module
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Create your views here.
@api_view(['GET', 'POST'])
def movie_index(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MovieListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# 로그인한 사용자만 볼 수 있도록
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community(request, movie_id):
    # GET 방식이면 리뷰를 보는 행위
    if request.method == 'GET':
        movie = get_object_or_404(Movie, id=movie_id)
        reviews = movie.review_set.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializers = ReviewListSerializer(data=request.data)
    if serializers.is_valid(raise_exception = True):
        serializers.save(movie=movie, user=request.user)
        return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST','DELETE', 'PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    # GET 방식이면, detail 페이지 데이터 전송
    if request.method == 'GET':
        serializer = ReviewListSerializer(review)
        return Response(serializer.data)

    elif request.method == 'POST':
        review = get_object_or_404(Review, id=review_pk)
        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid(raise_exception = True):
            serializers.save(review=review, user=request.user)
            return Response(serializers.data, status=status.HTTP_201_CREATED)

    # DELETE 방식이면 리뷰를 작성 데이터를 DB에 삭제 후 전송
    elif request.method == 'DELETE':
        review.delete()
        return Response({'movie_id': review.movie_id})

    # PUT 방식이면 리뷰를 작성 데이터를 DB에 수정 후 전송
    elif request.method == 'PUT':
        serializer = ReviewListSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['DELETE', 'PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def change_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'DELETE':
        comment.delete()
        return Response({'comment_id': comment.id})

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile_info(request, user_id):
    
    # 작성한 리뷰가 없으면 404 에러가 난다.
    # reviews = get_list_or_404(Review, user_id=user_id)
    # comments = get_list_or_404(Comment, user_id=user_id)

    # 그래서 이렇게 쓰겠다.
    reviews = Review.objects.filter(user_id=user_id)
    comments = Comment.objects.filter(user_id=user_id)

    if request.method == 'GET':
        review_serializer = ReviewListSerializer(reviews,  many=True)
        comment_serializer = CommentSerializer(comments, many=True)
        # [{}, {}] 이런 형태로 들어오는데 이렇게 해줘야 구분할 수 있다.
        return Response({'review': review_serializer.data, 'comment': comment_serializer.data})


def get_recommend_movie_list(movie, movies, similar, top=30):
    search_movie_idx = movie.index.values
    print(search_movie_idx)
    similar_idx = similar[search_movie_idx, :top].reshape(-1)
    print(similar_idx)
    similar_idx = similar_idx[similar_idx != search_movie_idx] # 제목이 movie_title 인 영화 제외
    result = movies.iloc[similar_idx].sort_values('popularity', ascending=False)[:10]
    return result


@api_view(['GET'])
# 아직은 프로토 타입
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def recommend(request, movie_id):
    if Movie.objects.get(id=movie_id):
        
        movies = pd.DataFrame(list(Movie.objects.all().values()))
        movie = movies[movies['id'] == movie_id]
        
        transformer = CountVectorizer()
        genres_vector = transformer.fit_transform(movies['genre_ids'])
        similar = cosine_similarity(genres_vector, genres_vector)
        similar = similar.argsort()
        similar = similar[:, ::-1]
        res = get_recommend_movie_list(movie, movies, similar)

        # 아직은 프로토 타입
        return Response(res)