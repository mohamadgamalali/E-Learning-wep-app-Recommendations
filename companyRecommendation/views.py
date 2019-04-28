from django.shortcuts import render
from django.http import Http404
from .models import Company
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import CompaniesSerializer
from rest_framework import status


def index(request):
    all_company = Company.objects.all()
    return render(request, 'companyRecommendation/index.html', {'all_company': all_company})


def detail(request, companyId):
    try:
        company = Company.objects.get(pk=companyId)
    except Company.DoesNotExist:
        raise Http404("company does not exist")
    return render(request, 'companyRecommendation/detail.html', {'company': company})

class CompanyList(APIView):
      def get(self, request):
            companies1 = Company.objects.all()
            serializer = CompaniesSerializer(companies1, many=True)
            return Response(serializer.data)

      def post(self, request):
            serializer = CompaniesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      def delete(self, request, pk, format=None):
          snippet = self.get_object(pk)
          snippet.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
class main():
    def recommend(self):
        self = CompanyList.get()