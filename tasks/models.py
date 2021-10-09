from django.db import models

# Create your models here.

class Task(models.Model):
    """
    Задача
    """

    name = models.CharField("Наименование", max_length=255)
    description = models.CharField("Описание", max_length=1000)
    executors = models.ManyToManyField(
        "User",
        verbose_name="Исполнители"
    )
    finish_date = models.DateField("Дата завершения")
    attached_file = models.FileField("Прикрипленный файл")

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


