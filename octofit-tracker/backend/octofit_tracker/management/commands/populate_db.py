
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark')
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='pass', first_name='Steve', last_name='Rogers')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne')
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='pass', first_name='Clark', last_name='Kent')

        # Create activities
        Activity.objects.create(name='Running', user='ironman', team='Marvel')
        Activity.objects.create(name='Swimming', user='captain', team='Marvel')
        Activity.objects.create(name='Flying', user='superman', team='DC')
        Activity.objects.create(name='Martial Arts', user='batman', team='DC')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=200)
        Leaderboard.objects.create(team='DC', points=180)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 50 pushups')
        Workout.objects.create(name='Situps', description='Do 50 situps')
        Workout.objects.create(name='Squats', description='Do 50 squats')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
