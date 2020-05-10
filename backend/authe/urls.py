from django.conf.urls import url
from rest_framework import routers
from authe import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^login/', views.obtain_auth_token),
]

urlpatterns += router.urls
