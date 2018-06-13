import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

class TodoQuerySet(QuerySet):
    def my_tasks(self, user_id):
        return self.filter(created_by=user_id).order_by('-priority')

    def from_higher(self):
        return self.order_by('-priority')

    def from_lower(self):
        return self.order_by('priority')

class Task(models.Model):
    def __str__(self):
        return self.name

    TASK_PRIORITY = (
        (3, 'HIGHER'),
        (2, 'MEDIUM'),
        (1, 'LOWER'),
    )

    name = models.CharField(max_length=100)
    priority = models.CharField(
        max_length=1,
        choices=TASK_PRIORITY,
        default=2,
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='example2')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='assigned_to')
    objects = TodoQuerySet.as_manager()  # Activate custom QuerySet