from django.db import models

class TaskList(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    desc = models.TextField(verbose_name='Описание')
    status = models.CharField(max_length=50, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'