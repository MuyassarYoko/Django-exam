from rest_framework import serializers

from users.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'date_of_birth', 'email', 'bio', 'role', 'password', 'avatar']


class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'avatar', 'date_of_birth', 'password', 'email']

    def create(self, validated_data):
        avatar = validated_data.get('avatar',
                                    'default_images/user_icon.png')
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            avatar=avatar,
            date_of_birth=validated_data.get('date_of_birth')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'avatar', 'email']
        extra_kwargs = {
            'avatar': {
                'required': False,
            }
        }

    def update(self, instance: User, validated_data):
        first_name = validated_data.pop('first_name', instance.first_name).capitalize()
        last_name = validated_data.pop('last_name', instance.last_name).capitalize()

        instance.first_name = first_name
        instance.last_name = last_name

        return super().update(instance, validated_data)
