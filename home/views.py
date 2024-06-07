from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactMessage, Profile
from .serializers import ContactMessageSerializer, ProfileSerializer, UserLoginSerializer, SubmitFormSerializer
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
from home.models import SubmitForm
import json


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




# @api_view(['POST'])
# @csrf_exempt
# def submit_form(request):
#     if request.method == 'POST':
#         serializer = SubmitFormSerializer(data=request.data)
#         print(request.data.get('config'))
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import SubmitForm

@api_view(['POST'])
@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        config = request.data.get('config')
        accelerateLaunch = request.data.get('accelerateLaunch')
        model = request.data.get('model')
        metadata = request.data.get('metadata')
        folders = request.data.get('folders')
        datasetPreparation = request.data.get('datasetPreparation')
        presets = request.data.get('presets')
        loraType = request.data.get('loraType')
        networkWeights = request.data.get('networkWeights')
        dimFromWeight = request.data.get('dimFromWeight')
        trainBatchSize = request.data.get('trainBatchSize')
        epoch = request.data.get('epoch')
        maxTrainEpoch = request.data.get('maxTrainEpoch')
        maxTrainStep = request.data.get('maxTrainStep')
        saveEveryNEpochs = request.data.get('saveEveryNEpochs')
        captionFileExtension = request.data.get('captionFileExtension')
        seed  = request.data.get('seed')
        cacheLatent = request.data.get('cacheLatent')
        cacheLatentToDisk = request.data.get('cacheLatentToDisk')
        lrScheduler = request.data.get('lrScheduler')
        optimizer = request.data.get('optimizer')
        maxGradNorm = request.data.get('maxGradNorm')
        lrSchedulerArg = request.data.get('lrSchedulerArg')
        optimizerArg = request.data.get('optimizerArg')
        learningRate = request.data.get('learningRate')
        lrWarmup = request.data.get('lrWarmup')
        lrCycle = request.data.get('lrCycle')
        lrPower = request.data.get('lrPower')
        maxResolution = request.data.get('maxResolution')
        stopTE = request.data.get('stopTE')
        enableBuckets = request.data.get('enableBuckets')
        minBucketRes = request.data.get('minBucketRes')
        maxBucketRes = request.data.get('maxBucketRes')
        textEncoderLR = request.data.get('textEncoderLR')
        unetEncoderLR = request.data.get('unetEncoderLR')
        cacheTextEncoderOutput = request.data.get('cacheTextEncoderOutput')
        noHalfVAE = request.data.get('noHalfVAE')
        
        # Save submitted form data to the database
        details = SubmitForm(config=config, accelerateLaunch=accelerateLaunch, 
                             model=model, metadata=metadata, folders=folders, datasetPreparation=datasetPreparation,
                             presets=presets, loraType=loraType, networkWeights=networkWeights, 
                             dimFromWeight=dimFromWeight, trainBatchSize=trainBatchSize, epoch=epoch,
                             maxTrainEpoch=maxTrainEpoch, maxTrainStep=maxTrainStep, saveEveryNEpochs=saveEveryNEpochs,
                             captionFileExtension=captionFileExtension, seed=seed, cacheLatent=cacheLatent, 
                             cacheLatentToDisk=cacheLatentToDisk, lrScheduler=lrScheduler, optimizer=optimizer,
                             maxGradNorm=maxGradNorm, lrSchedulerArg= lrSchedulerArg, optimizerArg=optimizerArg,
                             learningRate=learningRate, lrWarmup=lrWarmup, lrCycle=lrCycle, lrPower=lrPower,
                             maxResolution=maxResolution, stopTE=stopTE, enableBuckets=enableBuckets,
                             minBucketRes=minBucketRes, maxBucketRes=maxBucketRes, textEncoderLR= textEncoderLR, unetEncoderLR=unetEncoderLR,
                             cacheTextEncoderOutput=cacheTextEncoderOutput, noHalfVAE=noHalfVAE)
        details.save()

        # Create a dictionary with the form data
        form_data = {
            'config': config,
            'accelerateLaunch': accelerateLaunch,
            'model': model,
            'metadata': metadata,
            'folders': folders,
            'datasetPreparation': datasetPreparation,
            'presets': presets,
            'loraType': loraType,
            'networkWeights': networkWeights,
            'dimFromWeight': dimFromWeight,
            'trainBatchSize': trainBatchSize,
            'epoch': epoch,
            'maxTrainEpoch': maxTrainEpoch,
            'maxTrainStep': maxTrainStep,
            'saveEveryNEpochs': saveEveryNEpochs,
            'captionFileExtension': captionFileExtension,
            'seed': seed,
            'cacheLatent': cacheLatent,
            'cacheLatentToDisk': cacheLatentToDisk,
            'lrScheduler': lrScheduler,
            'optimizer': optimizer,
            'maxGradNorm': maxGradNorm,
            'lrSchedulerArg': lrSchedulerArg,
            'optimizerArg': optimizerArg,
            'learningRate': learningRate,
            'lrWarmup': lrWarmup,
            'lrCycle': lrCycle,
            'lrPower': lrPower,
            'maxResolution': maxResolution,
            'stopTE': stopTE,
            'enableBuckets': enableBuckets,
            'minBucketRes': minBucketRes,
            'maxBucketRes': maxBucketRes,
            'textEncoderLR': textEncoderLR,
            'unetEncoderLR': unetEncoderLR,
            'cacheTextEncoderOutput': cacheTextEncoderOutput,
            'noHalfVAE': noHalfVAE,
        }

        # Write form data to a JSON file
        with open('form_data.json', 'w') as json_file:
            json.dump(form_data, json_file)

        # Return a success response
        return Response(status=status.HTTP_201_CREATED)
    return HttpResponse("HI WE DIDNT SUPPORT GET REQUEST")


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

def download_json_file(request):
    # Read the JSON file content
    with open('form_data.json', 'r') as file:
        json_content = file.read()

    # Set response content type
    response = HttpResponse(json_content, content_type='application/json')

    # Set Content-Disposition header to force download
    response['Content-Disposition'] = 'attachment; filename="form_data.json"'

    return response