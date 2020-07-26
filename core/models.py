from django.db import models
from django.contrib.auth.models import User
from .gcs import GoogleCloudStorage
import uuid

# Create your models here.

class Pet(models.Model):
    city = models.CharField(max_length=100)    
    description = models.TextField()
    phone = models.CharField(max_length=11, null=True)
    email = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    end_date = models.DateTimeField(null=True, blank=True)
    begin_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    photo = models.CharField(max_length=1000)
    
    def __str__(self):
        return str(self.id)

    def get_photo(self):
        gcs = GoogleCloudStorage()
        return gcs.get_file(self.photo)

    def upload_photo(self, photo):
        if self.photo:
            self.delete_photo()
        photo_name = f'{photo}-{uuid.uuid4()}'
        gcs = GoogleCloudStorage()
        gcs.save_file(photo, photo_name)
        self.photo = photo_name
        self.save()

    def delete_photo(self):
        gcs = GoogleCloudStorage()
        gcs.delete_file(self.photo)
            
        


    class Meta:
        db_table = 'pet_lost'