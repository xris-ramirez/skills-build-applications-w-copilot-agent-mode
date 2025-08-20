from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import Activity
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Populate the database with test Activity data.'

    def handle(self, *args, **kwargs):
        # Create a test user if not exists
        user, created = User.objects.get_or_create(username='testuser')
        if created:
            user.set_password('testpass')
            user.save()

        # Create test activities
        activities = [
            {'activity_type': 'Running', 'duration': 30, 'date': date.today(), 'notes': 'Morning run'},
            {'activity_type': 'Cycling', 'duration': 45, 'date': date.today() - timedelta(days=1), 'notes': 'Evening ride'},
            {'activity_type': 'Swimming', 'duration': 60, 'date': date.today() - timedelta(days=2), 'notes': 'Pool session'},
        ]
        for act in activities:
            Activity.objects.get_or_create(user=user, **act)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
