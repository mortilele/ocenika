from django.conf.urls import url
from django.urls import path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'universities', views.UniversityViewSet, basename='university')
router.register(r'professors', views.ProfessorViewSet)
router.register(r'ratings', views.ProfessorRatingViewSet)

urlpatterns = [
    url(r'metrics', views.count_metrics),
]

urlpatterns += router.urls

