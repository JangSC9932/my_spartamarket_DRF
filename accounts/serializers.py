from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'birthday',
            'gender',
            'introduction',
            'nickname',
        ]

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            # set_password 에서 암호화 해줌
            instance.set_password(password)
        instance.save()
        return instance
