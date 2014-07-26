import random
from models import Score

class Storage():
  def populate(self):
    new_score = Score()
    new_score.score = random.randint(1, 1234)
    new_score.save()

  def get_score(self):
    score_query = Score.objects.all().order_by('-timestamp')[:1]
    return score_query[0].score
