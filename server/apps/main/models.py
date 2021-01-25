from django.db import models
from typing import final


@final
class Task_ID(models.Model):

    task_id = models.CharField(max_length=100)

    class Meta():
        verbose_name = 'Task_id'
        verbose_name_plural = 'Task_ids'

    def __str__(self) -> str:
        return '<Task_id {0}>'.format(self.task_id)
