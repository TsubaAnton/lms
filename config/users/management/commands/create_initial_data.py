from django.core.management.base import BaseCommand
from users.models import User, Payment
from materials.models import Course, Lesson
from django.utils import timezone


class Command(BaseCommand):
    help = 'Create initial data for users, courses, lessons, and payments'

    def handle(self, *args, **kwargs):

        user1 = User.objects.create(
            email='user1@example.com',
            phone='1234567890',
            city='CityA'
        )
        user1.set_password('password123')
        user1.save()

        user2 = User.objects.create(
            email='user2@example.com',
            phone='0987654321',
            city='CityB'
        )
        user2.set_password('password123')
        user2.save()

        course1 = Course.objects.create(
            name='Course 1',
            description='Description for Course 1'
        )

        course2 = Course.objects.create(
            name='Course 2',
            description='Description for Course 2'
        )

        lesson1 = Lesson.objects.create(
            name='Lesson 1',
            description='Description for Lesson 1',
            course=course1
        )

        lesson2 = Lesson.objects.create(
            name='Lesson 2',
            description='Description for Lesson 2',
            course=course2
        )

        Payment.objects.create(
            user=user1,
            payment_date=timezone.now(),
            course=course1,
            lesson=None,
            amount_payment=1000,
            payment_method='cash'
        )

        Payment.objects.create(
            user=user2,
            payment_date=timezone.now(),
            course=None,
            lesson=lesson1,
            amount_payment=500,
            payment_method='transfer'
        )

        self.stdout.write(self.style.SUCCESS('Successfully created initial data'))
