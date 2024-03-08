from django.db import models
from django.contrib.auth.models import User
ADMIN = 'admin'
VIEWER = 'customer'
USER_TYPE = [
        (ADMIN, 'admin'),
        (VIEWER, 'customer'),
    ]
# Create your models here.
class UserAccount(models.Model):
     user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
     User_Type = models.CharField(max_length=20,choices=USER_TYPE,default=VIEWER,)

     def __str__(self):
        return str(self.user.first_name)