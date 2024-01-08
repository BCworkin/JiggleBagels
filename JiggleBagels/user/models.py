from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    user_profile = models.OneToOneField('UserProfile', on_delete=models.CASCADE, null=True, related_name='user_profile')

    class Meta:
        db_table = 'user'

    error_message = ''

    def set_error_info(self, msg: str):
        self.error_message = msg

    def get_error_info(self):
        return self.error_message
    
class UserProfile(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    ph_number = models.IntegerField(null=True, blank=True, verbose_name="primary phone number")
    address = models.CharField(null=True, blank=True, max_length=150, verbose_name='address')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'user_profile'