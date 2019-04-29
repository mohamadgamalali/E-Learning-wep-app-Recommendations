from django.shortcuts import render
from django.http import Http404
from .models import Quizzes
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import QuizzesSerializer
from rest_framework import status
from userRecommendation.models import Users

def index(request):
    all_quizzes = Quizzes.objects.all()
    return render(request, 'quizRecommendation/index.html', {'all_quizzes': all_quizzes})


def detail(request, quizId):
    try:
        quiz = Quizzes.objects.get(pk=quizId)
    except Quizzes.DoesNotExist:
        raise Http404("quiz does not exist")
    return render(request, 'quizRecommendation/detail.html', {'quiz': quiz})


class QuizList(APIView):

    def get(self, request):
        companies1 = Quizzes.objects.all()
        serializer = QuizzesSerializer(companies1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuizzesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
