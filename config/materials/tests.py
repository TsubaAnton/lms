from rest_framework.test import APITestCase, APIClient, force_authenticate
from .models import Course, Lesson
from users.models import User
from rest_framework import status
from django.urls import reverse


class LessonTestCase(APITestCase):

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

    def test_lesson_create(self):
        data = {'name': 'test_create', 'description': 'test_create',
                'course': self.course.id, 'url': 'https://www.youtube.com/'}
        response = self.client.post(reverse('materials:lesson_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_retrieve(self):
        data = {'name': self.lesson.name, 'description': self.lesson.description}
        response = self.client.get(reverse('materials:lesson_retrieve', kwargs={'pk': self.lesson.id}), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_update(self):
        lesson = Lesson.objects.create(
            name='test_lesson',
            description='test_description',
            url='https://www.youtube.com/',
            course=self.course
        )
        data = {'name': 'test_update', 'description': 'test_update',
                'course': self.course.id, 'url': 'https://www.youtube.com/'}
        response = self.client.patch(reverse('materials:lesson_update', kwargs={'pk': lesson.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_destroy(self):
        data = {'name': 'test_destroy', 'description': 'test_destroy'}
        response = self.client.delete(reverse('materials:lesson_destroy', kwargs={'pk': self.lesson.id}), data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
