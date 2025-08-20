
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Team, Activity, Workout, Leaderboard

class APISmokeTest(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='testpass')
		self.client = APIClient()
		self.client.force_authenticate(user=self.user)

	def test_api_root(self):
		response = self.client.get(reverse('api-root'))
		self.assertEqual(response.status_code, 200)

	def test_users_endpoint(self):
		response = self.client.get(reverse('user-list'))
		self.assertEqual(response.status_code, 200)

	def test_teams_endpoint(self):
		response = self.client.get(reverse('team-list'))
		self.assertEqual(response.status_code, 200)

	def test_activities_endpoint(self):
		response = self.client.get(reverse('activity-list'))
		self.assertEqual(response.status_code, 200)

	def test_workouts_endpoint(self):
		response = self.client.get(reverse('workout-list'))
		self.assertEqual(response.status_code, 200)

	def test_leaderboard_endpoint(self):
		response = self.client.get(reverse('leaderboard-list'))
		self.assertEqual(response.status_code, 200)
