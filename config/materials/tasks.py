from celery import shared_task
from users.models import Subscription, User
from django.conf import settings
from django.core.mail import send_mail
from .models import Course
from django.utils import timezone
from datetime import timedelta


@shared_task
def send_course_update_mail(course_id):
    course = Course.objects.filter(id=course_id).first()
    if course:
        subscription = Subscription.objects.filter(course_id=course_id)
        for subs in subscription:
            send_mail(
                subject=f"Курс {course.name} обновлен",
                message=f"Курс {course.name} обновлен",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[subs.user.email],
                fail_silently=False
            )


@shared_task
def check_user_activity_task():
    user_list = User.objects.filter(is_active=True)
    for user in user_list:
        if user.last_login and user.last_login < (timezone.now() - timedelta(days=30)):
            user.is_active = False
            user.save()
