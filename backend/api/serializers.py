from rest_framework import serializers
from api.models import University, Professor, ProfessorReview, Subject
from utils import constants
from rest_framework import status


class SubjectShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'abbreviation']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class ProfessorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorReview
        exclude = ('updated_at',)
        extra_kwargs = {
            'email': {'write_only': True},
            'professor': {'write_only': True}
        }

    def to_representation(self, instance):
        output = super().to_representation(instance)
        output['created_at'] = instance.created_at.strftime("%Y-%m-%d")
        return output

    def complete(self):
        email = self.validated_data['email']
        professor = self.validated_data['professor']
        if ProfessorReview.objects.last_review_in_week(email, professor):
            return constants.REVIEW_ALREADY_SUBMITTED, status.HTTP_400_BAD_REQUEST
        rating = ProfessorReview.objects.create(**self.validated_data)
        serializer = ProfessorReviewSerializer(instance=rating)
        return serializer.data, status.HTTP_201_CREATED


class ProfessorSerializer(serializers.ModelSerializer):
    universities = UniversitySerializer(many=True)
    subjects = SubjectShortSerializer(many=True, read_only=True)
    ratings = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Professor
        fields = ['id', 'first_name', 'last_name', 'patronymic',
                  'full_name', 'avatar', 'ratings', 'subjects',
                  'average_rating', 'rating_count', 'universities'
                  ]

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['ratings'] = result['ratings'][:3]
        return result

    def get_ratings(self, obj):
        return ProfessorReviewSerializer(obj.ratings.filter(status=constants.ACTIVE), many=True).data


class ProfessorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        exclude = ('full_name', 'rating_count', 'average_rating')


class ProfessorShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['full_name', 'avatar']


class UniversityFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'abbreviation', 'description', 'logo', 'professor_set', 'subjects']

    professor_set = ProfessorShortSerializer(many=True, read_only=True)
    subjects = SubjectShortSerializer(many=True, read_only=True)

