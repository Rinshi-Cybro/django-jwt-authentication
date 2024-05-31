from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from ..models import UserData
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegisterSerializer, LoginSerializer


# Create your views here.

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Successfully Registred'})
        return Response(serializer.errors)
    


class UserLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
            if user is None:
                return Response({'status': 400, 'message': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
            
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        return Response({'status': 400, 'message': 'Something went wrong!!', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class UserLogoutView(APIView):

    # permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
























    
    
# class UserLoginView(APIView):
#     def post(self, request):
#         data = request.data
#         serializer = LoginSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             email = serializer.data['email']
#             password = serializer.data['password']
#             user = authenticate(email = email, password = password)
#             if user is None:
#                 return Response({'status':400, 'message': 'Invalid email or password'})
            
#             refresh = RefreshToken.for_user(user)
#             return{
#                 'refresh':str(refresh),
#                 'access': str(refresh.access_token)
#             }
#         return Response({'status':400, 'message': 'Something went worng!!', 'data': serializer.errors})
    

            




