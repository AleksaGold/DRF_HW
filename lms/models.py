from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    """Класс для описания модели Course."""

    name = models.CharField(max_length=150, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание курса", **NULLABLE)
    preview = models.ImageField(
        upload_to="courses/previews", verbose_name="Превью (картинка)", **NULLABLE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец курса",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ("name",)

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"{self.name}"


class Lesson(models.Model):
    """Класс для описания модели Lesson."""

    name = models.CharField(max_length=150, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание урока", **NULLABLE)
    preview = models.ImageField(
        upload_to="lessons/previews", verbose_name="Превью (картинка)", **NULLABLE
    )
    video_link = models.URLField(verbose_name="Ссылка на видео", **NULLABLE)
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        related_name="lessons",
        **NULLABLE,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец урока",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ("name",)

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"{self.name} ({self.course})"


class Subscription(models.Model):
    """Класс для описания модели Subscription."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="subscription",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        related_name="subscription",
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        ordering = ("user", "course")

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"{self.user} - {self.course}"
