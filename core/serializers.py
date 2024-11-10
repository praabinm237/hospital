from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model
from random import randint
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password

User = get_user_model()

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)
    
class LogoutSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    
    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is not associated with any account.")
        return value
    
class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise ValidationError({
                'confirm_password': 'Passwords do not match',
            })
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        otp = randint(0000,9999)
        user.otp = otp
        user.save()
        subject = 'Registration successful'
        request = self.context['request']
        activation_link =  f'{request.get_host()}?otp={otp}'
        message = f'''Hi {user.username}, Your otp for activating your account is {otp} for {user.email}
                    and activation link : {activation_link}'''
        email_from = 'hello@new-hospital.com'
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )
        return user
    
class OTPVerificationSerializer(serializers.Serializer):
    otp = serializers.IntegerField()
    email = serializers.EmailField()
    
    def validate(self, attrs):
        user = User.objects.filter(
            email=attrs['email'],
            otp=attrs['otp'],
        ).exists()
        if not user:
            raise ValidationError(
                {'otp': 'Invalid OTP'},
            )
        return attrs
    
    def update(self, instance, validated_data): 
        instance.is_active = True
        instance.save()
        return instance
    
class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    def validate_email(self, value):
        user = User.objects.filter(email=value).exists()
        if not user:
            raise ValidationError({'details': 'User with this email does not exist.'})
        return value

class PasswordUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.IntegerField()
    password = serializers.CharField(max_length=255)
       
    def validate_email(self, attrs):
        user = User.objects.filter(email=attrs.get('email'),otp=attrs.get('otp')).exists()
        if not user:
            raise ValidationError({'details': 'Email or otp is stale'})
        return attrs   
    
    def update(self, instance, validated_data):
        instance.password = make_password(validated_data.get('password'))
        instance.save()
        return instance

class UserGroupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    groups = serializers.CharField(max_length=50)  

       
class GroupSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

