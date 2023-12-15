from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "username", "email", "password", "is_superuser"]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"default": False},
            "email": {
                "validators": [
                    UniqueValidator(Account.objects.all(), "user with this email already exists.")
                ]
            },
            "username": {
                "validators": [
                    UniqueValidator(Account.objects.all(), "A user with that username already exists.")
                ]
            }
        }

    def create(self, validated_data):
        if validated_data["is_superuser"]:
            user = Account.objects.create_superuser(
                **validated_data
            )
        else:
            user = Account.objects.create_user(
                **validated_data
            )
        return user

    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance
