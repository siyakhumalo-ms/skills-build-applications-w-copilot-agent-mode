from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.activity = Activity.objects.create(user=self.user, type='Test', duration=10, date='2025-12-03')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=10, week=1)

    def test_user_email_unique(self):
        with self.assertRaises(Exception):
            User.objects.create(name='Another', email='test@example.com', team=self.team)

    def test_team_name(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_activity_type(self):
        self.assertEqual(self.activity.type, 'Test')

    def test_workout_name(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_leaderboard_points(self):
        self.assertEqual(self.leaderboard.points, 10)
