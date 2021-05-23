from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.manager import Manager
import datetime


class Players(models.Model):
	name = models.CharField(max_length=255)
	position = models.CharField(max_length=255)
	bio = models.TextField()
	image_url = models.CharField(max_length=2083)

class Fixtures(models.Model):
	home_team = models.CharField(max_length=255)
	away_team = models.CharField(max_length=255)
	fixture_date = models.DateTimeField(default=timezone.now)
	competition_image = models.CharField(max_length=2083)
	description = models.CharField(max_length=255)
	venue_image = models.CharField(max_length=2083)


class Transfernews(models.Model):
	player_name = models.CharField(max_length=255)
	player_image = models.CharField(max_length=2083)
	player_description = models.CharField(max_length=3000)
	date_posted = models.DateTimeField(default=timezone.now)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
    	super().save(*args, **kwargs)


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	transfernews = models.ForeignKey(Transfernews, related_name="comments", on_delete=models.CASCADE)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.transfernews.player_name, self.user.username)





    	





	
