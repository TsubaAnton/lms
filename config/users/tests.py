from rest_framework.test import APITestCase, APIClient, force_authenticate
from materials.models import Course, Lesson
from .models import User, Subscription
from django.urls import reverse


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        self.course = Course.objects.create(
            name='test_course',
            description='test_description'
        )
        self.lesson = Lesson.objects.create(
            name='test_lesson',
            description='test_description',
            url='https://www.youtube.com/',
            course=self.course
        )
        self.user = User.objects.create(
            email='test_email@test.com',
            password='1234',
            is_moderator=False
        )
        self.moderator = User.objects.create(
            email='moderator@test.com',
            password='12345678',
            is_moderator=True
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_subscription_activate(self):
        url = reverse('users:subscription')
        data = {'course_id': self.course.id}

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Подписка добавлена'})

    def test_subscription_deactivate(self):
        Subscription.objects.create(user=self.user, course=self.course)
        url = reverse('users:subscription')
        data = {'course_id': self.course.id}

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Подписка удалена'})
