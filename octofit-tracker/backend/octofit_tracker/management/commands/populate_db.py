from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import Activity
from django.db import transaction
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            # Delete all data
            Activity.objects.all().delete()
            User.objects.all().exclude(is_superuser=True).delete()

            # Create teams
            teams = ['Marvel', 'DC']

            # Create users (superheroes)
            users = [
                {'username': 'ironman', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
                {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'team': 'Marvel'},
                {'username': 'batman', 'email': 'batman@dc.com', 'team': 'DC'},
                {'username': 'superman', 'email': 'superman@dc.com', 'team': 'DC'},
            ]
            user_objs = {}
            for u in users:
                user, _ = User.objects.get_or_create(username=u['username'], email=u['email'])
                user.set_password('password')
                user.save()
                user_objs[u['username']] = user

            # Create activities
            activities = [
                {'user': user_objs['ironman'], 'activity_type': 'Running', 'duration': 30, 'date': date.today(), 'notes': 'Morning run'},
                {'user': user_objs['spiderman'], 'activity_type': 'Cycling', 'duration': 45, 'date': date.today() - timedelta(days=1), 'notes': 'Evening ride'},
                {'user': user_objs['batman'], 'activity_type': 'Swimming', 'duration': 60, 'date': date.today() - timedelta(days=2), 'notes': 'Pool session'},
                {'user': user_objs['superman'], 'activity_type': 'Flying', 'duration': 120, 'date': date.today() - timedelta(days=3), 'notes': 'Sky patrol'},
            ]
            for act in activities:
                Activity.objects.create(**act)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
