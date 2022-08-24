from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    memo = models.TextField(blank=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    datecompleted = models.DateTimeField(null=True, blank=True, verbose_name='Дата выполнения')
    important = models.BooleanField(default=False, verbose_name='Важность')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Задачи'
        ordering = ('-created',)