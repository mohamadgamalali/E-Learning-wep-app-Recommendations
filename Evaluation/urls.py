from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quizRecommendation', include('quizRecommendation.urls')),
    url(r'^userRecommendation', include('userRecommendation.urls')),
    url(r'^companyRecommendation', include('companyRecommendation.urls')),

]
