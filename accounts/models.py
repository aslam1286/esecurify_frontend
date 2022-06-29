from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

