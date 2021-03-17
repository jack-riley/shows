from django.db import models
from datetime import datetime



# Create your models here.

class DataManager(models.Manager):
    def validator (self,postData) :
        errors = {}
        if len (postData['title']) < 2:
            errors['title'] = "Title should be at least two (2) characters"
        
        if len (postData['network']) < 3:
            errors['network'] = "Network should be at least three (3) characters"  
        if len (postData['desc']) > 0:
            if len (postData['desc']) < 10:
                errors['desc'] = "Description is optional, but should be at least ten (10) characters if present"
        current_date = datetime.strftime(datetime.today(), '%Y,%m,%d')
        if current_date < (postData['release_date']) :
            errors['release_date'] = "Release date must be in the past"
        
        if postData['new'] == "new":
            titles = (Show.objects.filter(title=postData['title']))

            if titles:
                errors['same_title'] = "Title already in use. Title cannot be a duplicate"
       
        return errors

class Network (models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DataManager()

class Show (models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    network = models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DataManager()


