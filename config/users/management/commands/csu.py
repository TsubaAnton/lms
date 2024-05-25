from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='onton@icloud.com',
            first_name='Onton',
            last_name='Onton',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('onton1010')
        user.save()
