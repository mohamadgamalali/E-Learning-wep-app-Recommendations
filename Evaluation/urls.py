from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from quizRecommendation import views as quiz_view
from userRecommendation import views as user_view
from companyRecommendation import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quizRecommendation', include('quizRecommendation.urls')),
    url(r'^userRecommendation', include('userRecommendation.urls')),
    url(r'^companyRecommendation', include('companyRecommendation.urls')),
    url(r'^Company/', views.CompanyList.as_view()),
    url(r'^Quizzes/', quiz_view.QuizList.as_view()),
    url(r'^Users/', user_view.UserList.as_view()),
]
