from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from rest_framework.authtoken.models import Token

from utils import constants
from utils.permissions import IsAuthenticatedAndActive
from .models import University, Professor, ProfessorReview, PrivacyPolicy
from api import serializers
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from authe.models import User

from django.http import JsonResponse


class UniversityViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = University.objects.all()
    serializer_class = serializers.UniversityFullSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name']
    ordering = ['-rating']


class ProfessorViewSet(mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = Professor.objects.all()
    serializer_class = serializers.ProfessorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['full_name', 'subjects__name', 'subjects__abbreviation', 'universities__name',
                     'universities__abbreviation']
    filterset_fields = ['universities', ]
    ordering_fields = ['last_name', 'full_name']
    ordering = ['last_name']


class ProfessorReviewViewSet(mixins.CreateModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    queryset = ProfessorReview.objects.filter(status=constants.ACCEPTED,
                                              created_at__gte=timezone.now() - relativedelta(months=6))
    serializer_class = serializers.ProfessorReviewListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['professor', ]
    permission_classes = [IsAuthenticatedAndActive]

    def get_permissions(self):
        if self.action in ['total_ratings', 'last_ratings', 'create']:
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticatedAndActive, ]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.ProfessorReviewCreateSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data, status = serializer.complete()
        return Response(data, status)

    @action(detail=False, methods=['get'])
    def total_ratings(self, request):
        professor_id = self.request.query_params['professor_id']
        professor_ratings = ProfessorReview.objects.filter(professor_id=professor_id)
        ones = professor_ratings.filter(value=1,
                                        status=constants.ACCEPTED,
                                        created_at__gte=timezone.now() - relativedelta(months=6)).count()
        twos = professor_ratings.filter(value=2, status=constants.ACCEPTED,
                                        created_at__gte=timezone.now() - relativedelta(months=6)).count()
        threes = professor_ratings.filter(value=3, status=constants.ACCEPTED,
                                          created_at__gte=timezone.now() - relativedelta(months=6)).count()
        fours = professor_ratings.filter(value=4, status=constants.ACCEPTED,
                                         created_at__gte=timezone.now() - relativedelta(months=6)).count()
        fives = professor_ratings.filter(value=5, status=constants.ACCEPTED,
                                         created_at__gte=timezone.now() - relativedelta(months=6)).count()
        total = professor_ratings.filter(status=constants.ACCEPTED,
                                         value__gt=0,
                                         value__lte=5,
                                         created_at__gte=timezone.now() - relativedelta(months=6)).count()
        average = round((ones * 1 + twos * 2 + threes * 3 + fours * 4 + fives * 5) / total) if total else 0
        return JsonResponse({
            'ones': ones,
            'twos': twos,
            'threes': threes,
            "fours": fours,
            'fives': fives,
            'total': total,
            'average': average
        })

    @action(detail=False, methods=['get'])
    def last_ratings(self, request):
        last_ratings = ProfessorReview.objects.filter(status=constants.ACCEPTED,
                                                      created_at__gte=timezone.now() - relativedelta(months=6)
                                                      ).order_by('-created_at')[:10]
        return Response(serializers.ProfessorReviewListSerializer(last_ratings, many=True).data)


def count_metrics(request):
    professors = Professor.objects.count()
    universities = University.objects.count()
    reviews = ProfessorReview.objects.count()
    users = User.objects.filter(is_active=True).count()

    return JsonResponse({
        'professors': professors,
        'universities': universities,
        'reviews': reviews,
        'users': users
    })


def test(request):
    user_id = request.GET.get('user_id', 2)
    user = User.objects.get(id=user_id)
    token = Token.objects.get(user_id=user_id)
    return render(request, 'emails/send_confirmation_email.html',
                  {'base_url': settings.BACKEND_URL,
                   'email': user.email,
                   'password': user.raw_password,
                   'user_id': user.id,
                   'token': token})


def policy(request):
    serializer = serializers.PrivacyPolicySerializer(instance=PrivacyPolicy.objects.first())
    policy_url = settings.BACKEND_URL + serializer.data['file']
    return JsonResponse({'file': policy_url})
