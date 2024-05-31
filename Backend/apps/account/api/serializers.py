from rest_framework import serializers 
from ..models import UserData


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ['id', 'name', 'email', 'password']


    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'], name=validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()



