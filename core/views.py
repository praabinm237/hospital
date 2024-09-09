from random import randint
from .serializers import (
    GroupSerializer,
    OTPVerificationSerializer,
    PasswordResetSerializer,
    PasswordUpdateSerializer, 
    UserCreateSerializer, 
    UserGroupSerializer, 
    UserSerializer, 
    LogoutSerializer
)
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.models import Group
from django.shortcuts import HttpResponse, get_object_or_404
from django.core.mail import send_mail

User = get_user_model()

class UserViewSet(ViewSet):
    queryset = User.objects.all()

    @swagger_auto_schema(
        request_body=UserSerializer,
        method='POST',
    )
    @action(detail=False, methods= ['POST'])
    def login(self, request):
        if request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user=authenticate(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
            )
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response(
                    {
                        'token': token.key,
                        'user' : user.username,
                    }
                )
            return Response(
                {
                    'error': 'Invalid credentials',
                },
                status = status.HTTP_401_UNAUTHORIZED,
            )

    @swagger_auto_schema(
        request_body=LogoutSerializer,
        method='POST',
    )
    @action(detail=False, methods= ['POST'])
    def log_out(self, request):
        serializer = LogoutSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            user = request.user
            if user.email == email:
                Token.objects.filter(user=user).delete() 
                return Response({"message": "User logged out successfully."}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {
                        "error": "Email does not match the logged-in user."
                    }, status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        request_body=UserCreateSerializer,
        method='POST',
    )
    @action(detail=False, methods= ['POST'])
    def register(self, request):
        context = {
            'request': request
        }
        serializer = UserCreateSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'details': 'User created successfully',
            }
        )
        
    @swagger_auto_schema(
        request_body=OTPVerificationSerializer,
        method='PUT',
    )
    @action(detail=False, methods= ['PUT'])
    def verify_otp(self,request):
        user = User.objects.get(
            email=request.data['email'],
        )
        serializer = OTPVerificationSerializer(instance = user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'details': 'OTP verified successfully',
            }, 
            status = status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        request_body=PasswordResetSerializer,
        method='POST',
    )
    @action(detail=False, methods= ['POST'])
    def password_reset(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = User.objects.get(email=email)
        user.otp = randint(0000,9999)
        user.save()
        message = f'Hi {user.username}, Your otp for resetting your password is {user.otp} for {user.email}'
        email_from = 'hello@new-hospital.com'
        subject = 'Reset Password'
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )
        return Response(
            {
                'details': 'OTP sent successfully',
            }
        )
    
    @swagger_auto_schema(
        request_body=PasswordUpdateSerializer,
        method='PUT',
    )
    @action(detail=False, methods= ['PUT'])
    def password_update(self, request):  
        user = get_object_or_404(User, email=request.data.get('email'))
        serializer = PasswordUpdateSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'details': 'Password updated successfully',
            },
            status = status.HTTP_200_OK,
        )
        
        
    
    @swagger_auto_schema(
        request_body=UserGroupSerializer,
        method='POST',
    )
    @action(detail=False, methods= ['POST'])
    def assign_groups(self, request):
        
        if request.method == 'POST':
            serializer = UserGroupSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['email']
            group_name = serializer.validated_data['groups']
            try:
                user = User.objects.get(email=user)
            except:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            try:
                group = Group.objects.get(name=group_name)
            except:
                return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)
        
            user.groups.add(group)
            return Response(
            {
                'details': 'User added to group successfully',
            }
        )
            
    @swagger_auto_schema(
        request_body=GroupSerializer,
        method='POST',
    )
    @action(detail=False, methods= ['POST'])
    def add_groups(self, request):
        if request.method == 'POST':
            serializer = GroupSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            group_name = serializer.validated_data['name']
            Group.objects.create(name=group_name)
        return Response(
            {
                'details': 'Group created successfully',
            }
        )

def activate(request):
    otp = request.GET.get('otp')
    serializer = OTPVerificationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return HttpResponse(otp)    

            