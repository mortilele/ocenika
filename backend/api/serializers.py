from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import University, Professor, ProfessorRating
from utils import constants
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class ProfessorRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorRating
        exclude = ['updated_at',]
        extra_kwargs = {
            'email': {'write_only': True},
            'professor': {'write_only': True}
        }

    def complete(self):
        email = self.validated_data['email']
        professor = self.validated_data['professor']
        if ProfessorRating.objects.last_review_in_week(email, professor):
            return constants.REVIEW_ALREADY_SUBMITTED
        ProfessorRating.objects.create(**self.validated_data)
        return status.HTTP_201_CREATED


class ProfessorSerializer(serializers.ModelSerializer):
    ratings = ProfessorRatingSerializer(many=True, read_only=True)
    universities = UniversitySerializer(many=True)

    class Meta:
        model = Professor
        fields = ['id', 'first_name', 'last_name', 'patronymic',
                  'full_name', 'avatar', 'ratings',
                  'average_rating', 'rating_count', 'universities'
                  ]

        read_only_fields = ['full_name', 'average_rating', 'rating_count']
        extra_kwargs = {
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
            'patronymic': {'write_only': True}
        }


class ProfessorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        exclude = ('full_name', 'rating_count', 'average_rating')

    def complete(self):
        try:
            data = {
                'first_name': self.validated_data['first_name'],
                'last_name': self.validated_data['last_name'],
                'patronymic': self.validated_data['patronymic'],
            }
            professor = Professor(**data)
            professor.save()
            if self.validated_data.get('avatar'):
                professor.avatar = self.validated_data['avatar']
            for university in self.validated_data['universities']:
                professor.universities.add(university)
            professor.save()
        except Exception as e:
            logger.error(str(e))
            return status.HTTP_400_BAD_REQUEST


class ProfessorShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['full_name', 'avatar']


class UniversityFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

    professor_set = ProfessorShortSerializer(many=True, read_only=True)


