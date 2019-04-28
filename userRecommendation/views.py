from django.shortcuts import render
from django.http import Http404
from .models import Users

def index(request):
    all_users = Users.objects.all()
    return render(request, 'userRecommendation/index.html', {'all_users':all_users})

def detail(request, user_Id):
    try:
        users = Users.objects.get(pk=user_Id)
    except Users.DoesNotExist:
        raise Http404("user does not exist")
    return render(request, 'userRecommendation/detail.html', {'users':users})
