from django.db import models

from django.contrib.auth.models import User
from django.conf import settings

from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	is_agent = models.BooleanField(default=False)
	bio = models.TextField(blank=True)
	review = models.TextField(blank=True)
	profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

	def __str__(self):
		return self.user.username

	def save(self, *args, **kwargs):
        
		super().save(*args, **kwargs)

        
		# agent_profile, created = AgentProfile.objects.get_or_create(user=self.user)

		# agent_profile.is_agent = self.is_agent
		# agent_profile.save()
