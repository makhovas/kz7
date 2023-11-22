
from django.conf import settings

from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Удалить всех пользователей и создать суперюзера'

    def handle(self, *args, **kwargs):

        User.objects.all().delete()
        user = User.objects.create(
            email=settings.EMAIL_HOST_USER,
            first_name='Admin',
            last_name='Adminov',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            chat_id='1084646498',
        )
        user.set_password('24586744')
        user.save()
