
from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	members = models.ManyToManyField(User, related_name='teams')

	def __str__(self):
		return self.name

class Workout(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	duration = models.PositiveIntegerField(help_text="Duration in minutes")

	def __str__(self):
		return self.name

class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	activity_type = models.CharField(max_length=100)
	duration = models.PositiveIntegerField(help_text="Duration in minutes")
	date = models.DateField()
	notes = models.TextField(blank=True)
	workout = models.ForeignKey(Workout, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return f"{self.user.username} - {self.activity_type} on {self.date}"

class Leaderboard(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
	score = models.IntegerField(default=0)

	def __str__(self):
		return f"{self.user.username} - {self.score}"
