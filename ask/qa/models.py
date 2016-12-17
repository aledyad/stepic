from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import models as auth_models
from django.core.urlresolvers import reverse

# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(auth_models.User)
    likes = models.ManyToManyField(auth_models.User, related_name = '+')
    objects = QuestionManager()

    def get_url(self):
        return reverse('question', args=[self.pk])

    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(auth_models.User)
