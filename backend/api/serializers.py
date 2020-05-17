from rest_framework import serializers
from api.models import University, Professor, ProfessorReview, Subject, PrivacyPolicy
from authe.models import User
from utils import constants, string_utils, exceptions
from rest_framework import status


class SubjectShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'abbreviation']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


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
        return ProfessorReviewListSerializer(obj.ratings.filter(status=constants.ACCEPTED), many=True).data


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
        fields = ['id',
                  'name',
                  'abbreviation',
                  'description',
                  'logo',
                  'professor_set',
                  'subjects',
                  'rating']

    professor_set = ProfessorShortSerializer(many=True, read_only=True)
    subjects = SubjectShortSerializer(many=True, read_only=True)


class ProfessorReviewCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True, default=None)

    class Meta:
        model = ProfessorReview
        exclude = ('updated_at', 'user')
        # extra_kwargs = {
        #     'professor': {'write_only': True}
        # }

    def to_representation(self, instance):
        output = super().to_representation(instance)
        output['created_at'] = instance.created_at.strftime("%Y-%m-%d")
        return output

    def complete(self):
        user = self.context['request'].user
        email = self.validated_data.pop('email', None)
        if user and user.is_authenticated:
            if not user.is_confirmed:
                message = constants.CONFIRM_USER
            elif not user.transcript:
                message = constants.ASSIGN_TRANSCRIPT
            else:
                message = constants.REVIEW_ON_MODERATION
        else:
            if email:
                try:
                    user = User.objects.get(email=email)
                    if not user.is_confirmed:
                        message = constants.CONFIRM_USER
                    elif not user.transcript:
                        message = constants.ASSIGN_TRANSCRIPT
                    else:
                        message = constants.REVIEW_ON_MODERATION
                except Exception as e:
                    user = User.objects.create_user(email=email,
                                                    password=string_utils.generate_password())
                    message = constants.CONFIRMATION_SEND
            else:
                raise User.DoesNotExist

        professor = self.validated_data['professor']
        self.validated_data['user'] = user
        self.validated_data['moderator_message'] = message
        # if ProfessorReview.objects.last_review_in_week(user, professor):
        #     raise exceptions.CommonException(detail=constants.REVIEW_ALREADY_SUBMITTED)

        rating = ProfessorReview.objects.create(**self.validated_data)
        serializer = ProfessorReviewListSerializer(instance=rating)
        print(serializer.data)
        return serializer.data, status.HTTP_201_CREATED


class ProfessorReviewListSerializer(serializers.ModelSerializer):
    professor = ProfessorShortSerializer(read_only=True)
    subject = SubjectShortSerializer(read_only=True)

    class Meta:
        model = ProfessorReview
        exclude = ('updated_at', 'user')

    def to_representation(self, instance):
        output = super().to_representation(instance)
        output['created_at'] = instance.created_at.strftime("%Y-%m-%d")
        return output


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ('file', )
