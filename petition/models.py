from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Petition(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voters = models.ManyToManyField(User, related_name='petitions')
    votes = models.PositiveIntegerField(default=0)
    def __str__(self):
        return str(self.id)