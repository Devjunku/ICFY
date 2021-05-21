from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # 메인 페이지 (여러 가지 추천 영화가 나온다.)
    path('', views.movie_index, name='movie_index'),
    # 단일 영화 페이지
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    # GET : 특정 영화에 대한 커뮤니티
    # POST: 특정 영화에 대한 리뷰 생성
    path('<int:movie_id>/community', views.community, name='community'),
    # GET : 특정 리뷰 보기
    # PUT : 특정 리뷰 수정
    # DELETE : 특정 리뷰 삭제 
    # path('community/<int:review_pk>', views.review, name='review'),
]