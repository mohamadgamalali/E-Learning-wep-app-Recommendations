from django.shortcuts import render
from django.http import Http404
from .models import Quizzes

def index(request):
    all_quizzes = Quizzes.objects.all()
    return render(request, 'quizRecommendation/index.html', {'all_quizzes':all_quizzes})

def detail(request, quizId):
    try:
        quiz = Quizzes.objects.get(pk=quizId)
    except Quizzes.DoesNotExist:
        raise Http404("quiz does not exist")
    return render(request, 'quizRecommendation/detail.html', {'quiz':quiz})
