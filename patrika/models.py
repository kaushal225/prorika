from django.db import models
from authentication.models import User
from helpers.models import TrackingModel
# Create your models here.

class Problem(TrackingModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False) 
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    website=models.CharField(max_length=255)

    def __str__(self):
        return self.name