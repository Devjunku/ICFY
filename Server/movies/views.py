from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse, HttpResponse
from .models import Movie, Review
from .serializers import MovieListSerializer, ReviewListSerializer
from Server.movies import serializers

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
        
@api_view(['GET', 'POST'])
def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def community(request, movie_id):
    # GET 방식이면 리뷰를 보는 행위
    if request.method == 'GET':
        movie = get_object_or_404(Movie, id=movie_id)
        reviews = movie.review_set.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, id=movie_pk)
    serializers = ReviewListSerializer(data=request.data)
    if serializers.is_valie(raise_exception = True):
        serializers.save(movie=movie)
        return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):

    # GET 방식이면, detail 페이지 데이터 전송
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewListSerializer(review)
        return Response(serializer.data)

    # DELETE 방식이면 리뷰를 작성 데이터를 DB에 삭제 후 전송
    elif request.method == 'DELETE':
        data = {
            'Delete': f'{request.user}님이 작성하신 영화 리뷰 {review.title}이 삭제되었습니다.'
        }
        review.delete()
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    # DELETE 방식이면 리뷰를 작성 데이터를 DB에 수정 후 전송
    elif request.method == 'PUT':
        serializer = ReviewListSerializer(Review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)