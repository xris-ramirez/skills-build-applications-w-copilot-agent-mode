
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, Activity, Workout, Leaderboard

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'teams']

class TeamSerializer(serializers.ModelSerializer):
	members = UserSerializer(many=True, read_only=True)
	class Meta:
		model = Team
		fields = ['id', 'name', 'members']

class WorkoutSerializer(serializers.ModelSerializer):
	class Meta:
		model = Workout
		fields = ['id', 'name', 'description', 'duration']

class ActivitySerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	workout = WorkoutSerializer(read_only=True)
	class Meta:
		model = Activity
		fields = ['id', 'user', 'activity_type', 'duration', 'date', 'notes', 'workout']

class LeaderboardSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	team = TeamSerializer(read_only=True)
	class Meta:
		model = Leaderboard
		fields = ['id', 'user', 'team', 'score']
