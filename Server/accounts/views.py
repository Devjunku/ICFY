from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserProfileSerializer, UserCheckSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Create your views here.
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    serializer = UserProfileSerializer(person)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def check(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    serializer = UserCheckSerializer(person)
    return Response(serializer.data, status=status.HTTP_200_OK)
    