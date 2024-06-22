from django.db import models
from faker import Faker
import factory
import random


class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    points = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def increment_points(self):
        self.points += 1
        self.save()

    def decrement_points(self):
        self.points -= 1
        if self.points < 0:
            self.points = 0

        self.save()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.LazyAttribute(lambda n: Faker().name())
    age = factory.LazyAttribute(lambda n: random.randint(5, 80))
    points = 0
    # points = factory.LazyAttribute(lambda n: random.randint(0, 100))
    address = factory.LazyAttribute(lambda n: Faker().address())


class Winner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name

