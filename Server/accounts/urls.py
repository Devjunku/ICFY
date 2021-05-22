from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('api-token-auth/',  obtain_jwt_token),
    path('<username>/', views.profile, name='profile'),
    # path('delete/', views.delete, name='delete'),
    # path('update/', views.update, name='update'),
    # path('password/', views.change_password, name='change_password'),
    # path('<int:user_pk>/follow/', views.follow, name='follow'),
]