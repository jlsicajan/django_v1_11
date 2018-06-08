import datetime

from django.db import models


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


class UserTask(models.Model):
    def __str__(self):
        return self.id

    user_id = models.IntegerField()
    task_id = models.IntegerField()
