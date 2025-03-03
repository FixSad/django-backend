from rest_framework import serializers
from .models import User, Result

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'surname',
            'name',
            'patronymic',
            'date_of_birth',
            'gender',
            'email',
            'phone_number',
            'city',
            'country',
            'education_level',
            'other_education',
            'profession',
            'workplace',
            'smokes',
            'drinks_alcohol',
            'stress_level',
            'goals',
            'consent',
            'password',
            'additional_comments',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'result', 'description', 'user']