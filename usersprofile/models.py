from django.db import models
from users.models import CustomUser

class Profile(models.Model):
    
    GENDER = (
        (0, 'Male'),
        (1, 'Female')
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    about = models.TextField(max_length=250, blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, default=0)

    def __str__(self):
        return self.user.user_name


