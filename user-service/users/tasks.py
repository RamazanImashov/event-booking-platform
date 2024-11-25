# users/tasks.py

from config.celery import app
from users.utils.utils import generate_user_id
from django.contrib.auth import get_user_model


def generate_and_assign_user_id(user_id, role):
    User = get_user_model()
    user = User.objects.get(pk=user_id)
    user.custom_id = generate_user_id(role)
    user.save()


@app.task
def generate_and_assign_user_id_celery(user_id, role):
    generate_and_assign_user_id(user_id, role)
