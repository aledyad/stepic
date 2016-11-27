from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import models as auth_models

# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        return []

    def popular(self):
        return []


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.ForeignKey(auth_models.User)
    likes = models.ManyToManyField(auth_models.User, related_name = '+')

    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(auth_models.User)
