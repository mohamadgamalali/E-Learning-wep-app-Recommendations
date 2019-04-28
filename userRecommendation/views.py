from django.shortcuts import render
from django.http import Http404
from .models import Users
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import UsersSerializer
from rest_framework import status

def index(request):
    all_users = Users.objects.all()
    return render(request, 'userRecommendation/index.html', {'all_users':all_users})


def detail(request, user_Id):
    try:
        users = Users.objects.get(pk=user_Id)
    except Users.DoesNotExist:
        raise Http404("user does not exist")
    return render(request, 'userRecommendation/detail.html', {'users':users})


class UserList(APIView):

    def get(self, request):
        companies1 = Users.objects.all()
        serializer = UsersSerializer(companies1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)