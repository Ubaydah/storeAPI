from django.db.models import fields
from rest_framework import serializers, validators
from .models import *
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser
        fields = ['firstname', 'lastname', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}} 

        def create(self, validated_data):
            user = CustomUser(
                email= validated_data['email'],
                firstname = validated_data['firstname'],
                lastname = validated_data['lastname'],
            )
        
            user.set_password(validated_data['password'])
            user.save()
            Token.objects.create(user=user)
            return user 

class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['firstname', 'lastname']

    
    def update(self, instance, validated_data):
        
        instance.firstname = validated_data['firstname']
        instance.lastname = validated_data['lastname']
        

        instance.save()

        return instance

class ChangePasswordSerializer(serializers.ModelSerializer):

    old_password = serializers.CharField(write_only=True, required=True)
    new_password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    new_password2 = serializers.CharField(write_only=True, required=True)

    class Meta:

        model = CustomUser
        fields = ['old_password', 'new_password1', 'new_password2']

    #def validate(self, attrs):

        #if attrs['new_password1'] != attrs['new_password2']:

            #return serializers.ValidationError({"Detail":"The password field doesn't match"})

    def validate_old_password(self, value):
        user = self.context['request'].user
        if user.check_password(value) != True:

            return serializers.ValidationError({"detail": "Your old password is incorrect"})

    def update(self, instance, validated_data):

        instance.set_password(validated_data['new_password1'])

        instance.save()

        return instance

class WalletSerializer(serializers.ModelSerializer):
     
    class Meta:

        model = Wallet
        fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):

    class Meta:

        model = BankAccount
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):

    class Meta:

        model = Store
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = '__all__'

class TransactionsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Transactions
        fields = '__all__ '

