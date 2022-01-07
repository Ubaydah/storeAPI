from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class Login(APIView):
    permission_classes = ()

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user:
            return Response({"token": user.auth_token.key, "email": email})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class Register(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        user = CustomUser.objects.get(id=pk)
        serializer = ChangePasswordSerializer(user, data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": "Your password has been successfully changed"})


class ForgotPassword(APIView):
    pass

class UpdateUser(APIView):

    #permission_classes = [IsAuthenticated]
    #authentication_classes = ()
    def put(self, request, pk):

        user = CustomUser.objects.get(id=pk)
        serializer = UserUpdateSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data) 

  
class CreateStore(APIView):

    def post(self, request):

        serializer = StoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class UpdateStore(APIView):
    
    def put(self, request, pk):

        store = Store.objects.get(id=pk)
        serializer = StoreSerializer(store, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)



class GetStores(APIView):
    pass

class GetProducts(APIView):
    pass

class CreateProduct(APIView):

    pass

class FetchProduct(APIView):

    pass

class UpdateProduct(APIView):

    pass

class DeleteProduct(APIView):

    pass
        
class Deposit(APIView):

    pass

class Withdraw(APIView):

    pass

class Transfer(APIView):

    pass