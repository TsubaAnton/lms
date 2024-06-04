from rest_framework import serializers
from .models import User, Payment, Subscription


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ['id', 'user', 'course', 'lesson', 'amount_payment', 'payment_method', 'payment_date']
        read_only_fields = ['id', 'user', 'payment_date']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

        def create(self, validated_data):
            user = User(
                email=validated_data['email'],
                phone=validated_data.get('phone'),
                city=validated_data.get('city'),
                avatar=validated_data.get('avatar')
            )
            user.set_password(validated_data['password'])
            user.save()
            return user


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
