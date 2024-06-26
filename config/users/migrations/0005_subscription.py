# Generated by Django 4.2 on 2024-06-01 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_course_owner_lesson_owner'),
        ('users', '0004_user_is_moderator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='materials.course', verbose_name='Курс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
            },
        ),
    ]
