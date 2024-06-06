from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# class User(AbstractUser):
#     pass

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    username = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True)
    cover_photo = models.ImageField(upload_to='cover_photos/', blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    comments = models.BooleanField(default=False)
    candidates = models.BooleanField(default=False)
    offers = models.BooleanField(default=False)
    push_notifications = models.CharField(max_length=20, choices=[('everything', 'Everything'), ('same_as_email', 'Same as email'), ('nothing', 'No push notifications')])

    def __str__(self):
        return self.username


class SubmitForm(models.Model):
    config = models.CharField(max_length=100)
    accelerateLaunch = models.CharField(max_length=100)
    model = models.CharField(max_length=100) 
    metadata = models.CharField(max_length=30)
    folders = models.CharField(max_length=30)
    datasetPreparation = models.CharField(max_length=30)
    presets = models.CharField(max_length=30)
    loraType = models.CharField(max_length=30)
    networkWeights = models.CharField(max_length=50, null=True)
    dimFromWeight = models.BooleanField( null=True)
    trainBatchSize = models.CharField(max_length=30)
    epoch = models.CharField(max_length=40)
    maxTrainEpoch = models.CharField(max_length=30)
    maxTrainStep = models.CharField(max_length=30)
    saveEveryNEpochs = models.CharField(max_length=30)
    captionFileExtension = models.CharField(max_length=30)
    seed  = models.CharField(max_length=30, null= True)
    cacheLatent = models.CharField(max_length=30, null= True)
    cacheLatentToDisk = models.CharField(max_length=30, null= True)
    lrScheduler = models.CharField(max_length=30, null= True)
    optimizer = models.CharField(max_length=30, null= True)
    maxGradNorm = models.CharField(max_length=30, null= True)
    lrSchedulerArg = models.CharField(max_length=30, null= True)
    optimizerArg = models.CharField(max_length=30, null= True)
    learningRate = models.CharField(max_length=30, null= True)
    lrWarmup = models.CharField(max_length=30, null= True)
    lrCycle = models.CharField(max_length=30, null= True)
    lrPower = models.CharField(max_length=30, null= True)
    maxResolution = models.CharField(max_length=30, null= True)
    stopTE = models.CharField(max_length=30, null= True)
    enableBuckets = models.CharField(max_length=30, null= True)
    minBucketRes = models.CharField(max_length=30, null= True)
    maxBucketRes = models.CharField(max_length=30, null= True)
    textEncoderLR = models.CharField(max_length=30, null= True)
    unetEncoderLR = models.CharField(max_length=30, null= True)
    cacheTextEncoderOutput = models.CharField(max_length=30, null= True)
    noHalfVAE = models.CharField(max_length=30, null= True)
    



class NewSubmitForm(models.Model):
    config = models.CharField(max_length=100, null=True)
    accelerateLaunch = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null=True) 
    metadata = models.CharField(max_length=30, null=True)
    folders = models.CharField(max_length=30, null=True)
    datasetPreparation = models.CharField(max_length=30, null=True)
    presets = models.CharField(max_length=30, null=True)
    loraType = models.CharField(max_length=30, null=True)
    networkWeights = models.CharField(max_length=50, null=True)
    dimFromWeight = models.BooleanField( null=True)
    trainBatchSize = models.CharField(max_length=30, null=True)
    epoch = models.CharField(max_length=40, null=True)
    maxTrainEpoch = models.CharField(max_length=30, null=True)
    maxTrainStep = models.CharField(max_length=30, null=True)
    saveEveryNEpochs = models.CharField(max_length=30, null=True)
    captionFileExtension = models.CharField(max_length=30, null=True)
    seed  = models.CharField(max_length=30, null= True)
    cacheLatent = models.CharField(max_length=30, null= True)
    cacheLatentToDisk = models.CharField(max_length=30, null= True)
    lrScheduler = models.CharField(max_length=30, null= True)
    optimizer = models.CharField(max_length=30, null= True)
    maxGradNorm = models.CharField(max_length=30, null= True)
    lrSchedulerArg = models.CharField(max_length=30, null= True)
    optimizerArg = models.CharField(max_length=30, null= True)
    learningRate = models.CharField(max_length=30, null= True)
    lrWarmup = models.CharField(max_length=30, null= True)
    lrCycle = models.CharField(max_length=30, null= True)
    lrPower = models.CharField(max_length=30, null= True)
    maxResolution = models.CharField(max_length=30, null= True)
    stopTE = models.CharField(max_length=30, null= True)
    enableBuckets = models.CharField(max_length=30, null= True)
    minBucketRes = models.CharField(max_length=30, null= True)
    maxBucketRes = models.CharField(max_length=30, null= True)
    textEncoderLR = models.CharField(max_length=30, null= True)
    unetEncoderLR = models.CharField(max_length=30, null= True)
    cacheTextEncoderOutput = models.CharField(max_length=30, null= True)
    noHalfVAE = models.CharField(max_length=30, null= True)