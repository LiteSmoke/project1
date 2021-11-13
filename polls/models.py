from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):

    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.text

    def published_days_ago(self, days):
        return  timezone.now() - datetime.timedelta(days=days) <= self.pub_date <= timezone.now()

class Choise(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
