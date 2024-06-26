# Generated by Django 4.2 on 2024-05-19 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='materials/course/', verbose_name='Превью')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='materials/lesson/', verbose_name='Превью')),
                ('url', models.URLField(verbose_name='Ссылка на видео')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
