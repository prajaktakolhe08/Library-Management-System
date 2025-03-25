from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import Book

AdminUser = get_user_model() # since we are using custom user model we need this to rfer it dynamically.

# Admin signup serializer 
class AdminSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type':'password'}, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = AdminUser
        fields = ('id','email','username','password','password2')
        
    def validate(self, data):
        # check if password match
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': "Passwords did not match."})
        return data
    
    def create(self, validated_data):
        # Remove password2 from validated data because it isn't a field in our AdminUser model
        validated_data.pop("password2")
        #create the admin user with hashed password
        user = AdminUser.objects.create_user(**validated_data)
        return user
    
class AdminLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # Include all fields from Book Model

    
