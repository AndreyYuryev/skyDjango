from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='user2@sky.pro',
            first_name='User2',
            last_name='skypro',
            is_staff=False,
            is_superuser=False,
            is_active=True,
        )
        user.set_password('123qaz')
        user.save()