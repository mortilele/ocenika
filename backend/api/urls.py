from django.urls import path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'university', views.UniversityViewSet, basename='university')
router.register(r'professor', views.ProfessorViewSet)
router.register(r'rating', views.ProfessorRatingViewSet)

urlpatterns = router.urls