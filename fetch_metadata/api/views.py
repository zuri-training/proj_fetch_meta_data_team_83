from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from .permissions import IsCreatorOrAdminReadOnly
from . import serializers



# Create your views here.

UserModel = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    default_serializer_class = serializers.UserOutputSerializer
    renderer_classes = [TemplateHTMLRenderer]


    serializers_classes = {
        "create":serializers.UserInputSerializer
    }

    def create(self, request, *args, **kwargs):
        """
        User SignUp
            - Allow anyone to signup (without authentication)
        """
        self.check_permissions(request)
        serializer = serializers.UserInputSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)

        user = UserModel.objects.create_user(
            email = serializer.validated_data["email"],
            username = serializer.validated_data["username"],
            password = serializer.validated_data["password"]
        )
        response = serializers.UserOutputSerializer(user).data
        return Response(response, status=status.HTTP_201_CREATED, template_name='api/signup.html')

    def retrieve(self, request, pk=None):
        # Check if pk is a valid slug
        user = UserModel.objects.filter(slug=pk).first()

        if not user and pk.isdigit():
            # Find user by primary key/ID
            user = UserModel.objects.filter(pk=pk).first()

        self.check_object_permissions(request, user)
        response = serializers.UserOutputSerializer(user).data
        response = {'response':response}
        return Response(response, status=status.HTTP_200_OK, template_name='user_list.html')

    def get_permissions(self):
        if self.action == 'create': # Create, List, Retrieve, Update, or Destroy
            permission_classes = [permissions.AllowAny]
       #  elif self.action == 'retrieve':
            # permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsCreatorOrAdminReadOnly,permissions.IsAuthenticated]
        elif self.action == 'list':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        return self.serializers_classes.get(self.action, self.default_serializer_class)

    # @action(detail=True, methods=['post'])
    # def change_password(self, request, pk=None):
    #     """
    #     Allow an authenticated user to change password
    #     """
    #     user = self.get_object()
    #     serializer = serializers.PasswordChangeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user.change_password(serializer.validated_data['password'])
    #         user.save()
    #         return Response({'status': 'password changed'})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api/signup.html'

    def get(self, request, pk=None):
        signup = get_object_or_404(UserModel)
        serializer = serializers.UserInputSerializer(signup)
        return Response({'serializer': serializer, 'signup': signup})

    def post(self, request):
        self.check_permissions(request)
        serializer = serializers.UserInputSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)

        user = UserModel.objects.create_user(
            email = serializer.validated_data["email"],
            username = serializer.validated_data["username"],
            password = serializer.validated_data["password"]
        )
        response = serializers.UserOutputSerializer(user).data
        return Response(response, status=status.HTTP_201_CREATED)
