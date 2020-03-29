from .models import University, Professor, ProfessorRating
from .serializers import ProfessorSerializer, UserSerializer, UniversityFullSerializer, \
    ProfessorCreateSerializer, ProfessorRatingSerializer
from rest_framework import mixins, viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics
from django.http import JsonResponse


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = University.objects.all()
    serializer_class = UniversityFullSerializer


class ProfessorViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        professor = serializer.complete()
        return Response(ProfessorSerializer(professor).data)

    def get_serializer_class(self):
        if self.action == 'create':
            return ProfessorCreateSerializer
        return ProfessorSerializer


class ProfessorRatingViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ProfessorRating.objects.all()
    serializer_class = ProfessorRatingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.complete()
        return Response(data)


def count_metrics(request):
    professors = Professor.objects.count()
    universities = University.objects.count()
    reviews = ProfessorRating.objects.count()

    return JsonResponse({
        'professors': professors,
        'universities': universities,
        'reviews': reviews
    })
