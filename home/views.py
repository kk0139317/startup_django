from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactMessage, Profile
from .serializers import ContactMessageSerializer, ProfileSerializer, UserLoginSerializer
from .serializers import UserSerializer 
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
import json
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.permissions import AllowAny



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_profile(request):
    try:
        profile = Profile.objects.get(username=request.user)
        print(request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
@csrf_exempt
def submit_contact_form(request):
    if request.method == 'POST':
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# class UserLogin(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
#             if user is not None:
#                 login(request, user)
#                 return Response({'token': 'your_token_here'}, status=status.HTTP_200_OK)  # Replace with actual token generation
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserLogin(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.create(serializer.validated_data))
#         return Response(serializer.errors, status=400)



from rest_framework_simplejwt.tokens import RefreshToken

class UserLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileCreateView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserListView(APIView):
    def get(self, request):
        users = Profile.objects.all()
        serializer = ProfileSerializer(users, many=True)
        return Response(serializer.data)
    
# class ProfileDetailView(APIView):
#     def get(self, request):
#         users = Profile.objects.filter(id=1).values()
#         serializer = ProfileSerializer(users, many=True)
#         print(serializer.data)
#         return Response(serializer.data)
    
# class ProfileDetailView(generics.RetrieveAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     lookup_field = 'id'

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ProfileDetailView(request, id):
    try:
        profile = Profile.objects.get(id = id)
        # print(request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
    

def testing(request, id):
    id = id
    print(id)
    return HttpResponse("This is ", id)