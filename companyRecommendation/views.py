from django.shortcuts import render
from django.http import Http404
from .models import Company

def index(request):
    all_company = Company.objects.all()
    return render(request, 'companyRecommendation/index.html', {'all_company':all_company})

def detail(request, companyId):
    try:
        company = Company.objects.get(pk=companyId)
    except Company.DoesNotExist:
        raise Http404("company does not exist")
    return render(request, 'companyRecommendation/detail.html', {'company':company})
