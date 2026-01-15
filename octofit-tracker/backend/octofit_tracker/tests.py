from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.assertEqual(str(team), 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC', description='DC superheroes')
        user = User.objects.create(email='batman@dc.com', username='Batman', team=team)
        self.assertEqual(str(user), 'Batman')

    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        user = User.objects.create(email='spiderman@marvel.com', username='Spiderman', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2023-01-01')
        self.assertEqual(str(activity), 'Spiderman - Running')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body workout')
        self.assertEqual(str(workout), 'Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        user = User.objects.create(email='ironman@marvel.com', username='Ironman', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(str(leaderboard), 'Ironman: 100')
