import json

from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from rest_framework import mixins
from rest_framework.decorators import action

from .models import User
from rest_framework.response import Response

from authe.serializers import UserSerializer

from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.views import APIView
from .serializers import AuthTokenSerializer


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(user=user)
        return Response({'token': token.key})


obtain_auth_token = ObtainAuthToken.as_view()


class UserViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action in ['create', 'confirm']:
            self.permission_classes = [permissions.AllowAny, ]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super(UserViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def confirm(self, request, *args, **kwargs):
        token = self.request.query_params.get('token', None)
        if token:
            user = self.get_object()
            if token == Token.objects.get(user_id=user.id).key:
                user.is_confirmed = True
                user.save()
        return redirect('https://ocenika.com')

    def retrieve(self, request, *args, **kwargs):
        return Response()