from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Question(models.Model):
    question_text = models.TextField(verbose_name='Текст вопроса')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікациї')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категорія')


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(verbose_name='Відповідь')


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='категорія')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name

