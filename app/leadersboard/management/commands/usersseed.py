from django.core.management.base import BaseCommand, CommandError
from leadersboard.models import User, UserFactory
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of users to seed')


    def handle(self, *args, **options):
        if options['count'] < 1:
            raise CommandError('Count must be greater than 0')

        UserFactory.create_batch(options['count'])

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with users!'))