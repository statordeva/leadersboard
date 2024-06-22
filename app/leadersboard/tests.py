from django.test import TestCase
from leadersboard.models import *
from leadersboard.jobs.jobs import decide_winner

class UserTest(TestCase):
    def setUp(self):
        User.objects.create(name="Name", age=20, points=0, address="Address")

    def test_user(self):
        user = User.objects.get(name="Name")
        self.assertEqual(user.name, "Name")
        self.assertEqual(user.age, 20)
        self.assertEqual(user.points, 0)
        self.assertEqual(user.address, "Address")

    def test_user_increment(self):
        user = User.objects.get(name="Name")
        user.increment_points()
        self.assertEqual(user.points, 1)

    def test_user_decrement(self):
        user = User.objects.get(name="Name")
        user.decrement_points()
        self.assertEqual(user.points, 0)

    def test_user_cannot_decrement(self):
        user = User.objects.get(name="Name")
        user.decrement_points()
        self.assertEqual(user.points, 0)

    def tearDown(self):
        User.objects.all().delete()


class WinnerTest(TestCase):
    def setUp(self):
        User.objects.create(name="User A", age=20, points=10, address="Address A")
        User.objects.create(name="User B", age=20, points=5, address="Address B")

    def test_winner(self):
        decide_winner()
        winner = Winner.objects.first()
        self.assertEqual(winner.user.name, "User A")
        self.assertEqual(winner.points, 10)

    def tearDown(self):
        Winner.objects.all().delete()
        User.objects.all().delete()


class DrawTest(TestCase):
    def setUp(self):
        User.objects.create(name="User A", age=20, points=1, address="Address A")
        User.objects.create(name="User B", age=20, points=1, address="Address B")

    def test_winner(self):
        decide_winner()
        winner = Winner.objects.first()
        self.assertEqual(winner, None)

    def tearDown(self):
        Winner.objects.all().delete()
        User.objects.all().delete()