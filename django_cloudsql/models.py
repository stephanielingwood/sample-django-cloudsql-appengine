from django.db import models

class Score(models.Model):
  score = models.IntegerField()
  timestamp = models.DateTimeField(auto_now_add=True)
